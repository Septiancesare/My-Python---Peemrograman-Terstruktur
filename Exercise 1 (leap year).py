year = int(input("mau tahun berapa?"))
if year%400 == 0:
    print ("tahun itu merupakan tahun kabisat")
elif year%100 == 0:
    print ("tahun itu bukan merupakan tahun kabisat")
elif year%4 == 0:
    print ("tahun itu merupakan tahun kabisat")
else:
    print ("tahun itu bukan merupakan tahun kabisat")
