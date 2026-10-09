---
layout: post
title: 'simple-irc: C로 구현한 간이 IRC 서버'
date: '2026-10-09'
category: [report]
tags: [c, socket]
---

〈네트워크시스템〉 과제 노트

[`ShapeLayer/simple-irc`](https://github.com/ShapeLayer/simple-irc)

<br />

Simple IRC는 이름과는 다르게 IRC를 구현한 것은 아니다. 실시간 다중 사용자 채팅의 구현일 뿐이다. `socket`, `bind`, `listen` 사용의 기초적인 예제라고 할 수 있다.  

## 서버 측 초기화

[`server/src/server_sess.c:40-51`](https://github.com/ShapeLayer/simple-irc/blob/main/server/src/server_sess.c):

```c
void server_sess_open(server_sess_t *sess)
{
  if (bind(sess->fd, (struct sockaddr *)&sess->address, sizeof(sess->address)) < 0)
  {
    PANIC("Error during binding the socket (bind)");
  }
  sess->addrlen = sizeof(sess->address);


  if (listen(sess->fd, 3) < 0)
  {
    PANIC("Error during starting listening on the socket (listen)");
  }


  printf("Simple Chat Server started on port %d\n", sess->port);
}
```

<br />

[`server/src/main.c:73-80`](https://github.com/ShapeLayer/simple-irc/blob/main/server/src/main.c):

```c
server_sess_t *server_sess;
server_sess = calloc(1, sizeof(server_sess_t));
if (!server_sess) PANIC("Failed to allocate server session");
init_server_sess(server_sess);
printf("Server session initialized.\n");
server_sess_set_port(server_sess, args.port);
printf("Starting server on port %d...\n", args.port);


server_sess_open(server_sess);
```

서버 측에서는 서버 세션 디스크립터 `server_sess_t`를 생성하고 지정된 포트로 바인딩을 시도한다. 바인딩 과정에서 생성한 소켓 fd를 `listen` 호출에 사용하여 fd로 들어오는 연결을 수신 대기한다.   

<br />

[`serever/src/main.c:81`](https://github.com/ShapeLayer/simple-irc/blob/main/server/src/main.c):

```c
while (1) server_sess_update(server_sess);
```

서버 세션 초기화 과정에 문제가 발생하면 이미 `PANIC` 되었으므로, 서버가 정상 개방된 코드 흐름에서만 세션 업데이트 핸들러에 진입할 수 있다. 업데이트 핸들러 `server_sess_update`는 내부적으로 바인드된 fd에 이벤트가 발생했는지 확인하고, 이벤트에 따라 적절한 핸들러를 호출한다.  

<br />

업데이트 핸들러에서도 초기화 과정이 있다. 이 과정에서는 fd를 감시할 소켓 집합을 구성한다.   

[`server/src/server_sess.c:62-76`](https://github.com/ShapeLayer/simple-irc/blob/main/server/src/server_sess.c):

```c
FD_ZERO(&sess->readfds);
FD_SET(sess->fd, &sess->readfds);
sess->sd_cnt = sess->fd;

for (int i = 0; i < SERVER_MAX_CLIENT_CONNECTIONS; i++)
{
  int sd = sess->clients[i].socket;
  if (sd > 0)
    FD_SET(sd, &sess->readfds);
  if (sd > sess->sd_cnt)
    sess->sd_cnt = sd;
}

sess->__activity = select(sess->sd_cnt + 1, &sess->readfds, NULL, NULL, NULL);
if (sess->__activity < 0) PANIC("Error during select operation (select)");
```

매회 업데이트마다 현재 연결 목록으로 읽기 감시 집합을 다시 구성한다. 연결 목록의 업데이트를 반영하고, `select`가 수정한 감시 집합을 다시 의도한 상태로 복원한다.<sup>1</sup>

<br />

<sup>1</sup> `select`는 입력으로 주어진 감시 집합에서 읽기 준비가 된 fd만을 플래그해 감시 집합을 수정한다.  

```c
FD_ZERO(&readfds);
FD_SET(3, &readfds);
FD_SET(4, &readfds);
FD_SET(5, &readfds);

/*
   호출 전 readfds: {3, 4, 5}
   fd 4만 읽기 준비 상태가 됨
*/
select(6, &readfds, NULL, NULL, NULL);
/* 반환 후 readfds: {4} */
```

이렇게 되면 다음 호출에서는 `4`만 감시하게 되므로, 매회 업데이트마다 감시 집합을 재구성해야 한다.  

## 클라이언트 측 초기화

[`client/src/main.c:40-46`](https://github.com/ShapeLayer/simple-irc/blob/main/client/src/main.c):

```c
client_sess_t *client_sess;
client_sess = calloc(1, sizeof(client_sess_t));
if (!client_sess) PANIC("Failed to allocate client session");

init_client_sess(client_sess);
client_sess_connect(client_sess);

while (1) client_sess_update(client_sess);
```

클라이언트 측에서도 비슷한 초기화 과정을 거친다. `client_sess_connect`는 서버에 연결을 시도하고, 연결이 성공하면 fd를 반환한다. 마찬가지로 `PANIC` 되지 않았다면 세션 업데이트 핸들러 `client_sess_update`를 호출하는 데 큰 문제가 없다.  

<br />

[`client/src/client_sess.c:49-51`](https://github.com/ShapeLayer/simple-irc/blob/main/client/src/client_sess.c):

```c
FD_ZERO(&sess->readfds);
FD_SET(STDIN_FILENO, &sess->readfds);
FD_SET(sess->sock, &sess->readfds);
```

클라이언트 측 업데이트 핸들러에서는 표준 입력과 서버와의 연결 소켓을 감시한다. 표준 입력은 사용자가 입력한 메시지를 서버로 전송하기 위해 감시하고, 서버와의 연결 소켓은 서버가 보낸 메시지를 수신하기 위해 감시한다.  

## 새 연결

[`client/src/main.c:17`](https://github.com/ShapeLayer/simple-irc/blob/main/client/src/main.c):

```c
client_sess_connect(client_sess);
```

[`client/src/client_sess.c:40-41`](https://github.com/ShapeLayer/simple-irc/blob/main/client/src/client_sess.c):
```c
if (connect(sess->sock, (struct sockaddr *)&sess->addr, sizeof(sess->addr)) < 0)
  PANIC("Connection Failed (connect)");
```

클라이언트 측에서 소켓 fd를 `connect` 호출에 사용하여 서버에 연결을 시도한다. 연결이 성공하면 fd를 반환하고, 실패하면 `PANIC` 된다.

<br />

[`server/src/server_sess.c:79-100`](https://github.com/ShapeLayer/simple-irc/blob/main/server/src/server_sess.c)

```c
// handling new connections
if (FD_ISSET(sess->fd, &sess->readfds))
{
  if ((sess->__new_socket = accept(sess->fd, (struct sockaddr *)&sess->address, (socklen_t *)&sess->addrlen)) < 0)
  {
    PANIC("Error during accepting a new connection (accept)");
  }

  for (int i = 0; i < SERVER_MAX_CLIENT_CONNECTIONS; i++)
  {
    if (sess->clients[i].socket == 0)
    {
      sess->clients[i].socket = sess->__new_socket;
      printf("New connection: Guest%d\n", i);

      char welcome[STRING_BUFFER_SIZE];
      snprintf(welcome, sizeof(welcome), "Welcome! You are Guest%d. Use '/nick <name>' to change nickname.\n", i);
      send_to_socket(sess->__new_socket, welcome);
      break;
    }
  }
}
```

만약 서버 측에서 듣기 소켓에 이벤트가 발생(즉, 새 연결 요청이 들어옴)했다면, 연결을 `accept`하고 빈 클라이언트 슬롯을 찾아 새 소켓을 저장한다. 이어서 접속한 클라이언트 측에 환영 메시지를 전송한다. 클라이언트는 기본적으로 `Guest0`, `Guest1`과 같은 닉네임을 부여받는다.  

## 이벤트 핸들링

[`server/src/server_sess.c:103-125`](https://github.com/ShapeLayer/simple-irc/blob/main/server/src/server_sess.c):

```c
for (int i = 0; i < SERVER_MAX_CLIENT_CONNECTIONS; i++)
{
  int sd = sess->clients[i].socket;
  if (FD_ISSET(sd, &sess->readfds))
  {
    memset(sess->__str_buf, 0, STRING_BUFFER_SIZE);
    if ((sess->__valread = read(sd, sess->__str_buf, STRING_BUFFER_SIZE)) == 0)
    {
      // disconnection
      close(sd);
      sess->clients[i].socket = 0;
      printf("User disconnected: %s\n", sess->clients[i].nickname);
    }
      else
      {
      if (sess->__valread >= STRING_BUFFER_SIZE)
        sess->__str_buf[STRING_BUFFER_SIZE - 1] = '\0';
      else
        sess->__str_buf[sess->__valread] = '\0';
      server_sess_handle_client_message(sess, i, sess->__str_buf);
    }
  }
}
```

이어지는 서버 측 흐름에서는 모든 클라이언트 소켓을 전수검사하여 이벤트 발생을 확인한다. 만약 클라이언트 소켓에 이벤트가 발생했다면 `read`해 데이터를 가져온다. 반환값이 0이면 상대가 연결을 종료한 것이므로 소켓을 닫고 슬롯을 비운다. 메시지 데이터는 `NUL`을 추가하여 핸들러 `server_sess_handle_client_message`를 호출해 메시지를 처리한다. 대부분의 상황에서는 메시지를 클라이언트에 브로드캐스트하고 복귀한다.  

<br />

[`client/src/client_sess.c:58-71`](https://github.com/ShapeLayer/simple-irc/blob/main/client/src/client_sess.c):

```c
// handling incoming messages
if (FD_ISSET(sess->sock, &sess->readfds))
{
  memset(sess->__str_buf, 0, STRING_BUFFER_SIZE);
  sess->__valread = read(sess->sock, sess->__str_buf, STRING_BUFFER_SIZE);
  
  if (sess->__valread == 0)
  {
    client_sess_on_disconnected(sess);
    return;
  }
  
  printf("%s", sess->__str_buf);
}
```

한편 클라이언트 측에서는 서버와의 연결 소켓에 이벤트가 발생했는지 확인한다. 이벤트가 발생했다면 데이터를 `read`, 반환값이 0이면 서버가 연결을 종료한 것이므로 연결 종료 핸들러를 호출한다. 메시지 데이터는 그대로 출력한다.  

[`client/src/client_sess.c:73-81`](https://github.com/ShapeLayer/simple-irc/blob/main/client/src/client_sess.c):

```c
// handling message input
if (FD_ISSET(0, &sess->readfds))
{
  memset(sess->__str_buf, 0, STRING_BUFFER_SIZE);
  if (fgets(sess->__str_buf, STRING_BUFFER_SIZE, stdin) != NULL)
  {
    send(sess->sock, sess->__str_buf, strlen(sess->__str_buf), 0);
  }
}
```

또한 표준 입력에 이벤트가 발생했는지 확인한다. 이벤트가 발생했다면 데이터를 `fgets`하고, 서버에 `send` 한다.  
