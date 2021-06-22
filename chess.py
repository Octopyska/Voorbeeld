import random
import os


bord = [\
  ['R','N','B','Q','K','B','N','R'], #8
  ['P','P','P','P','P','P','P','P'], #7
  [' ',' ',' ',' ',' ',' ',' ',' '], #6
  [' ',' ',' ',' ',' ',' ',' ',' '], #5
  [' ',' ',' ',' ',' ',' ',' ',' '], #4
  [' ',' ',' ',' ',' ',' ',' ',' '], #3
  ['p','p','p','p','p','p','p','p'], #2
  ['r','n','b','q','k','b','n','r'], #1
]  #A  #B  #C  #D  #E  #F  #G  #H                                                                  


bord_klein = [\
   [' ',' ','B','Q','K','B',' ',' '], #8
   [' ',' ','P','P','P','P',' ',' '], #7
   [' ',' ',' ',' ',' ',' ',' ',' '], #6
   [' ',' ',' ',' ',' ',' ',' ',' '], #5
   [' ',' ',' ',' ',' ',' ',' ',' '], #4
   [' ',' ',' ',' ',' ',' ',' ',' '], #3
   [' ',' ','p','p','p','p',' ',' '], #2
   [' ',' ','b','q','k','b',' ',' '], #1
 ]  #A  #B  #C  #D  #E  #F  #G  #H                                                                   



coördinaten_kolom = ['A','B','C','D','E','F','G','H']
coördinaten_rij = ['8','7','6','5','4','3','2','1']
#stukken in dictionary
stukken = {'p':'♟','r':'♜','n':'♞','b':'♝','q':'♛','k':'♚',
           'P':'♙','R':'♖','N':'♘','B':'♗','Q':'♕','K':'♔',' ':' '}
def BordPrinten(bord): #Functie printen van bord
    print('  '+33*'-')                  
    for rij in range(8):
        print(coördinaten_rij[rij],'| ',end='')
        for kolom in range(8):
            print(stukken[bord[rij][kolom]],end=' | ')
        print('')
        print('  '+33*'-') 
    print('   ','   '.join(coördinaten_kolom)+'  ')

waarde_stukken = {'p':1, 'n':3, 'b':3, 'r':5, 'q':9, 'k':0, ' ':0}
def WaardeBerekenen(lijst): #Deze functie berekent het aantal punten op het bord door te kijken welke stukken er op het bord staan en hiervan het aantal betreffende punten erbij op te tellen (voor wit) of eraf te trekken (voor zwart).
    totaal = 0
    for rij in range(0, 8):
        for kolom in range(0,8):
            if stuk_kleur(lijst,rij,kolom) == 0:
                totaal = totaal + waarde_stukken[lijst[rij][kolom]]
            elif stuk_kleur(lijst,rij, kolom) == 1:
                string = lijst[rij][kolom].lower()
                totaal = totaal - waarde_stukken[string]
    return totaal

#Deze waardes heb ik van https://en.wikipedia.org/wiki/Chess_piece_relative_value 
waarde_pion = {
0:[[1.06,1.45],[0.97,1.33],[0.90,1.25],[0.90,1.20],[0.90,1.20]],7:[[1.06,1.45],[0.97,1.33],[0.90,1.25],[0.90,1.20],[0.90,1.20]], #Hier staan kolom a&h
1:[[1.12,1.29],[1.03,1.17],[0.95,1.10],[0.95,1.05],[0.95,1.05]],6:[[1.12,1.29],[1.03,1.17],[0.95,1.10],[0.95,1.05],[0.95,1.05]], #Hier staan kolom b&g
2:[[1.25,1.16],[1.17,1.07],[1.10,1.00],[1.05,0.95],[1.05,0.95]],5:[[1.25,1.16],[1.17,1.07],[1.10,1.00],[1.05,0.95],[1.05,0.95]], #Hier staan kolom c&f
3:[[1.40,1.05],[1.27,1.00],[1.20,0.95],[1.15,0.90],[1.10,0.90]],4:[[1.40,1.05],[1.27,1.00],[1.20,0.95],[1.15,0.90],[1.10,0.90]]  #Hier staan kolom d&e
}

