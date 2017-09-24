from bs4 import BeautifulSoup
import urllib.request as req
from mojimoji import zen_to_han
import datetime
import re
import config
import sender


def main():
    j = 0
    even = False
    change = False
    date_li = []
    days_li = []
    class_li = []
    change_li = []
    send_li = []
    day = datetime.datetime.today()
    + datetime.timedelta(1)
    today = day.strftime('%-m月%-d日')

    res = req.urlopen(config.get_url())
    soup = BeautifulSoup(res, 'html.parser')
    changes = soup.select('table:nth-of-type(10) > tr[height="35"] > td')

    for li in changes:
        if even is False:
            cut = li.string
            date_li.append(cut.lstrip())
            even = True
        elif even is True:
            cut = li.string
            change_li.append(cut.lstrip())
            even = False

    for x in date_li:
        days_li.append(re.findall(
            '(\d{1,2}月\d{1,2}日)\(([月火水木金])\) ([１２３４５６７８])',
            x
            ))
    for x in change_li:
        class_li.append(re.findall('.+　→　(.+)', x))

    # today = '10月3日'
    # days_li.append([('10月3日', '火', '８')])
    # print(days_li)
    # class_li.append(['ぎゃぎゃ'])
    # print(class_li)
    for x in days_li:
        time = x[0]
        if x[0][0] == today:
            change = True

            if '月' == time[1]:
                config.mon.change_class(
                        int(zen_to_han(time[2])),
                        class_li[j][0]
                        )
                send_li = config.mon.classes
            elif '火' == time[1]:
                config.tue.change_class(
                        int(zen_to_han(time[2])),
                        class_li[j][0]
                        )
                send_li = config.tue.classes
            elif '水' == time[1]:
                config.wed.change_class(
                        int(zen_to_han(time[2])),
                        class_li[j][0]
                        )
                send_li = config.wed.classes
            elif '木' == time[1]:
                config.thu.change_class(
                        int(zen_to_han(time[2])),
                        class_li[j][0]
                        )
                send_li = config.thu.classes
            elif '金' == time[1]:
                config.fri.change_class(
                        int(zen_to_han(time[2])),
                        class_li[j][0]
                        )
                send_li = config.fri.classes
            # print(send_li)
        else:
            # print('Not match.')
            if '月' == time[1]:
                send_li = config.mon.classes
            elif '火' == time[1]:
                send_li = config.tue.classes
            elif '水' == time[1]:
                send_li = config.wed.classes
            elif '木' == time[1]:
                send_li = config.thu.classes
            elif '金' == time[1]:
                send_li = config.fri.classes
        j += 1

    message = sender.text_gen(
            send_li,
            change,
            today,
            config.get_url()[-2:]
            )
    # print(message)
    sender.sender(message)


main()
