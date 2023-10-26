import math
import random

def basit():
    x = random.randint(5, 10)
    y = random.randint(1, 5)
    opr=['+','-','*','/']
    o=random.choice(opr)
    if o == '+':
        sonuc =(x + y)
    if o == '-':
        sonuc =(x - y)
    if o == '*':
            sonuc = (x * y)
    if o == '/':
        print("DİKKAT!!! Tam bölünmeyen işlemlerde yazacağın cevabı doğru sonucun bir alt tam sayısı şeklinde girmelisin.")
        sonuc= int(x / y)


    print(x, o, y ,"= ?")
    cvp= int(input())
    if cvp == sonuc:
        print("Doğru cevap :)")
    else:
        print("Yanlış cevap!! Sonucu doğru girdiğine emin ol işte cevap : ")
        print(sonuc)

def orta():
    x = random.randint(10, 100)
    y = random.randint(10, 100)
    opr = ['+', '-', '*', '/']
    o = random.choice(opr)
    if o == '+':
        sonuc = (x + y)
    if o == '-':
        sonuc = (x - y)
    if o == '*':
        sonuc = (x * y)
    if o == '/':
        print("DİKKAT!!! Tam bölünmeyen işlemlerde yazacağın cevabı doğru sonucun bir alt tam sayısı şeklinde girmelisin.")
        sonuc = int(x / y)

    print(x, o, y, "= ?")
    cvp = int(input())
    if cvp == sonuc:
        print("Doğru cevap :)")
    else:
            print("Yanlış cevap!! Sonucu doğru girdiğine emin ol işte cevap : ")
            print(sonuc)


def zor():
    x = random.randint(10, 100)
    y = random.randint(10, 100)
    z = random.randint(10, 100)
    opr = ['+', '-', '*', '/']
    o = random.choice(opr)
    if o == '+':
        sonuc = (x + y + z)
    if o == '-':
        sonuc = (x - y - z)
    if o == '*':
        sonuc = (x * y * z)
    if o == '/':
        print("DİKKAT!!! Tam bölünmeyen işlemlerde yazacağın cevabı doğru sonucun bir alt tam sayısı şeklinde girmelisin.")
        sonuc = int(x / y)

    print(x, o, y, o,  z, "= ?")
    cvp = int(input())
    if cvp == sonuc:
        print("Doğru cevap :)")
    else:
        print("Yanlış cevap!! Sonucu doğru girdiğine emin ol işte cevap : ")
        print(sonuc)
try:
    print("İlk önce basit işlemlerle başlayalım")
    basit()
    print("4 tanede orta seviye bir işlem çözelim")
    orta()
    orta()
    orta()
    orta()
    print("Şimdi zor seviyedeyiz 3 tane çözelim")
    zor()
    zor()
    zor()
    print("Tebrikler testi bitirdin :)")
except:
    print("HATA!! Sadece sayı girmelisin şimdi baştan başla!!")