waarde_knight = { #waarde van het paard op alle posities op het bord
0:[3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0],  7:[3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0],
1:[3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0],  6:[3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0],
2:[3.0,3.0,3.0,3.0,3.0,3.15,3.0,3.0], 5:[3.0,3.0,3.0,3.0,3.0,3.15,3.0,3.0],
3:[3.0,3.0,3.0,3.4,3.2,3.15,3.0,3.0], 4:[3.0,3.0,3.0,3.4,3.2,3.15,3.0,3.0]
}
isolated_connected_passed = {2:[2.1,2.1,2.1,3.5],3:[1.3,1.35,1.55,2.3],4:[1.05,1.15,1.30,1.55]}
def WaardeBerekenen2(bord,stuk_positie): #Deze functie berekent een precies aantal punten dat op het bord staat voor een kleur, die bedoelt is voor de engine. 
    waarde = 0
    [rij,kolom] = stuk_positie
    if bord[rij][kolom].lower() == 'p':
        Isolated = True
        is_passed = True
        waarde = waarde_pion[kolom][rij-2][begin_einde]
        if rij in [4,3,2]:#isolated, connected, passed. staat op rank 4,5,6
            if kolom > 0: #Isolated
                for rijtest in range(8):
                    if bord[rijtest][kolom-1].lower() == 'p':
                        Isolated = False
                        break
            if kolom < 7 and Isolated == True:
                for rijtest in range(8):
                    if bord[rijtest][kolom+1].lower() == 'p':
                        Isolated = False
                        break
            for rij_passed in range(0,rij): #ispassed
                if bord[rij_passed][kolom] == pion[1-turn]:
                    is_passed = False
                    break
                if kolom < 7:
                    if bord[rij_passed][kolom+1] == pion[1-turn]:
                        is_passed = False
                if kolom > 0:
                    if bord[rij_passed][kolom-1] == pion[1-turn]:
                        is_passed = False
            #vermenigvuldigt als er bonuses zijn op de pionen
            if is_passed == True and Isolated == False:
                vermenigvuldiger = isolated_connected_passed[rij][3]
            elif is_passed == True:
                vermenigvuldiger = isolated_connected_passed[rij][2]
            elif Isolated == True:
                vermenigvuldiger = isolated_connected_passed[rij][0]
            elif Isolated == False:
                vermenigvuldiger = isolated_connected_passed[rij][1]
            else:
                vermenigvuldiger = 1
            waarde *= vermenigvuldiger
    elif bord[rij][kolom].lower() == 'n':
        waarde = waarde_knight[kolom][rij] #waarde uit dictionary halen
    elif bord[rij][kolom].lower() == 'b':
        if rij == 6:
            if kolom in [1,3,4,6] and stuk_kleur(bord,rij-1,kolom+1) or stuk_kleur(bord,rij-1,kolom-1):
                waarde = 3.4
            else:
                waarde = 3
        elif rij == 5:
            if kolom in [0,7]:
                waarde = 3.1
            else:
                waarde = 3
        elif rij == 4:
            if kolom in [2,5] and stuk_kleur(bord,rij-1,kolom+1) != turn or stuk_kleur(bord,rij-1,kolom-1) != turn:
                waarde = 4
            else:
                waarde = 3.4
        else:
            waarde = 3
    elif bord[rij][kolom].lower() == 'r':
        if kolom in [2,3,4,5]: #Als de rook een beetje naar het midden toestaat is die meer waard
            waarde = 5.5
        else:
            waarde = 5
    elif bord[rij][kolom].lower() == 'q': #altijd 11
        waarde = 11
    elif bord[rij][kolom].lower() == 'k': #wordt een beetje waard als de koning op de achterste rij staat en op B of G
        if rij == 7:
            waarde = 1
    return waarde

def punten_bord(bord): #Berekent de punten van de engine uit. 
    wit_punten = 0
    zwart_punten = 0
    for teller in range(2):
        for rij in range(8):
            for kolom in range(8):
                kleur = stuk_kleur(bord,rij,kolom)
                if kleur == -1:
                    continue
                elif kleur == turn:
                    waarde = WaardeBerekenen2(bord,[rij,kolom])
                    if turn == 0: #witte punten
                        wit_punten += waarde
                    else: #zwarte punten
                        zwart_punten += waarde
        bord = turn_swap(bord)
    return wit_punten-zwart_punten

