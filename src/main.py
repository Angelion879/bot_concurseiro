"""Main function file"""
import os
import time
import requests

def get_todays_date():
    """returns the current date on a YYYY.MM.DD format"""

    date = str(time.localtime().tm_year), str(time.localtime().tm_mon), str(time.localtime().tm_mday)
    current_date = ".".join(date)

    return current_date

def ntfy_message_sender(message):
    try:
        CHAN = os.environ["SECRET_CHANNEL"]
    except KeyError:
        from keys import channel
        CHAN = channel

    requests.post(f"https://{CHAN}",
        data=f"{message}",
        headers={
            "Title": "Concursos Atualizados!",
            "Tags": "memo",
        }, timeout=10)

if __name__ == '__main__':
    print('aaa')
