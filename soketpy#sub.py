import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard
import requests


token="xxx" # токен группы в VK
access_token ="xxx" # acces tokenможно получить тут: https://vkhost.github.io/
group_id="xxx" # id/domen группы
v ="5.131" # версия api

py = vk_api.VkApi(token = token)
give = py.get_api()
longpoll = VkLongPoll(py) # получаем longpoll


def msg(id, text):
    py.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0}) # метод отправки



# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      # Чтобы наш бот не слышал и не отвечал на самого себя
       if event.to_me:

        # Для того чтобы бот читал все с маленьких букв 
          message = event.text.lower()
          # Получаем id пользователя
          id = event.user_id
    
          if message == '+': # если человек прописал + то:
            response = requests.get('https://api.vk.com/method/groups.isMember', # обращяемся к groups.isMember
              params = {
              'access_token': access_token,
              'v': v,
              'group_id': group_id,
              'user_id': id
              })
            data = response.json()['response'] # убираем все лишнее
            if data == 1: # если человек подписан то:
              msg(id, 'Вы подписаны!')
            else: # если человек не подписан то:
              msg(id, 'Вы не подписаны!')

          elif message == 'начать': # если человек прописал + то:
              msg(id, 'Привет, напиши + чтобы узнать подписан ли ты или нет.')

          else: # если человек прописал неизвестную команду то:
             msg(id, 'неизвестная команда')