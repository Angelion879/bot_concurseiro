"""Main function file"""
import os
import json
import requests
from bs4 import BeautifulSoup as bs
import page_flipper as pf
import scrapper as s

def build_news_lists():
    """builts the message to send through ntfy"""
    court_content = [["TRIBUNAIS:"]]
    police_content = [["POLICIA:"]]

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

    message_part1 = '\n\n'.join(str('\n - '.join(str(j)for j in i)) for i in court_news)
    message_part2 = '\n\n'.join(str('\n - '.join(str(j)for j in i)) for i in police_news)

    return message_part1+"\n\n"+message_part2

if __name__ == '__main__':
    print(message_builder())
