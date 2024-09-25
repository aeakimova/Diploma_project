## Анна Акимова, 21-я когорта — Финальный проект. Инженер по тестированию плюс

from sender_stand_request import track_number, get_order

# Тест 1. Успешное получение заказа по трек-номеру
def test_get_order_by_track():
    # В переменную get_order_response сохраняется тело ответа на вызов функции get_order
    # (получение заказа по сохраненному трек-номеру)
    get_order_response = get_order(track_number)
    # Проверяется, что код ответа равен 200
    assert get_order_response.status_code == 200