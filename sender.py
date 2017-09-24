from bs4 import BeautifulSoup
import urllib.request as req
import requests
import re


def text_gen(send_li, change, today, clasname):
    i = 0
    send_str = ''

    send_str += 'クラス:' + clasname + '\n['
    send_str += today + get_weather() + '連絡事項]\n//授業変更情報\n'
    if change:
        send_str += '<授業変更あり>\n'
    else:
        send_str += '<授業変更なし>\n'

    for x in send_li:
        i += 1
        if x != ' ':
            send_str += str(i) + ':' + x + '\n'

    send_str += '\n//連絡事項\n' + get_comment() + '\n'
    return send_str


def get_weather():
    url = (
            'https://weather.goo.ne.jp/'
            'weather/address/01213042/'
            )
    res = req.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    weather = soup.select('p[class="weather"]')
    tommo = weather[1].string
    tommo = tommo.replace('晴れ', '☀')
    tommo = tommo.replace('雨', '☂')
    tommo = tommo.replace('曇り', '☁')
    tommo = tommo.replace('時々', '/')
    tommo = tommo.replace('一時', '|')
    tommo = tommo.replace('のち', '▶')

    return tommo


def get_comment():
    url = 'http://writening.net/page?RUbwCR'
    res = req.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    comment = soup.select_one('div[class="section-item"]')
    p = re.compile(r"<[^>]*?>")
    comment = re.sub(p, "", str(comment)).lstrip().rstrip()
    # print(comment)
    return comment


def sender(message):
    url = "https://notify-api.line.me/api/notify"
    token = "***"
    headers = {"Authorization": "Bearer " + token}
    message = ''
    payload = {"message": message}

    r = requests.post(url, headers = headers, params = payload)
    print(r)
