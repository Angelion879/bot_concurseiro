"""Main function file"""
import os
import requests
import page_flipper as pf
import scrapper as s

def build_news_lists():
    """builts the message to send through ntfy"""
    court_content = []
    police_content = []

    available_pages = pf.create_page_link_list()

    for url in available_pages:
        j_array = s.get_json_content(url)
        for json_dict in s.json_array_handler(j_array):
            t = s.filter_through_content(json_dict,'Tribunal')
            if t:
                court_content.append(t)
            p = s.filter_through_content(json_dict,'Polícia')
            if p:
                police_content.append(p)

    return court_content, police_content

def message_builder():
    """builds the str for the ntfy message"""
    court_news, police_news = build_news_lists()

    message_part1 = 'TRIBUNAIS:\n'+('\n\n '.join(str('\n - '.join(str(j)for j in i)) for i in court_news))
    message_part2 = 'POLICIAIS:\n'+('\n\n '.join(str('\n - '.join(str(j)for j in i)) for i in police_news))

    return message_part1+"\n\n"+message_part2

def ntfy_message_sender(message):
    try:
        CHAN = os.environ["SECRET_CHANNEL"]
    except KeyError:
        from keys import channel
        CHAN = channel

    requests.post(f"https://{CHAN}",
        data=f"{message}",
        headers={
            "Title": "Editais do dia",
            "Tags": "memo",
        }, timeout=10)

if __name__ == '__main__':
    news = message_builder()
    print(news)

    ntfy_message_sender(news)
