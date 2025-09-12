"""Generates all numbers for available pages, and re-builds the url to flip through the pages"""

def page_flipper(max_page_number):
    for i in range(max_page_number+1):
        yield i

def url_string_builder(page_number):
    url = f'''https://www.in.gov.br/consulta/-/buscar/dou?q="Concurso+público"&s=todos
    &exactDate=dia&sortType=0&delta=20&currentPage=5&
    newPage={page_number}&score=0&id=654946296&displayDate=1757646000000'''

    return url

if __name__ == '__main__':
    pass
