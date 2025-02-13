import os

from dotenv import load_dotenv

load_dotenv()


def main():
    from gigachat.chat import get_giga_chat_answer
    while True:
        q = input("Тема: ")
        print(
            get_giga_chat_answer(
                q,
                "Напиши яркий телеграмм пост на эту тему, по возможности используй смайлики пожалуйста",
                os.getenv("AUTHORIZATION_SB_CODE")
            )
        )
        print()


if __name__ == "__main__":
    main()