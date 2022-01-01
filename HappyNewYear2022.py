"""アスキーアートを用いた年賀状？みたいなもの作ってみた
干支とおみくじを表示
"""

import pyfiglet
import random
import datetime

#西暦→干支
def Year_to_Eto(year: int) -> str:
    etoList = ["🐭 子", "🐮 丑", "🐯 寅", "🐰 卯", "🐲 辰", "🐍 巳",
               "🐴 午", "🐏 羊", "🐵 申", "🐔 酉", "🐶 戌", "🐗 亥"]
    index = (year+8) % 12
    return etoList[index]

#おみくじを引く
def Omikuzi() -> str:
    returnList = ["大吉", "吉", "中吉", "小吉", "末吉", "凶", "大凶"]
    rand = random.randint(0,6)
    return returnList[rand]

todayDate = datetime.datetime.today()  #今日の日付
if todayDate.month == 12:
    print("まだ新年明けてない")
    exit()
    
elif not(todayDate.month == 1 and todayDate.day==1):
    print("元日じゃないよ")
    exit()

#明けましておめでとう
print(pyfiglet.figlet_format('Happy New Year'))
print(pyfiglet.figlet_format("                       "+str(todayDate.year)))

#干支を表示
print("今年は "+Year_to_Eto(todayDate.year)+" 年です。")

#おみくじを引く
print("おみくじを引きます,,, "+Omikuzi()+" でした！")