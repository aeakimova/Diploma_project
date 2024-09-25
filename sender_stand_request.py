import configuration
import data
import requests

# Функция для создания нового заказа
def post_new_order(body):
    # Выполнение POST-запроса с использованием URL сайта из конфигурационного файла, эндпоинта создания заказа и тела запроса
    return requests.post(url = configuration.URL_SERVICE + configuration.CREATE_ODER, json = body)
# Вызов функции post_new_order с телом запроса из модуля data для сохранения трек-номера заказа в переменную track_number
track_number = post_new_order(data.order_body).json()['track']
# Вывод трек-номера заказа
#print(track_number)

# Функция для создания запроса на получения заказа по треку заказа
def get_order(track):
    # Выполнение GET-запроса с использованием URL сайта из конфигурационного файла, эндпоинта получения заказа по трек-номеру
    # и преобразованного в строку значения трек-номера
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_NUMBER + str(track))
# Вызов функции get_order
# response = get_order(track_number)
# Вывод тела ответа на запрос
#print(response.json())
# Вывод HTTP-статус кода ответа на запрос
#print(response.status_code)