"""Main function file"""
import os
import requests

def build_news_lists():
    """builts the message to send through ntfy"""
    pass

def message_builder():
    """builds the str for the ntfy message"""
    pass

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
    news = "aaa"
    print(news)

    ntfy_message_sender(news)
