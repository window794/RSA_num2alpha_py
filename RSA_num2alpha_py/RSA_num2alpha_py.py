# 数値→アルファベット
import re
def num2alpha(M):
    if len(str(M)) % 2 != 0:
        msg = ("数値：" + str(M) + "の値が偶数桁でなかったので、この関数を動かせません")
        return msg
    else:
        words = ""
        list = re.split('(..)',str(M))[1::2]
        for i in range(len(list)):
            words += chr(64+int(list[i]))
        return words

p=37 
q=71 
e=79
c=904
n=p*q 
print("n=:",n) 
for i in range(e): 
    if i*(p-1)*(q-1) % e == e-1: 
        m=i  
        print("m=:",m) 
        break 
d=(m*(p-1)*(q-1)+1)//e
print("d=:",d)
M=(c**d)%n
print("M=:",M)
print("出力結果:",num2alpha(M))
