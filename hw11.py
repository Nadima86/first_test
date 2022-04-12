price= int(input(""))
om = int(input("Введите размер оперативной памяти:"))
if om >=4 and om<=8:
    print ("ok")
else:
    print("выбирите от 4-8")
hd= int(input("размер жесткого диска:"))
if hd>=1000:
    print ("ok")
else:
    print("выбирите жесткий диск выше 1000 gb")
ssd = int(input("напишите размер ссд:"))
if ssd >=256:
    print("ok")
else:
    print("выбирите выше 256")
