# akinatorpy2 by iamquietw (with self-educating)

from config import questions, objects_db
import sqlite3

cursor = objects_db.cursor()
cursor.execute("SELECT * from objects")
objects = cursor.fetchall()

answers = []
current_question = 0
while len(answers) != len(questions):
    question_answer = input(f"{questions[str(current_question)]} >> ")
    current_question = current_question + 1
    answers.append(int(question_answer))
answer = ""
for item in objects:
    matches = 0
    for i in range(len(questions)):
        if answers[i] == item[i+1]:
            matches = matches + 1
    if matches == len(questions):
        answer = str(item[0])

if int(input(f'Ответ - {answer}? >> ')) == 0:
    name = input("Правильный ответ >> ")
    cursor.execute(f'INSERT INTO objects VALUES("{name}", {answers[0]}, {answers[1]}, {answers[2]}, {answers[3]}, {answers[4]});')
    objects_db.commit()
