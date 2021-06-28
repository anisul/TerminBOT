import time
import requests


def core():
    if is_termin_available() is True:
        telegram_bot_sendtext("TERMIN FOUND at: https://termin.dachau-med.de/impfung/")
    else:
        print("Termin not found")


def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def do_request():
    url = 'https://termin.dachau-med.de/impfung/wp-admin/admin-ajax.php?lang=de'
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {
        'sln[shop]': '16066',
        'sln_step_page': 'shop',
        'submit_shop': 'next',
        'action': 'salon',
        'method': 'salonStep',
        'security': '21cc502236'
    }

    session = requests.Session()
    response = session.post(url=url, headers=headers, data=payload)
    return response.json()['content']


def is_termin_available():
    if "Keine freien Termine" not in do_request():
        return True
    else:
        return False


while True:
    core()
    time.sleep(5)
