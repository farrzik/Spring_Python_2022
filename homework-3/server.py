import time

import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': 'Anton',
        'time': 12343,
        'text': 'text01923097'
    })

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/send", methods= ['POST'])
def send_message():
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    # TODO
    # проверить, является ли присланное пользователем правильным json-объектом
    # проверить, есть ли там имя и текст
    # Добавить сообщение в базу данных db
    data = flask.request.json
    if not isinstance(data, dict):
        return abort(400)

    if 'name' not in data or \
        'text' not in data:
        return abort(400)

    if not isinstance(data['name'], str) or \
        not isinstance(data['text'], str) or \
        len(data['name']) == 0 or \
        len(data['text']) == 0:
        return abort(400)

    text = data['text']
    name = data['name']
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    messages_volume = 0
    users = set()
    for message in db:
        messages_volume += 1
        users.add('<li>' + message['name'] + '</li>')
    return "<p><strong>СТАТУС СЕРВЕРА:</strong></p>" \
           "<p>Список пользователей: <ul>{users}</ul></p>" \
           "<p>Всего пользователей: {users_volume}</p>" \
           "<p>Всего сообщений: {messages_volume}</p>".format(
        users_volume=len(users),
        users=''.join(users),
        messages_volume=messages_volume
    )



app.run()
