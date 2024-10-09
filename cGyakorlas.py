import math



def harom():
    # 1. megoldás
    for i in range(0,21,1):
        print(i)

    # 2. megoldás
    for i in range(21):
        print(i)

    #3. megoldás
    for i in range(0,21):
        print(i)

    #4.megoldás
    i = 0
    while i<21:
        print(i)
        i+=1
def negy():
    for i in range(20,57,2):
        print(i)

def ot():
    for i in range(77,-77,-4):
        print(i)

def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot!"))
    return szam

def hat():
    #6.	Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

    szam1 = beolvas()
    szam2 = beolvas()

    # melyik a nagyobb
    if szam2 < szam1:
        # csere
        atmenet = szam1
        szam1=szam2
        szam2 = atmenet

    for i in range(szam1, szam2+1, 1):
        print(i, end=" ")


def het():
    #7.	Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat<0:
        for i in range(0, szorzat-1,-1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat+1,1):
            print(i, end=" ")
def nyolc():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2
    if szorzat < 0:
        i = 0
        while i<szorzat-1:
            print(i, end=" ")
            i -= 1
            # i=i-1 ugyanaz
    else:
        i = 0
        while i < szorzat+1:
            print(i, end=" ")
            i += 1

def kilenc():
    for i in range(1,8):
        print(i, end=",")
        if i==7:
            print(i, end=" ")
            #print(str+(i))+",", end=" ")
def kilencA():
    for i in range(0, 8, 1):
        #print(str(i)+",", end = " ")
        print(", "+str(i), end=" ")


def beolvas2():
    szam=float(input("Kérem adjon meg egy valós számot!"))
    return szam
def tizenegy():
    x=beolvas2()
    y=beolvas2()

    eredmeny=3*x+pow(y,2)
    print("3*x"+str(x)+"+"+str(y)+"^2="+str(eredmeny))

def tizenketto():
    x = beolvas2()
    y = beolvas2()
    db = 0
    for szam in range(math.ceil(x), round(y)+1, 1):
        #print(szam)
        if szam%2 == 0:
            db += 1
            print("A páros számok száma: "+str(db)+"db.")



