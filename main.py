

todolist = []

#Listeyi yazdir.
def listele():
    for liste in todolist:
        print(liste)

def add():
    pass

def delete():
    pass

def islemler():
    print("1-Listeyi Goruntule\n"
          "2-Listeye Ekle\n"
          "3-Gorev Sil\n"
          "4-Cikis")

    secim = int(input("Seciminiz :"))
    try:
        match (secim):
            case 1:
                listele()
            case 2:
                add()
            case 3:
                delete()
            case 4:
                pass
    except:
        print("Hatali islem yapildi.")
