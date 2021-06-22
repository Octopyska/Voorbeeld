import chess
import sys
import time
import os

def printer(print_zin):
    for c in print_zin:
        print(c, end='')
        sys.stdout.flush() #deze regel gevonden op internet
        time.sleep(.02)

def cls(): #functie gevonden op internet om console te clearen
    os.system('cls' if os.name=='nt' else 'clear') 

def keuzechecker1():
    keuze1 = input("Uw keuze: ")
    if keuze1 == "1":
        cls()
        printer('Wilt u met één persoon of met twee personen spelen?')
        printer('\n1. Eén persoon \n2. Twee personen \n3. Ga terug\n\n')
        keuzechecker2() #gaat naar de volgende vraag om te beantwoorden
    elif keuze1 =="2":
        cls()
        printer('Bezoek chess.com eens!\n\nToets \'1\' als u genoeg heeft geoefend!\n')
        keuzechecker3() #gaat naar de volgende vraag om te beantwoorden
    elif keuze1 == "3":
        cls()
        printer('Het was gezellig!\nTot ziens!')
        time.sleep(2) #wacht even af, zodat de persoon het kan lezen
        pass #sluit het programma af
    else:
        #er is iets ingevuld wat niet mogelijk is, hij runt dit segment opnieuw en vraagt daarmee om een nieuwe input
        printer('Dit is niet mogelijk, voer opnieuw een keuze in.')
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        keuzechecker1()

def keuzechecker2():
    keuze2 = input("Uw keuze: ")
    if keuze2 == '1': #1 persoon
        cls()
        printer("Wilt u tegen makkelijk of moeilijk spelen?")
        printer('\n1. Makkelijk \n2. Moeilijk (normaal bord, heel langzaam) \n3. Moeilijk (klein bord, sneller) \n4. Ga terug\n\n')
        keuzechecker4()
    elif keuze2 == '2': #2 personen
        cls()
        chess.spelen(6,chess.bord,chess.pos_koning)
    elif keuze2 == '3': #teruggaan
        mainmenu()
    else:
        #er is iets ingevuld wat niet mogelijk is, hij runt dit segment opnieuw en vraagt daarmee om een nieuwe input
        printer('Dit is niet mogelijk, voer opnieuw een keuze in.')
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        keuzechecker2()

def keuzechecker3():
    keuze3 = input()
    if keuze3=='1':
        mainmenu()
    else:
        #er is iets ingevuld wat niet mogelijk is, hij runt dit segment opnieuw en vraagt daarmee om een nieuwe input
        printer('Dit is niet mogelijk, voer opnieuw een keuze in.')
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        keuzechecker3()

def keuzechecker4():
    keuze4 = input("Uw keuze: ")
    if keuze4 == '1': #makkelijker
        cls()
        chess.spelen(int(keuze4),chess.bord,chess.pos_koning)
    elif keuze4 == '2': #moeilijk
        cls()
        chess.spelen(2,chess.bord,chess.pos_koning)
    elif keuze4 == '3':
        cls()
        chess.spelen(2,chess.bord_klein,chess.pos_koning)
    elif keuze4 == '4': #teruggaan
        mainmenu()
    else:
      printer('Dit is niet mogelijk, voer opnieuw een keuze in.')
      sys.stdout.write("\033[F")
      sys.stdout.write("\033[K")
      keuzechecker4()


def mainmenu():
    cls()
    #aanhef past zich aan je eigen tijd aan
    #tijd -1 want repl heeft andere localtime dan in Nederland
    result = time.localtime()
    if result.tm_hour<5:
        aanhef="Goedenacht, het is al laat, je bed roept je"
    elif result.tm_hour<11:
        aanhef="Goedemorgen"
    elif result.tm_hour<17:
        aanhef="Goedemiddag"
    else:
        aanhef="Goedenavond"
    printer(aanhef+"! Welkom bij Diep Blauw. Hieronder staan de mogelijkheden:")
    printer("\n1. Begin een nieuw spel \n2. Schaakregels \n3. Stop met spelen\n\n")
    keuzechecker1() #runt de eerste vraag naar input van de gebruiker

mainmenu()