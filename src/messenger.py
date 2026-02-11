"""Message building and sending functions"""
import os
import requests

def message_builder(content):
    """creates message string based on the news list"""

    message_content = []

    for tender in content:
        body = f"## [{tender[0]}]({tender[2]})\n{tender[1]}"
        message_content.append(body)

    message = "\n\n".join(message_content)
    return message

def ntfy_message_sender(news_content):
    """sends message through ntfy"""

    body = message_builder(news_content)
    try:
        CHAN = os.environ["SECRET_CHANNEL"]
    except KeyError:
        from .keys import channel
        CHAN = channel

    requests.post(f"https://{CHAN}",
        data=body.encode('utf-8'),
        headers={
            "Title": "Concursos Atualizados!",
            "Tags": "memo",
            "Markdown": "yes"
        }, timeout=10)

if __name__ == "__main__":
    holder = [['Concurso TJ AL', 'Situação atual: comissão formada', 'https://exemple.com'],
                    ['Concurso TJ PB', 'Situação atual: comissão formada', 'https://exemple.com']]

    # ntfy_message_sender(holder)
    print("done!")
