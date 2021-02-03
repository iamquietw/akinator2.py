import sqlite3

questions = {
    "0": "Это живое?",
    "1": "Это жидкость?",
    "2": "Это человек?",
    "3": "Ответ - да?",
    "4": "Ответ - нет?"
}

objects_db = sqlite3.connect("objects.db")
