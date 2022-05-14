import requests
anon = input('Если вы хотите отправлять сообщения без введения имени, напишите "да": ')
if anon == "да" or anon == "Да" or anon == "ДА":
    name = 'Анонимный пользователь'
else:
    name = input('Введите имя: ')

while True:
    text = input('Введите сообщение: ')
    response = requests.post('http://127.0.0.1:5000/send',
                             json={
                                 'name': name,
                                 'text': text
                             }
                            )