def Zet_Maken():  #maakt van e2e4, koordinaten op het bord zodat de computer kan rekenen,.
    while True:
        zet = input(zwart_wit + " aan zet: ").lower() #vraag aan spelar om coördinaten
        if zet[:2] != zet[2:] and len(zet) == 4:                 
            if ord(zet[0]) in range(97,105) and ord(zet[2]) in range(97,105) and zet[1] in coördinaten_rij and zet[3] in  coördinaten_rij: 
                rij_pre =  (int(zet[1])-1)        
                kolom_pre = ord(zet[0])-97  
                rij_post =  (int(zet[3])-1) 
                kolom_post = ord(zet[2])-97     
                rij_pre = abs(7*(1-turn) - rij_pre) #Moet omdraaien als zwart aan zet is
                rij_post = abs(7*(1-turn) - rij_post)  
                kolom_pre = abs(7*(turn) - kolom_pre)
                kolom_post = abs(7*(turn) - kolom_post)
                return([rij_pre,kolom_pre,rij_post,kolom_post])
            else: 
                print("Coördinaten bestaan niet op het bord. Schrijf bijvoorbeeld e4e5 (tussen a-h, 1-8).")
        else:
            print("Dit kan niet") 

turn = 0 #Variabelen die bijhouden wie er aan zet is.
zwart_wit = "Wit" #Wordt gebruikt bij de print functie en bij de input in ( Zet_Maken() )
def turn_swap(bord): #zorgt 
    global turn 
    global zwart_wit
    if turn == 0: #Als wit aan zet was, zwart nu aan zet. 
        turn = 1 
        zwart_wit = "Zwart"
    else: #Anders som 
        turn = 0 
        zwart_wit = "Wit"
    bord.reverse() 
    for rij in bord:  
        rij.reverse() 
    coördinaten_kolom.reverse() #voor het printen van de kolomen en rijen aan de onderkant en zijkant
    coördinaten_rij.reverse()
    return bord

def stuk_kleur(bord,rij,kolom): #kijkt coordinaten op bord en kijkt welke kleur het is
    if bord[rij][kolom] == ' ': 
        return(-1)
    elif ord(bord[rij][kolom]) > 96: #kleine letter dus witte kleur
        return(0)
    else: 
        return(1) #zwarte kleur

pos_koning = [[7,4],[7,3]]
def positie_koning(rij_k,kolom_k,pos_koning): #verandert positie van de koning, deze houden we bij zodat we niet de koning de hele tijd op moeten zoeken bij een functie zoals schaak.
    pos_koning[turn][0] = rij_k
    pos_koning[turn][1] = kolom_k    
    return pos_koning

stukken_check = ['r','n','b','k','q']
pion = ['p','P']
def schaak(bord,rij_koning,kolom_koning): #kijkt of een positie op het bord schaak staat. 
    if rij_koning != 0: #Pionen checken
        if kolom_koning > 0:
            if bord[rij_koning-1][kolom_koning-1] == pion[1-turn]:
                return True
        if kolom_koning < 7:
            if bord[rij_koning-1][kolom_koning+1] == pion[1-turn]:
                return True
    for stuk in stukken_check: #stukken checken
        for [rij_verschil,kolom_verschil] in richting[stuk]:
            rij_test = rij_koning+ rij_verschil
            kolom_test = kolom_koning + kolom_verschil
            while rij_test in range(8) and kolom_test in range(8):
                if stuk_kleur(bord,rij_test,kolom_test) == 1-turn and bord[rij_test][kolom_test].lower() == stuk:
                    return True
                elif stuk_kleur(bord,rij_test,kolom_test) == 1-turn and bord[rij_test][kolom_test].lower() != stuk:
                    break
                elif stuk_kleur(bord,rij_test,kolom_test) == turn:
                    break
                rij_test += rij_verschil
                kolom_test += kolom_verschil
                if stuk in ['k','n']:   #Moet while loop niet heralen bij k en n
                    break
    return False

def schaak_positie(bord,rij_pre,kolom_pre,rij_post,kolom_post,pk): #Kijkt of na een zet, je schaak staat of niet. 
    pos_koning = diepecopy(pk)
    stuk_bewaren = bord[rij_post][kolom_post]
    bord[rij_post][kolom_post] = bord[rij_pre][kolom_pre]
    bord[rij_pre][kolom_pre] = ' '
    if bord[rij_post][kolom_post].lower() == 'k':
        pos_koning = positie_koning(rij_post,kolom_post,pos_koning)
    isschaak = schaak(bord,pos_koning[turn][0],pos_koning[turn][1])
    bord[rij_pre][kolom_pre] = bord[rij_post][kolom_post]
    bord[rij_post][kolom_post] = stuk_bewaren
    if bord[rij_pre][kolom_pre].lower() == 'k':
        pos_koning = positie_koning(rij_post,kolom_post,pos_koning)
    return isschaak

