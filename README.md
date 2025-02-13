# giga_chat
Пакет для связи с gigachat от Сбера
# Как использовать
Установите зависимости
```commandline
pip install requests cachetools pydantic-settings
```
Импортируйте в свой код
```python
from gigachat.chat import get_giga_chat_answer

# функция возвращающая ответ от gigachat
get_giga_chat_answer(
    "Вопрос к Чату",
    "Контекст вопроса",
    "Код авторизации Сбера"
)

```
