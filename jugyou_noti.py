import requests

#外部送信---------------------------------------------------------------

#送信先URL（Line Notify）
url     = "https://notify-api.line.me/api/notify"
#送信用トークン
token   = "Ar6en6ug1lb3aHKSXDlzSOgvq2GgfNUGyt2LHdARr5O"
#token = "15TKZejQr0sbBKwzWGCmCE8BLjA0Qi4LLKmv0KyDw9p"
headers = {"Authorization" : "Bearer "+ token}

message = "\n今日もお疲れ様でした。\n次授業日の持ち物・提出物・連絡事項などの記入に協力していただける方がいましたら、以下のURLで開かれるページのテキストを更新してください。(連絡事項がない場合は「なし」と記入していただけるとありがたいです)\npassword:0120\nhttps://writening.net/update?NVznd8"
payload = {"message" :  message}


#メッセージ送信
r = requests.post(url ,headers = headers ,params=payload)
