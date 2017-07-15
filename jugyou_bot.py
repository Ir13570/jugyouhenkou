import urllib.request
from bs4 import BeautifulSoup
import re
import datetime
import mojimoji
import requests

#スクレイピング------------------------------------------------------------------------------

#url定義 ※2は持ち物連絡ページを参照しており、無印は授業変更ページを参照しています。
url     = 'http://jyugyou.tomakomai-ct.ac.jp/jyugyou.php?class=J2' 
url2    = 'https://writening.net/page?NVznd8'
#URLOPEN&HTML取得
html    = urllib.request.urlopen(url).read()
soup    = BeautifulSoup(html)
html2   = urllib.request.urlopen(url2).read()
soup2   = BeautifulSoup(html2)

#変更情報切り抜き
soup_sc = soup.find_all("table", width="55%", border="1", cellspacing="0", cellpadding="0", bgcolor="#FFFFFF")
soup2_sc = soup2.find_all("div", class_="section-item")

#文字列化
soup_str    = str(soup_sc)
soup2_str   = str(soup2_sc)

#要素抜き出し
htmlp       = re.compile(r"<[^>]*?>")
soup_str    = htmlp.sub("", soup_str)
soup_str    = soup_str[15:-1] + "　"
soup2_str   = htmlp.sub("", soup2_str)
soup2_str   = soup2_str[10:-5]

#soup_str = "7月6日(火) ５・６時限目　プログラミングⅠ　→　論理回路Ⅰ　7月16日(木) １・２時限目　論理回路Ⅰ　→　プログラミングⅠ　7月6日(金) ３時限目　プログラミングⅠ　→　論理回路Ⅰ　"

#情報リスト化
pattern         = r"(1?[0-9])月([1-3]?[0-9])日"
day_list        = re.findall(pattern, soup_str)
pattern         = r"\(([月火水木金])\)"
weekday_list    = re.findall(pattern, soup_str)
pattern         = r"(?:([１２３４５６７８]?)・?([１２３４５６７８])時限目)"
classtime_list  = re.findall(pattern, soup_str)
pattern         = r"　.{2,8}　→　(.{2,8})　"
class_list      = re.findall(pattern, soup_str)

#出力テスト
print("変更情報原文:" + soup_str)
print("変更月日一覧:" + str(day_list))
print("変更曜日一覧:" + str(weekday_list))
print("変更時間一覧:" + str(classtime_list))
print("変更後授業名一覧:" + str(class_list))
#日付情報・授業データ編集-----------------------------------------------------------------------------------

#日付取得
today   = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%-m/%-d")
weekday = (datetime.date.today() + datetime.timedelta(days=1)).weekday()

#曜日日本語化
if weekday == 0:
    weekday_str = "月曜日"
elif weekday == 1:
    weekday_str = "火曜日"
elif weekday == 2:
    weekday_str = "水曜日"
elif weekday == 3:
    weekday_str = "木曜日"
elif weekday == 4:
    weekday_str = "金曜日"
elif weekday == 5:
    weekday_str = "土曜日"
elif weekday == 6:
    weekday_str = "日曜日"

#標準時間割定義
classes  = [["物理Ⅰ", "物理Ⅰ", "英語ⅡA ", "英語ⅡA ", "倫理・社会", "倫理・社会", "国語Ⅱ"], ["体育Ⅱ", "体育Ⅱ", "英語ⅡB", "英語ⅡB", "プログラミングⅠ", "プログラミングⅠ", "H.R."], ["創造工学Ⅱ", "創造工学Ⅱ", "数学ⅡA", "数学ⅡA", "工学実験Ⅰ", "工学実験Ⅰ", "工学実験Ⅰ"], ["論理回路Ⅰ", "論理回路Ⅰ", "英語ⅡA", "数学ⅡB", "国語Ⅱ", "国語Ⅱ", "数学ⅡA"], ["化学Ⅱ", "化学Ⅱ", "歴史", "歴史", "数学ⅡB", "数学ⅡB"], ["土曜日です。サーバーの実行曜日設定にミスがあります。石川は修正してください。"], ["日曜です。実行設定にミスがあります。石川を呼んでください。"]]

#出力テスト
#print(today)
#print(weekday)
#print(classes[weekday])
print("処理対象月日")
print("\n変更処理前<0>:" + str(classes[weekday]))
j       = 0
c       = 0
change  = 0
for i in day_list:
    
    if "/".join(i) == today:
        #print("TODAY!!")

        #classtime_list参照
        if weekday == 5 or 6:
            print("週末ですよ")
        elif classtime_list[j][0] == "":

            c += 1
            #print(classtime_list[j][1])
            print("/".join(i) + "日に該当、処理開始")
            ct                      = int(mojimoji.zen_to_han(classtime_list[j][1])) - 1
            classes[weekday][ct]    = class_list[j]
            change                  = 1
            print(str(c) + "次変更処理<1>:" + str(classes[weekday]))

        else:

            c += 1
            print("/".join(i) + "日に該当、処理開始")
            #print(classtime_list[j][0])
            ct  = int(mojimoji.zen_to_han(classtime_list[j][0])) - 1
            classes[weekday][ct] = class_list[j]
            
            #iprint(classtime_list[j][1])
            ct                      = int(mojimoji.zen_to_han(classtime_list[j][1])) - 1
            classes[weekday][ct]    = class_list[j]
            change                  = 1
            print(str(c) + "次変更処理<2>:" + str(classes[weekday]))

    else:
        print("/".join(i) + "日ではない")
    j += 1

#外部送信---------------------------------------------------------------

#送信先URL（Line Notify）
url     = "https://notify-api.line.me/api/notify"
#送信用トークン
<<<<<<< HEAD
token   = "***" 
headers = {"Authorization" : "Bearer "+ token}

#変更判定出力
if change == 1:
        change_str  = "<授業変更あり>"
elif change == 0:
        change_str  = "<授業変更なし>"
else:
        change_str  = "原因不明の例外です。石川はさっさと確認を行ってください。"

#メッセージ作成
message = "\n" + today + weekday_str + change_str + "\nどうも、授業変更通知botです。\n明日の時間割は以下の通りです。"

i = 1
for s in classes[weekday]:
    message = message + "\n " + str(i) + ":"  + s
    i += 1

message = message + "\n【持ち物・課題・連絡等】\n" + soup2_str
payload = {"message" :  message}

#持ち物出力
print("持ち物内容:" + soup2_str)

#メッセージ送信
r = requests.post(url ,headers = headers ,params=payload)
