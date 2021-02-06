from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

def get_soup(url):
    """
    url에 대한 request를 요청하고 soup객체를 반환한다.
    :param url:
    :return: soup 객체
    """
    req = Request(
        url,
        data=None,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/html"
        }
    )
    source = urlopen(req)
    soup = BeautifulSoup(source, 'lxml')
    return soup

def all_seats():
    base_url = 'http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no='
    number = ['1', '2', '3']
    urllist = [base_url + i for i in number]
    count = 1

    all_lib = [get_soup(url) for url in urllist]

    all_seats = {}
    for lib in all_lib:
        # maptemp 아래 소속되어있는 모든 자리 자료를 리스트로 얻는다.
        bs_seats = lib.select('#maptemp > *')
        seats = []
        for seat in bs_seats:
            if seat['id'].startswith('Layer'):
                id_num = int(re.findall('Layer([0-9]+)', seat['id'])[0])
                id_color = seat.select('td')[0]['bgcolor']
                if id_color == 'red':
                    is_full = 1
                else:
                    is_full = 0
                seats.append({id_num: is_full})
        all_seats[count] = seats
        count += 1
    return all_seats

print(all_seats())
