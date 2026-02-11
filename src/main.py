"""Main function file"""
import time
from src import scrap, messenger

STORAGE = "Last_update.txt"
AREA = "PC"
ROLE = "Perito Criminal"

def get_todays_date():
    """returns the current date on a YYYY.MM.DD format"""

    date = str(time.localtime().tm_year), str(time.localtime().tm_mon), str(time.localtime().tm_mday)
    current_date = ".".join(date)

    return current_date

def there_is_new_content(stored, new_content):
    """compares the latest saved content to the currently in hand, 
    returns true if there's something new, and false if not"""

    with open(stored, "r", encoding='utf-8') as file:
        og_content = file.read()

        for i in new_content:
            if str(i) not in og_content:
                return True
        file.close()
    return False

def update_doc_with_tenders_info(stored, filtered_content):
    """updates the document with the daily date and tenders contents"""

    today_date = get_todays_date()
    with open(stored, "w", encoding='utf-8') as file:
        file.write(today_date)
        file.write("\n\n")

        for i in filtered_content:
            file.write(str(i) + "\n")

if __name__ == '__main__':
    # link it all together
    daily_content = scrap.scrapper(AREA, ROLE)
    if there_is_new_content(STORAGE, daily_content):
        messenger.ntfy_message_sender(daily_content)

    update_doc_with_tenders_info(STORAGE, daily_content)
    print('done!')
