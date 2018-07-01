Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("""*********************************
ATM MAKİNESİNE HOŞGELDİNİZ .. 

İŞLEMLER ;
1 . BAKİYE SORGULAMA 

2 . PARA YATIRMA

3 . PARA ÇEKME

4. KART İADE 
*********************************""" )
bakiye = 1000

while True:


    işlem = input("İşlemi seçiniz : ")
    if (işlem == '4' ):
            print("Kartınız çıkarılıyor..")



    elif işlem == '1':
        print("Bakiyeniz gösteriliyor...")
        print("Bakiyeniz :",bakiye)
        x = input("Fişe basılmasını ister misini ?(N/Y) :")
        if x == 'N' or x == 'n':
            print("Tekrar bekleriz...")
            break

        elif x == 'Y' or x == 'y':
            print("Fişiniz basılıyor...")
            k = input("Başka bir işlem yapmak ister misiniz ? (N/Y):")
            if k == 'Y' or k == 'y':
                print("Ana ekrana geçiliyor...")
                continue

            else:
                print("Tekrar bekleriz")
                print("Kartınız çıkartılıyor..")

                break




    elif işlem == '2':
        yatırma = int(input("Yatırmak istediğiniz tutarı giriniz : "))
        print("Paranız yatırılıyor..")
        bakiye += yatırma
        print("Paranız yatırıldı.")
        print("Yeni Bakiyeniz : ",bakiye)
        b =input("Fiş ister misiniz ? (N/Y) : ")
        if b == 'Y' or b=='y':
            print("Fişiniz basılıyor")
            j = input("Başka bir işlem yapmak ister misiniz ? N/Y : ")
            if j == 'Y' or j == 'y':
                print("Ana eknara geçiliyor..")
            else:
                print("Tekrar bekleriz..")
                print("Kartınız çıkartılıyor..")
                break
        else:
            print("Tekrar bekleriz")

            break





    elif işlem == '3' :
        cekme = int(input("Çekmek istediğiniz tutarı giriniz : "))
        if bakiye < cekme:
            print("Bakiyeniz yetersiz")
            m =input("Başka işlema yapmak ister misiniz ? N/Y :")
            if m == 'y' or m == 'Y':
                print("Ana ekrana geçiliyor..")
                continue
            else:
                print("Tekrar bekleriz..")
                print("Kartınız çıkartılıyor..")
                break


        elif  bakiye - cekme >=0:

            print("Paranız çekiliyor..")
            bakiye -= cekme
            print("Yeni Bakiyeniz : ",bakiye)
            p = input("Fiş ister misiniz ? N/Y :")
            if p == 'y' or p == 'Y':
                print("Fişiniz basılıyor..")
               

            else:
                print("Kartını çıkartılıyor..")

            o=input("Başka bir işlem yapmak ister misiniz ? N/Y : ")
            if o == 'y' or o == 'Y':
                    print("Ana ekrana geçiliyor..")
                    continue
            else:
                print("Kartınız çıkartılıyor..")
                print("Tekrar bekleriz")
                break
        break


    else:
        print("Geçersiz işlem")
        break