rokade_mogelijk = [[1,1],[1,1]]
richting = {'r':[[1,0],[-1,0],[0,1],[0,-1]],'n':[[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2],],'b':[[1,1],[-1,1],[1,-1],[-1,-1]],
            'q':[[1,1],[-1,1],[1,-1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]],'k':[[1,1],[-1,1],[1,-1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]]}
def mogelijke_zetten(bord,pos_koning): #Deze functie berekent alle mogelijke zetten voor een kleur en zet deze in een list. Hiermee kan je kijken of er een pad is (geen zetten meer mogelijk) of er een schaakmat is (geen zitten meer mogelijk en de speler staat schaak). Ook kun je er een simple engine mee maken. 
    zetten = []
    for rij in range(8):
        for kolom in range(8):
            if stuk_kleur(bord,rij,kolom) == turn: #alle stukken van de speler.
                stuk = bord[rij][kolom].lower()
                if stuk == 'p':
                    if rij == 6:
                        for i in range(1,3):
                            if bord[rij-i][kolom] == ' ':
                                if schaak_positie(bord,rij,kolom,rij-i,kolom,pos_koning) == False:
                                    zetten.append([rij,kolom,rij-i,kolom])
                            else:
                                break
                    else:
                        if bord[rij-1][kolom] == ' ':
                            if schaak_positie(bord,rij,kolom,rij-1,kolom,pos_koning) == False:
                                zetten.append([rij,kolom,rij-1,kolom])
                    if kolom > 0:
                        if bord[rij-1][kolom-1] != ' ' and stuk_kleur(bord,rij-1,kolom-1) == 1-turn:
                            if schaak_positie(bord,rij,kolom,rij-1,kolom-1,pos_koning) == False:
                                zetten.append([rij,kolom,rij-1,kolom-1])
                    if kolom < 7:
                        if bord[rij-1][kolom+1] != ' ' and stuk_kleur(bord,rij-1,kolom+1) == 1-turn:
                            if schaak_positie(bord,rij,kolom,rij-1,kolom+1,pos_koning) == False:
                                zetten.append([rij,kolom,rij-1,kolom+1])
                elif stuk in ['r','n','b','q','k']:
                    for [rij_verschil,kolom_verschil] in richting[stuk]: #uit dictionary halen
                        rij_test = rij + rij_verschil
                        kolom_test = kolom + kolom_verschil
                        while rij_test in range(8) and kolom_test in range(8):
                            if bord[rij_test][kolom_test] == ' ':
                                if schaak_positie(bord,rij,kolom,rij_test,kolom_test,pos_koning) == False:
                                    zetten.append([rij,kolom,rij_test,kolom_test])
                            elif stuk_kleur(bord,rij_test,kolom_test) == 1-turn:
                                if schaak_positie(bord,rij,kolom,rij_test,kolom_test,pos_koning) == False:
                                    zetten.append([rij,kolom,rij_test,kolom_test])
                                break
                            else:
                                break
                            rij_test += rij_verschil
                            kolom_test += kolom_verschil
                            if stuk in ['k','n']:   #Moet while loop niet heralen bij
                                break
                if stuk == 'k': #Rokade
                    if bord[7][7-7*turn].lower() == 'r' and rokade_mogelijk[turn][1-turn] == 1:    #kleine rokade
                        kleine_rokade = True
                        for i in range(4-1*turn,7-7*turn,1-2*turn):    #4-1*turn 7-7*turn
                            if bord[7][i] not in ['k','K',' '] or schaak(bord,7,i) == True: #Kijkt of het veld leeg is en schaak.
                                kleine_rokade = False
                                break
                        if kleine_rokade == True:
                            zetten.append([rij,kolom,rij,6-5*turn]) #6-5*turn, witte koning naar 6, zwarte koning naar 1.
                    if bord[7][7-7*(1-turn)].lower() == 'r' and rokade_mogelijk[turn][turn] == 1 and bord[7][1+5*turn] == ' ': #1+5*turn, 1 voor wit, 5 voor zwart.
                        lange_rokade = True
                        for i in range(4-1*turn,6-5*(1-turn),2*turn-1):
                            if bord[7][i] not in ['k','K',' '] or schaak(bord,7,i) == True:
                                lange_rokade = False
                                break
                        if lange_rokade == True:
                            zetten.append([rij,kolom,rij,2+3*turn]) #Bewegen zet koning
    return(zetten)

