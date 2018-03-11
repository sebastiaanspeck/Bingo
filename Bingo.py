from random import randint
import os
import copy

kaart = []
kaartBegin = []

def menu():
    cls()
    correct = True
    while correct:
        print('Welkom bij Bingo \n- Menu Bingo - \nSingleplayer  (S)\nMultiplayer   (M)\nQuit          (Q)')
        keuze = input('\nKies een optie (S, M, of Q): ')
        if keuze.upper() == 'S':
            cls()
            correct = False
            singleplayer()
        elif keuze.upper() == 'M':
            cls()
            correct = False
            multiplayer()
        elif keuze.upper() == 'Q':
            quit()
        else:
            cls()
            print('Je hebt een foute keuze gemaakt')

def singleplayer():
    speelkaart = vulKaart()
    kaartBegin = copy.deepcopy(speelkaart) 
    printKaart(speelkaart)
    input('Druk op Enter om het spel te starten')
    speelBingo(speelkaart, kaartBegin)

def multiplayer():
    global kaart
    global kaartBegin
    keuze = False
    while keuze == False:
        spelers = int(input('Met hoeveel spelers wil je spelen?: '))
        if spelers > 1:
            keuze = True
    for i in range(spelers):
        kaart.append(vulKaart())
        kaartBegin.append(copy.deepcopy(kaart[i]))
        print('\nSpeelkaart speler ',i+1, ': ', sep='')
        printKaart(kaart[i])

    input('Druk op Enter om het spel te starten')
    speelBingoMulti(spelers)
        

def vulKaart():
    kaart = [['.' for x in range(5)] for x in range(5)]
    nummers = []
    for j in range(5):
        for i in range(5):
            a = randint(1,99)
            while a in nummers:
                a = randint(1,99)
            kaart[i][j] = a
            nummers.append(a)
    return kaart

def printKaart(kaart):
    decimaal = [1,2,3,4,5,6,7,8,9,'X']
    i = 0
    print('|----|----|----|----|----|')
    for i in range(len(kaart)):
        for x in range(len(kaart[i])):
            if x == 0 and kaart[i][x] in decimaal:
                print('|',kaart[i][x],' |', end='')
            elif  x == 0:
                print('|',kaart[i][x],'|', end='')
            if x > 0:
                if kaart[i][x] in decimaal:
                    print('',kaart[i][x],' |', end='')
                else:
                    print('',kaart[i][x],'|', end='')
        if i < (len(kaart)-1):
            print('\n|----+----+----+----+----|')
        else:
            print('\n|----|----|----|----|----|')

def speelBingo(kaart, kaartBegin):
    beurt = 0
    gespeeldenummers = []
    gewonnen = False
    while gewonnen == False:
        cls()
        beurt += 1
        nummer = randint(1,99)
        while nummer in gespeeldenummers:
            nummer = randint(1,99)
        if nummer not in gespeeldenummers:
            gespeeldenummers.append(nummer)
        print('Aantal beurten:', beurt,'\nGetrokken nummer:', nummer)
        for i in range(len(kaart)):
            for x in range(len(kaart[i])):
                if nummer == kaart[i][x]:
                    kaart[i][x] = 'X'
        for i in range(5):
            if kaart[i][0] == 'X' and kaart[i][1] == 'X' and kaart[i][2] == 'X' and kaart[i][3] == 'X' and kaart[i][4] == 'X':
                gewonnen = True
        for i in range(5):
            if kaart[0][i] == 'X' and kaart[1][i] == 'X' and kaart[2][i] == 'X' and kaart[3][i] == 'X' and kaart[4][i] == 'X':
                gewonnen = True
        if kaart[0][0] == 'X' and kaart[1][1] == 'X' and kaart[2][2] == 'X' and kaart[3][3] == 'X' and kaart[4][4] == 'X':
            gewonnen = True
        elif kaart[0][4] == 'X' and kaart[1][3] == 'X' and kaart[2][2] == 'X' and kaart[3][1] == 'X' and kaart[4][0] == 'X':
            gewonnen = True
        print('Kaart:')
        printKaart(kaart)
        input('Druk op Enter om een nieuw getal te trekken')
    cls()
    print('Bingo! \n','\nGetrokken nummers: ')
    gespeeldenummers.sort()
    for i in range(len(gespeeldenummers)):
        if (i+1) % 10 == 0:
            if gespeeldenummers[i] < 10:
                print(gespeeldenummers[i],'',sep='')
            else:
                print(gespeeldenummers[i],sep='')
        elif i == len(gespeeldenummers)-1:
            print(gespeeldenummers[i],end='')
        elif gespeeldenummers[i] < 10:
            print(' ',gespeeldenummers[i],', ',end='', sep='')
        else:
            print(gespeeldenummers[i],', ',end='', sep='')
    print('\n\nKaart begin: ')
    printKaart(kaartBegin)
    print('\nKaart einde: ')
    printKaart(kaart)
    goedeKeuze = False
    while goedeKeuze == False:
        keuze = input('Het spel is afgelopen \n1. Terug naar het menu \n2. Afsluiten\nUw keuze: ')
        if keuze == '1':
            menu()
            goedeKeuze == True
        elif keuze == '2':
            quit() 

