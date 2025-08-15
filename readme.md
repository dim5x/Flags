## Тестовое веб-приложение-викторина на Flask, которое показывает случайный флаг, предлагая угадать, какой стране он принадлежит.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/be6e0b233eaf4c4a945c93f142e1cf8a)](https://app.codacy.com/gh/dim5x/Flags/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

### Требования:

- Python 3.7+
- Flask

### Структура проекта:

```
    Flags/
    ├── flags.py             # Основной скрипт приложения
    ├── data.py              # Список стран.
    └── static/ 
        ├── css/             # Папка со стилями.
        └── images/          # Папка с изображениями флагов (в формате .svg)
    ├── templates/           # Папка с шаблонами.
    └── readme.md            # Этот файл.
```

### Установка:

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/dim5x/Flags
    cd Flags
    ```

2. Установка зависимостей:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустите приложение:

   ```bash
   python app.py
   ```

4. Откройте в браузере:

   ```
   http://127.0.0.1:5000/
   ```

### Технические детали:

- Использует Flask для веб-интерфейса.

- Флаги хранятся в формате `SVG` (масштабируемая векторная графика).

- Случайный флаг выбирается через `secrets.randbelow()` (криптографически безопасный метод).

- Секретный ключ Flask генерируется автоматически через `token_hex(16)`.