# Bot Helper





## Описание
Бот-помощник создан для автоматизации ответов на типичные вопросы пользователей. В случае сложных запросов бот перенаправляет их на операторов, что позволяет сократить время ожидания и повысить эффективность службы поддержки. Бот использует обучаемую нейросеть для распознавания и обработки вопросов.


## Пример
Telegram-бот доступен по ссылке: [Bot Helper](https://t.me/devman_rokyl_bot)

# Запуск проекта

### Предварительные требования
- Python 3.6 и выше
- Виртуальное окружение (рекомендуется)
- API-ключ для Telegram-бота ([инструкция](https://way23.ru/регистрация-бота-в-telegram.html))
- Ключ доступа API для ВКонтакте ([инструкция](https://vk.com/dev/access_token))
- `project_id` и файл с параметрами `google_application_credentials` для работы с DialogFlow

### Установка зависимостей

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/Rokyl59/bot_helper.git
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

### Обучение нейросети


Перед первым запуском необходимо обучить нейросеть:

```bash
python teach_df.py
```

### Запуск бота
Для запуска Telegram-бота выполните:

```bash
python tg_bot.py
```

Для запуска VK-бота выполните:

```bash
python3 vk_bot.py
```

### DialogFlow

- Для получения `project_id` необходимо создать проект [DialogFlow](https://cloud.google.com/dialogflow/es/docs/quick/setup).
- Необходимо создать [агента DialogFlow](https://cloud.google.com/dialogflow/es/docs/quick/build-agent).
- Для получения файла-json с параметрами google_application_credentials необходимо:
  - установить [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
  - выполнить [авторизацию](https://cloud.google.com/docs/authentication/provide-credentials-adc) c использованием Google Cloud CLI


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, 
создайте файл `.env` в корневой директории проекта и запишите туда данные в таком 
формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:

- `TOKEN_TG` - Ваш API-ключ для работы с Telegram-ботом
- `DF_PROJECT_ID` - Ваш ID проекта DialogFlow
- `TOKEN_VK` - Ваш API-ключ для работы с VK-ботом
- `GOOGLE_APPLICATION_CREDENTIALS` - путь к файлу `credentials`


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).