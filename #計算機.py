#計算機 
def hi ():
    print("歡迎使用計算機！")
hi ()
x = float(input("請輸入第一個數字："))
y = float(input("請輸入第二個數字："))  
print("請選擇運算：")
print("1. 加法")
print("2. 減法")
print("3. 乘法")
print("4. 除法")
choice = input("請輸入選項（1/2/3/4）：")
if choice == '1':
    result = x + y
    print("結果：", result)
elif choice == '2':
    result = x - y
    print("結果：", result)
elif choice == '3':
    result = x * y
    print("結果：", result)

    
    print("結果：", result)
else:
    print("無效的選項！")
#筆記
#float()：將輸入的數字轉換為浮點數，以便進行計算。
#input()：用於從用戶獲取輸入。
#if-elif-else：用於根據用戶選擇的運算類型執行相應的計算。   
