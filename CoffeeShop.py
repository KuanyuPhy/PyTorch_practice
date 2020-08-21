import random
import time
import sys

Kind = input("Coffee or Tea:")
Size = input("輸入你的飲料Size:")

times = 25

if  ( Size in ["M","L","XL"]):
    if(Kind in ["Coffee"]):
        Coffee =["冰本日咖啡","熱本日咖啡","冰咖啡密斯朵","馥列白","濃焦糖那堤"
        ,"雲朵冰搖濃縮咖啡","特選馥郁那堤","冰那堤","冰焦糖瑪朵","冰摩卡","冰美式"]   
        for i in range(times):
            drink = random.shuffle(Coffee)
            if i < times-1:
                print("次數",i+1,"次","抽到的是",Coffee[0])
                time.sleep(0.3)
            else:
                print("今晚，我想來點",Coffee[0],"Size: ",Size)
    elif(Kind in ["Tea"]):
        Tea =["伯爵茶那堤","醇濃抹茶那堤","經典紅茶那堤","冰經典紅茶那堤","玫瑰蜜香茶那堤"
        ,"冰玫瑰蜜香茶那堤","抹茶那堤","冰抹茶那堤","冰抹茶咖啡"]
        for i in range(times):
            drink = random.shuffle(Tea)
            if i < times-1:
                print("次數",i+1,"次","抽到的是",Tea[0])
                time.sleep(0.3)
            else:
                print("今晚，我想來點",Tea[0],"Size: ",Size)
else:    
    print("Error!")
    sys.exit()

