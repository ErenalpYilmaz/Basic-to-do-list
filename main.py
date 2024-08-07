todolist = []

#Listeyi yazdir.
def listele():
    print("TO-DO-LIST :")
    for liste in todolist:
        print(f"{todolist.index(liste)+1}. {liste}")
    print("\n\n")
def add():
    mission = input("Gorevi giriniz : ")
    todolist.append(mission)
    return listele()

def delete():
    deletItem = int(input("Kacinci gorevi silmek istiyorsunuz  : "))
    todolist.pop(deletItem-1)

def islemler():
    print("1-Gorev Listesini Goruntule\n"
          "2-Gorev Ekle\n"
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
                return False
    except:
        print("Hatali islem yapildi.")
        return False

while True :
    islemler()