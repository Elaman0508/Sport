import requests
from django.conf import settings

def send_sms(phone, message, code):
    # Формируем XML-запрос
    new_phone = "".join(filter(str.isdigit, phone))  # Удаляем все нецифровые символы
    xml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
    <message>
        <login>{settings.NIKITA_LOGIN}</login>
        <pwd>{settings.NIKITA_PASSWORD}</pwd>
        <sender>{settings.NIKITA_SENDER}</sender>
        <text>{message} {code}</text>
        <phones>
            <phone>{new_phone}</phone>
        </phones>
    </message>"""

    headers = {"Content-Type": "application/xml"}
    url = "https://smspro.nikita.kg/api/message"

    # Отправляем запрос
    response = requests.post(url, data=xml_data.encode("utf-8"), headers=headers)

    # Обработка ответа
    if response.status_code == 200:
        response_text = response.text
        print(f"SMS отправлено успешно: {response_text}")

        # Проверяем статус ответа от Nikita
        if "<status>2</status>" in response_text:
            print("SMS успешно отправлено.")
            return True
        else:
            print(f"Ошибка в ответе от Nikita: {response_text}")
            return False
    else:
        print(f"Ошибка при отправке SMS: {response.status_code}, {response.text}")
        return False