def stuk_bewegen(zet,bord,pos_koning): #Krijgt een zet binnen, beweegt deze zet op het bord
    global rokade_mogelijk
    if bord[zet[0]][zet[1]] in ['r','R'] and zet[1] in [0,7] and zet[0] == 7:
        rokade_mogelijk[turn][int(zet[1]/7)] = 0
    elif bord[zet[0]][zet[1]].lower() == 'k':
        if abs(zet[1]-zet[3]) == 2:
            bord[7][(zet[1]+zet[3])//2] = bord[7][7-7*(zet[3]<4)]
            bord[7][7-7*(zet[3]<4)] = ' ' 
        rokade_mogelijk[turn][0] == 0
        rokade_mogelijk[turn][1] == 0
    bord[zet[2]][zet[3]] = bord[zet[0]][zet[1]]
    bord[zet[0]][zet[1]] = ' '
    if bord[zet[2]][zet[3]].lower() == 'k':
        pos_koning = positie_koning(zet[2],zet[3],pos_koning)
    if zet[2] == 0:
        if bord[zet[2]][zet[3]].lower() == 'p':
            bord[zet[2]][zet[3]] = chr(113-32*turn) #grote q voor zwart en kleine voor wit
    return bord,pos_koning

def zetten_invoeren(zetten,bord): #zorgt ervoor dat je een valide zet invoert, anders vraagt de functie nog om een zet, totdat het een keer goed is.
    while True:
        zet = Zet_Maken()
        if zet in zetten:
            return stuk_bewegen(zet,bord,pos_koning)

def Wengine(zetten,bord,pos_koning): #Deze functie is de makkelijke engine. Hij berekent met een andere functie alle zetten en kiest hiervan die hem de meeste punten opleverd, en dus niet de per see de beste zet. 
    alle_zetten = len(zetten)
    if alle_zetten == 0:
        return True
    else:
        waarden = []
        for indexx,[rpre,kpre,rpost,kpost] in enumerate(zetten):
            stuk_bewaren = bord[rpost][kpost]
            bord[rpost][kpost] = bord[rpre][kpre]
            bord[rpre][kpre] = ' '
            waarden.append(WaardeBerekenen(bord))
            bord[rpre][kpre] = bord[rpost][kpost]
            bord[rpost][kpost] = stuk_bewaren
    indexen = []
    for index in range(0, len(waarden)):
        if waarden[index] == min(waarden): #De beste waarde voor engine kiezen
            indexen.append(index)
        else:
            pass
    dezet = random.choice(indexen)
    zet = zetten[dezet]
    stuk_bewegen(zet,bord,pos_koning)
    bord = turn_swap(bord)
def diepecopy(bord): #maakt een copy van het bord, copy.deepcopy is veel langzamer
    a = [] 
    for row in bord:
        a.append(list(row))
    return a

def Octo_Engine(bord,pos_koning): #Engine kijkt 4 keer vooruit, kijk minimax in verslag
    zetten = mogelijke_zetten(bord,pos_koning)
    if len(zetten) == 0:
        return 'checkmate' 
    waarden = []
    for i,zet in enumerate(zetten): #met 1 achter (1 diep)
        print('',round(100*i/len(zetten),1),'%', end='\r')
        bord_test = diepecopy(bord) #maakt een nieuw bord aan om aan te rekenen
        pk_test = diepecopy(pos_koning)
        bord_test, pk_test = stuk_bewegen(zet,bord_test,pk_test)
        bord_test = turn_swap(bord_test)
        zetten1 = mogelijke_zetten(bord_test,pk_test)
        waarden1 = [] 

        for zet1 in zetten1: #met 2 achter (2 diep) etc.
            bord_test1 = diepecopy(bord_test) #Nog een nieuw bord aan.
            pk_test1 = diepecopy(pk_test)
            bord_test1, pk_test1 = stuk_bewegen(zet1,bord_test1,pk_test1)
            bord_test1 = turn_swap(bord_test1)
            zetten2 = mogelijke_zetten(bord_test1,pk_test1)
            waarden2 = []

            for zet2 in zetten2:
                bord_test2 = diepecopy(bord_test1) #nieuw bord aan.
                pk_test2 = diepecopy(pk_test1)
                bord_test2, pk_test2 = stuk_bewegen(zet2,bord_test2,pk_test2)
                bord_test2 = turn_swap(bord_test2)
                zetten3 = mogelijke_zetten(bord_test2,pk_test2)  
                waarden3 = []

                for zet3 in zetten3:
                    bord_test3 = diepecopy(bord_test2) #nieuw bord aan
                    pk_test3 = diepecopy(pk_test2)
                    bord_test3, pk_test3 = stuk_bewegen(zet3,bord_test3,pk_test3)    
                    waarden3.append(punten_bord(bord_test3)) #De waardes onderaan de tree.
                if len(zetten3) == 0:
                    if schaak(bord,pk_test2[turn][0],pk_test2[turn][1]) == True: #schaakmat
                        waarden3.append(1000000)
                    else: #patstelling
                        waarden3.append(0) #patstelling niet afgekregen. Moet werken met de huidige stand.
                waarden2.append(max(waarden3)) #hoogste waarde pakken (wit wil dit)
                bord_test2 = turn_swap(bord_test2)

            if len(zetten2) == 0:
                if schaak(bord,pk_test1[turn][0],pk_test1[turn][1]) == True: #schaakmat
                    waarden2.append(-1000000)
                else: #patstelling
                    waarden2.append(0) #patstelling niet afgekregen. Moet werken met de huidige stand.                
            waarden1.append(min(waarden2)) #kleine waarde, zwart wil dit.
            bord_test1 = turn_swap(bord_test1)

        if len(zetten1) == 0:
            if schaak(bord,pk_test[turn][0],pk_test[turn][1]) == True: #schaakmat
                waarden1.append(1000000)
            else: #patstelling      
                waarden1.append(0) #patstelling niet afgekregen. Moet werken met de staande stand.  
        waarden.append(max(waarden1))
        bord_test = turn_swap(bord_test)

    return zetten[waarden.index(min(waarden))]
def cls(): #functie gevonden op internet om console te clearen
    os.system('cls' if os.name=='nt' else 'clear') 


def spelen(keuze4,bord,pos_koning): #Deze functie zorgt ervoor dat je kan blijven spelen totdat er een checkmate is. 
    global begin_einde
    beurt = 0
    checkmate_pattstelling = False
    while checkmate_pattstelling == False:
        if beurt > 15: #Endgame of midgame
            begin_einde = 1
        else:
            begin_einde = 0        
        cls()
        BordPrinten(bord) 
        zetten = mogelijke_zetten(bord,pos_koning)
        totaal = WaardeBerekenen(bord)
        if totaal > 0:
            print("Score :",'+'+str(totaal))
        else:
            print("Score :",totaal)
        if len(zetten) == 0: #dus pat of schaakmate
            checkmate_pattstelling = True
            if schaak(bord,pos_koning[turn][0],pos_koning[turn][1]) == True:
                BordPrinten(bord)
                print("CHECKMATE")
            else:
                BordPrinten(bord)
                print("STALEMATE")
            break
        zetten_invoeren(zetten,bord)
        if keuze4 == 1: #Wengine
            bord = turn_swap(bord)
            zetten = mogelijke_zetten(bord,pos_koning)
            checkmate = Wengine(zetten,bord,pos_koning)
            beurt += 1
            if checkmate == True:
                checkmate_pattstelling = True
                print("Gefeliciteerd, zwart staat schaakmat")
        elif keuze4 == 2: #Octo engine 
            cls()
            BordPrinten(bord)
            print("De Engine is aan het berekenen")
            bord = turn_swap(bord)
            zet = Octo_Engine(bord, pos_koning)
            if zet == 'checkmate':
                checkmate_pattstelling = True
                print("Gefeliciteerd, zwart staat schaakmat")
            else: 
                stuk_bewegen(zet,bord,pos_koning)
                bord = turn_swap(bord)
                beurt += 1
        else: #Een tegen een spelen
            bord = turn_swap(bord)
            beurt += 0.5
