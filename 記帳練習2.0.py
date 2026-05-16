#x= 收入
#y= 支出
#z= 储蓄
Z = 0 
print("你目前存款為:", Z)
while True:
    try:
        x= int(input("請輸入收入:"))
        break
    except ValueError:
        print("請輸入數字")
while True:
    try:
        y= int(input("請輸入支出:"))
        break
    except ValueError:
        print("請輸入數字")
Z = Z + x - y
print("你目前存款為:", Z)
if Z < 0:
    print("你已經負債了")
input("按Enter鍵結束")  