# 🤖 Everytimeless Bot

![screenshot](https://user-images.githubusercontent.com/50603255/91010513-99620780-e61d-11ea-8ec0-f91cce84daa6.png)

에타([everytime.kr](https://everytime.kr))의 새 글을 키워드로 감지해 알려주는 텔레그램 봇

## 사전 준비

* 항상 켜져 있는 리눅스 서버
* [BotFather](https://t.me/botfather)를 이용한 텔레그램 봇 발급
* 봇의 알림을 받을 채팅 방 고유 번호

## 설치

이 저장소를 클론(clone)해 주세요.

```shell
git clone https://github.com/nbsp1221/everytimeless-bot.git
cd everytimeless-bot
```

`.env` 파일을 열어 환경 변수를 설정해 주세요. 다음과 같은 4가지 값을 설정해야 합니다.

* `TELEGRAM_BOT_TOKEN`: 봇의 토큰(token) 값
* `TELEGRAM_BOT_CHAT_ID`: 채팅 방 고유 번호
* `EVERYTIME_ID`: 에타([everytime.kr](https://everytime.kr))의 아이디
* `EVERYTIME_PASSWORD`: 에타([everytime.kr](https://everytime.kr))의 비밀번호

### 🐳 [도커](https://www.docker.com/)를 사용하고 있나요?

[docker-compose](https://docs.docker.com/compose/) 도구를 이용해 쉽게 설치할 수 있습니다.

```shell
docker-compose up
```

모든 게 정상적으로 완료되면, 여러분이 설정한 텔레그램 채팅 방으로 안내 메시지가 올 것입니다!

### 👨‍💻 수동으로 설치

파이썬 의존성 관리 도구인 [Poetry](https://python-poetry.org/)를 설치합니다.

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

프로젝트 의존성을 설치합니다.

```shell
poetry install
```

프로그램을 실행합니다.

```shell
poetry run python src/main.py
```

## 사용 방법

확인할 게시판을 `/add board` 명령어로 추가합니다. 게시판 번호를 입력해야 합니다. 게시판 주소에서 이를 확인할 수 있으며 아래는 '광운대학교'의 '자유 게시판'을 추가한 예시입니다.

```
/add board 370443
```

키워드를 `/add keyword` 명령어로 추가합니다. 아래는 '프로그래밍' 키워드를 추가한 예시입니다.

```
/add keyword 프로그래밍
```

게시판 설정과 키워드 설정이 완료되면 키워드가 포함된 새 글이 올라올 경우 텔레그램 봇이 이를 확인하고 메시지를 보내드립니다.

## 명령어 안내

* `/help`: 명령어 확인
* `/add [board | keyword] <value>`: 게시판 또는 키워드 추가
* `/remove [board | keyword] <value>`: 게시판 또는 키워드 삭제
* `/show`: 추가된 목록 확인
