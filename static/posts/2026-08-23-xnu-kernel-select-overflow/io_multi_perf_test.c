#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/select.h>
#include <poll.h>
#include <string.h>
#include <fcntl.h>
#include <sys/event.h>

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
    FD_SET(pipes[0][0], &readfds); // FD_SETSIZE 이내의 정상적인 fd 하나만 등록

    write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1);

    struct timeval timeout = {0, 0};
    int ret = select(10000, &readfds, NULL, NULL, &timeout); // nfds만 부풀림
    if (ret < 0) {
      perror("select");
    }

    read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1);
  }
  end = get_time_us();
  printf("select, avg %.2f us\n", (double)(end - start) / ITERATIONS);

cleanup:
  for (i = 0; i < MAX_FD_COUNT; i++)
  {
    close(pipes[i][0]);
    close(pipes[i][1]);
  }

  return 0;
}
