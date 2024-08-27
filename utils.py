import json
import random
import string
from pathlib import Path

# Путь к файлам
users_file = Path("users.txt")
aliases_file = Path("aliases.json")

# Инициализация файлов при отсутствии
if not users_file.exists():
    users_file.touch()

if not aliases_file.exists():
    aliases_file.write_text(json.dumps({}))

def load_users():
    """Загружает список пользователей из файла."""
    with users_file.open("r") as f:
        users = f.read().splitlines()
        return set(map(int, users)) if users else set()

def add_user(user_id):
    """Добавляет пользователя в файл, если его там еще нет."""
    users = load_users()
    if user_id not in users:
        with users_file.open("a") as f:
            f.write(f"{user_id}\n")

def get_all_users():
    """Возвращает множество всех пользователей."""
    return load_users()

def load_aliases():
    """Загружает словарь псевдонимов из файла."""
    with aliases_file.open("r") as f:
        return json.load(f)

def save_aliases(aliases):
    """Сохраняет словарь псевдонимов в файл."""
    with aliases_file.open("w") as f:
        json.dump(aliases, f)

def generate_alias():
    """Генерирует случайный псевдоним из 8 символов."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def get_or_create_alias(user_id):
    """Получает существующий или создает новый псевдоним для пользователя."""
    aliases = load_aliases()
    if str(user_id) not in aliases:
        alias = generate_alias()
        aliases[str(user_id)] = alias
        save_aliases(aliases)
    return aliases[str(user_id)]