def speelBingoMulti(spelers):
    beurt = 0
    gespeeldenummers = []
    gewonnen = False
    while gewonnen == False:
        cls()
        beurtSpeler = 0
        beurt += 1
        nummer = randint(1,99)
        while nummer in gespeeldenummers:
            nummer = randint(1,99)
        if nummer not in gespeeldenummers:
            gespeeldenummers.append(nummer)
        print('Aantal beurten:', beurt,'\nGetrokken nummer:', nummer)
        for i in range(spelers):
            for i in range(len(kaart[beurtSpeler])):
                for x in range(len(kaart[beurtSpeler][i])):
                    if nummer == kaart[beurtSpeler][i][x]:
                        kaart[beurtSpeler][i][x] = 'X'
            for i in range(5):
                if kaart[beurtSpeler][i][0] == 'X' and kaart[beurtSpeler][i][1] == 'X' and kaart[beurtSpeler][i][2] == 'X' and kaart[beurtSpeler][i][3] == 'X' and kaart[beurtSpeler][i][4] == 'X':
                    gewonnen = True
                    beurtSpeler = beurtSpeler
            for i in range(5):
                if kaart[beurtSpeler][0][i] == 'X' and kaart[beurtSpeler][1][i] == 'X' and kaart[beurtSpeler][2][i] == 'X' and kaart[beurtSpeler][3][i] == 'X' and kaart[beurtSpeler][4][i] == 'X':
                    gewonnen = True
                    beurtSpeler = beurtSpeler
            if kaart[beurtSpeler][0][0] == 'X' and kaart[beurtSpeler][1][1] == 'X' and kaart[beurtSpeler][2][2] == 'X' and kaart[beurtSpeler][3][3] == 'X' and kaart[beurtSpeler][4][4] == 'X':
                gewonnen = True
                beurtSpeler = beurtSpeler
            elif kaart[beurtSpeler][0][4] == 'X' and kaart[beurtSpeler][1][3] == 'X' and kaart[beurtSpeler][2][2] == 'X' and kaart[beurtSpeler][3][1] == 'X' and kaart[beurtSpeler][4][0] == 'X':
                gewonnen = True
                beurtSpeler = beurtSpeler
            print('Speler:', beurtSpeler+1, '\nKaart:')
            printKaart(kaart[beurtSpeler])
            if gewonnen == False:
                beurtSpeler += 1
        input('Druk op Enter om een nieuw getal te trekken')
    cls()
    print('Bingo! \n','\nBeurten:',beurt,'\nDe winnaar is: Speler', beurtSpeler,'\nGetrokken nummers: ')
    gespeeldenummers.sort()
    for i in range(len(gespeeldenummers)):
        if (i+1) % 10 == 0:
            if gespeeldenummers[i] < 10:
                print(gespeeldenummers[i],'',sep='')
            else:
                print(gespeeldenummers[i],sep='')
        elif i == len(gespeeldenummers)-1:
            print(gespeeldenummers[i],end='')
        elif gespeeldenummers[i] < 10:
            print(' ',gespeeldenummers[i],', ',end='', sep='')
        else:
            print(gespeeldenummers[i],', ',end='', sep='')
    print('\n\nKaart begin: ')
    printKaart(kaartBegin[beurtSpeler])       
    print('\nKaart einde: ')
    printKaart(kaart[beurtSpeler]) 
    goedeKeuze = False
    while goedeKeuze == False:
        keuze = input('Het spel is afgelopen \n1. Terug naar het menu \n2. Afsluiten\nUw keuze: ')
        if keuze == '1':
            menu()
            goedeKeuze == True
        elif keuze == '2':
            quit() 

def cls():
    os.system('cls')           

menu()
