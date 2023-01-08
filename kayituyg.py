################# kullanici kayit uygulamasi #################
import json
import time
import os
class kullanici():
    def __init__(self,isim="s",soyisim="s",yas=0):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
    def add_user(self):#kullanıcı ekleme kısmı
        os.system("cls")
        print("kullanıcı ekleme sayfasındasınız\n".upper())
        denek = False 
        self.isim = input('kullanici isimi nedir = ')
        self.soyisim = input('kullanici soyisimi nedir = ')
        while denek == False:#kullanici yaş bölümüne str değer girmesin diye kontrol
            try:
                self.yas = int(input("kullanici yasi nedir = "))
                denek = True
            except:
                denek = False
        sozluk = {'isim':self.isim,'soyisim':self.soyisim,'yas':self.yas,'numara':0} 
        try:#daha önce veri kaydedilmiş mi
            with open("bilgiler.json","r") as dosya:
                data = json.load(dosya)
            with open("bilgiler.json","r") as dosya:
                data2 = json.load(dosya)    
            a = 0
            a += len(data[0]["kullanicilar"])+1 #kullanıcı numarasını ayarladığımız kısım
            sozluk.update({"numara":a})#kullanıcıya numara değerini verdiğimiz kısım
            print("kullanici numarasi = [{}]".format(a))
            data[0]["kullanicilar"].append(sozluk)#tekrar dosyaya yazdıracağımız için yeni kullanıcıyı eklediğimiz kısım
            for u in data2[0]["kullanicilar"]:#kullanıcının içeride mevcut olup olmadığının kontrolü    
                isim = u["isim"] == sozluk["isim"]
                soyisim = u["soyisim"] == sozluk["soyisim"]
                yas = u["yas"] == sozluk['yas']
                if isim == True and soyisim == True and yas == True:
                    print("bu kullanici zaten mevcut olduğu için eklenmedi")   
                    data[0]["kullanicilar"].pop()
                # if isim == False or soyisim == False or yas == False: 
            with open('bilgiler.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)#en sonki değeri yazdırdığımız kısım
        except:#daha önce kaydedilmiş veri yoksa
            sozluk.update({"numara":1})
            my_dict = {"kullanicilar":[sozluk]}
            with open('bilgiler.json', 'w', encoding='utf-8') as f:
                json.dump([my_dict], f, ensure_ascii=False, indent=4) 
            print("ilk kullanici olusturuldu \nkullanici numarasi = [1]")
    def find_user(self):#veriler içinden kullanıcı bulma
        os.system("cls")
        print("kullanici arama ekranindasiniz\n".upper())
        try:
            with open("bilgiler.json","r") as dosya:
                data = json.load(dosya)
            girdi = int(input("lütfen kullanıcının numarasını yazın = "))
            for u in data[0]["kullanicilar"][girdi-1]:#kullanıcı bilgilerini sıralattığımız kısım
                print("{} --> {}".format(u,data[0]["kullanicilar"][girdi-1][u]))
        except:
            print("oluşturulmuş bir kullanıcı yok".upper())
    def change_user(self):#belirlenen kullanıcı üstünde değişiklik yapma
        os.system("cls")
        print("kullanici degistirme ekranindasiniz\n".upper())
        try:
            with open("bilgiler.json","r") as dosya:
                data = json.load(dosya)
            girdi = int(input("lütfen değiştirmek istediğiniz kullanıcının numarasını yazın = "))
            datalar = data[0]["kullanicilar"][girdi-1]
            print(datalar)
            print("Lütfen hangi öğeyi değiştirmek istediğinizi yazın ")
            degistir = input()
            yenioge = input(f"yeni {degistir} ne olsun = ")
            if degistir == "yas":
                yenioge = int(yenioge)
            data[0]["kullanicilar"][girdi-1][degistir] = yenioge
            with open('bilgiler.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except:
            print("oluşturulmuş kullanıcı yok".upper()) 
    def delete_user(self):
        os.system("cls")
        print("kullanici silme ekranindasin\n".upper())
        try:
            with open("bilgiler.json","r") as dosya:
                data = json.load(dosya)
                sil = int(input("lütfen silmek istediğiniz kullanıcının numarasını yazın = "))
            b = sil - 1
            #data[0]["kullanicilar"][girdi-1]
            data[0]["kullanicilar"].remove(data[0]["kullanicilar"][b])
            for i in range(len(data[0]["kullanicilar"])-sil+1):
                data[0]["kullanicilar"][b]["numara"] -= 1
                b+=1
            with open('bilgiler.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("kullanici silindi")
        except:
            print("oluşturulmuş kullanıcı yok".upper())
def board():

    liste = ["kullanıcı ekle","kullanıcı ara","kullanıcı bilgisi değiştir","kullanıcı sil",
    "çıkış"]
    i = 1
    os.system("cls")
    print("********************")
    for u in liste:
        print(f"[{i}] {u}")
        i+=1
    print("********************")
def exitt():
    exit()      
board()
while True:
    haci = False
    while haci == False:
        try:
            giris = int(input("yapmak istediğiz işlem nedir = "))
            haci = True
        except:
            haci = False
    if giris == 1:
        kullanici().add_user()
        time.sleep(3)
        board()
    if giris == 2:
        kullanici().find_user()
        input("geçmek için (enter)")
        board()
    if giris == 3:
        kullanici().change_user()
        time.sleep(3)
        board()
    if giris == 4:
        kullanici().delete_user()
        time.sleep(3)
        board()
    if giris == 5:
        exitt()