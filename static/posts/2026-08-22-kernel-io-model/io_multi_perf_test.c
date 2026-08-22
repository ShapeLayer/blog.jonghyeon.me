#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/select.h>
#include <poll.h>
#include <string.h>
#include <fcntl.h>

#ifdef __linux__
#include <sys/epoll.h>
#define OS_TYPE "epoll"
#elif defined(__APPLE__) || defined(__FreeBSD__) || defined(__OpenBSD__) || defined(__NetBSD__)
#include <sys/event.h>
#define OS_TYPE "kqueue"
#else
#define OS_TYPE "null"
#endif

#define MAX_FD_COUNT 5000 // 감시할 파일 디스크립터 수
#define ITERATIONS 10000  // 반복 횟수

// 시간 측정
long long get_time_us()
{
  struct timeval tv;
  gettimeofday(&tv, NULL);
  return (long long)tv.tv_sec * 1000000 + tv.tv_usec;
}

int main()
{
  int pipes[MAX_FD_COUNT][2];
  int i, j;
  long long start, end;
  char dummy = 'a';

  printf("Supports: %s\n", OS_TYPE);
  printf("FD: %d, Loop: %d\n\n", MAX_FD_COUNT, ITERATIONS);

  // Create fds
  for (i = 0; i < MAX_FD_COUNT; i++)
  {
    if (pipe(pipes[i]) < 0)
    {
      perror("creating pipe failed.");
      exit(1);
    }
    // non-blocking: select/poll/epoll/kqueue가 블로킹되어 측정에 영향을 주지 않도록 설정
    fcntl(pipes[i][0], F_SETFL, O_NONBLOCK);
  }

  /**
   * select
   */
  start = get_time_us();
  for (i = 0; i < ITERATIONS; i++)
  {
    fd_set readfds;
    FD_ZERO(&readfds);
    int max_fd = 0;
    for (j = 0; j < MAX_FD_COUNT; j++)
    {
      FD_SET(pipes[j][0], &readfds);
      if (pipes[j][0] > max_fd)
        max_fd = pipes[j][0];
    }

    write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1); // 마지막 FD에 이벤트 발생

    struct timeval timeout = {0, 0};
    select(max_fd + 1, &readfds, NULL, NULL, &timeout);

    read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1); // clear
  }
  end = get_time_us();
  printf("select, avg %.2f us\n", (double)(end - start) / ITERATIONS);

  /**
   * poll
   */
  struct pollfd fds[MAX_FD_COUNT];
  for (i = 0; i < MAX_FD_COUNT; i++)
  {
    fds[i].fd = pipes[i][0];
    fds[i].events = POLLIN;
  }

  start = get_time_us();
  for (i = 0; i < ITERATIONS; i++)
  {
    write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1);
    poll(fds, MAX_FD_COUNT, 0);
    read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1);
  }
  end = get_time_us();
  printf("poll, avg %.2f us\n", (double)(end - start) / ITERATIONS);

  /**
   * epoll/kqueue
   */
#ifdef __linux__
  // Linux epoll
  int epfd = epoll_create1(0);
  struct epoll_event ev, evs[MAX_FD_COUNT];
  for (i = 0; i < MAX_FD_COUNT; i++)
  {
    ev.events = EPOLLIN;
    ev.data.fd = pipes[i][0];
    epoll_ctl(epfd, EPOLL_CTL_ADD, pipes[i][0], &ev);
  }

  start = get_time_us();
  for (i = 0; i < ITERATIONS; i++)
  {
    write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1);
    epoll_wait(epfd, evs, MAX_FD_COUNT, 0);
    read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1);
  }
  end = get_time_us();
  close(epfd);

#elif defined(__APPLE__) || defined(__FreeBSD__) || defined(__OpenBSD__) || defined(__NetBSD__)
  // BSD/macOS kqueue
  int kq = kqueue();
  struct kevent change_list[MAX_FD_COUNT];
  struct kevent event_list[MAX_FD_COUNT];
  struct timespec timeout = {0, 0};

  for (i = 0; i < MAX_FD_COUNT; i++)
  {
    EV_SET(&change_list[i], pipes[i][0], EVFILT_READ, EV_ADD, 0, 0, NULL);
  }
  // 최초 등록
  kevent(kq, change_list, MAX_FD_COUNT, NULL, 0, NULL);

  start = get_time_us();
  for (i = 0; i < ITERATIONS; i++)
  {
    write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1);
    // kqueue 이벤트 대기
    kevent(kq, NULL, 0, event_list, MAX_FD_COUNT, &timeout);
    read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1);
  }
  end = get_time_us();
  close(kq);
#else
  goto cleanup;
#endif

  printf("%s, avg %.2f us\n", OS_TYPE, (double)(end - start) / ITERATIONS);

cleanup:
  for (i = 0; i < MAX_FD_COUNT; i++)
  {
    close(pipes[i][0]);
    close(pipes[i][1]);
  }

  return 0;
}
