import random
import math

def laske(lista):
    a=0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            a=a+1
    return a



        


class Kaupunki:
    def __init__(self, nimi='', kok=0, asuk=0):
        self.nimi = nimi            #Kaupungin nimi
        self.kokluo = kok           # Kokoluokka
        self.asmaa = asuk           # Asukasmäärä
        self.asal = 0               # Asuinalueitten määrä   
        self.alujak = []            # Alueitten jakomatriisi
        self.aluLohk = []           # Asuinalueet per lohko(mat,nat,kat)
        self.osadata = self.Kaupunginosat() # kaupunginosaluokka osadata:an
        self.asudata = self.Aluedata() # Aluedata(hahmoluokat ja määrät) asudata:an
        self.alulis = []       # Aluelistan luonti
        self.matlohk = [0,0,0,0,0,0,0,0,0,0,0,0,0] # Matalantiheyden alueet
        self.natlohk = [0,0,0,0,0,0,0,0,0,0,0]     # Normaalitiheyden alueet 
        self.katlohk = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Korkeantiheyden
        self.kokoLuokka()           # Tarkistetaan kokoluokka ja tarvittaessa pyydetään
        self.asukasMaara()          # Luodaan asukasmäärä kokoluokan mukaan ja lasketaan alueitten määrä
        self.jakoTasot()            # Katsotaan kokoluokan mukainen jakomatriisi
        self.alueJako()             # Jaetaan alueet ryhmiin
        self.alueet()               # Täytetään *lohk listat 
        self.alulist()              # Täytetään alulist
        

    def kokoLuokka(self):
        if self.kokluo == 0:
            self.kokluo = random.randint(1,6)
        elif 0 < self.kokluo < 7:
            pass
        else: self.kokVal()
            

    def kokVal(self):
        a = input("kokoluokka(1-6), 0 satunnainen")
        try:
           val = int(a)
        except ValueError:
           a = 0
        a = int(a)
        if a > 6:
            a = 6
            print("Yli 6 muutettiin kuudeksi")
        self.kokluo = a
    def alueJako(self):
        for i in range(len(self.alujak)):
            self.aluLohk.append(math.trunc((self.alujak[i]/100)*(self.asal)))

        
    def asukasMaara(self):
        if self.asmaa == 0:
                ## Tarkistaa kaupungin kokoluokan ja palauttaa
                ## asukamäärän
            if self.kokluo == 1:   self.asmaa = random.randint(3000,6500)
            elif self.kokluo == 2: self.asmaa = random.randint(6501,9000)
            elif self.kokluo == 3: self.asmaa = random.randint(9001,20000)
            elif self.kokluo == 4: self.asmaa = random.randint(20001,80000)
            elif self.kokluo == 5: self.asmaa = random.randint(80001,250000)
            elif self.kokluo == 6: self.asmaa = random.randint(250001,1000000)
        else:

                ## Tarkistaa syötetyn asukasluvun pätevyyden ja korjaa kokoluokka virheen
            if self.asmaa < 3000:
                self.kokluo = 1
                self.asmaa = random.randint(3000,6500)
                print("Liian vähän asukkaita, korjattu\n")
            elif 3000 <= self.asmaa < 6501 and self.kokluo !=1: self.kokluo = 1
            elif 6501 <= self.asmaa < 9001 and self.kokluo !=2: self.kokluo = 2
            elif 9001 <= self.asmaa < 20001 and self.kokluo !=3: self.kokluo = 3
            elif 20001 <= self.asmaa < 80001 and self.kokluo !=4: self.kokluo = 4
            elif 80001 <= self.asmaa < 250001 and self.kokluo !=5: self.kokluo = 5
            elif 250001 <= self.asmaa < 1000001 and self.kokluo !=6: self.kokluo = 6
            else:
                self.kokluo = 6
                self.asmaa =  random.randint(250001,1000000)
                print("Liikaa asukkaita, korjattu alas\n")
        self.asal =  self.asmaa//500
        
    def jakoTasot(self):
        ## Luo jakomatriisin
        
        if self.kokluo == 1:   self.alujak = [70, 20, 10]
        elif self.kokluo == 2: self.alujak = [65, 25, 10]
        elif self.kokluo == 3: self.alujak = [60, 25, 15]    
        elif self.kokluo == 4: self.alujak = [55, 30, 15]
        elif self.kokluo == 5: self.alujak = [45, 35, 20]
        elif self.kokluo == 6: self.alujak = [35, 35, 30]

    def AsutusYht(self):
        a = 0
        a = sum(self.aluLohk)
        return a

    def alueet(self):
        while sum(self.matlohk) < self.aluLohk[2]:
            for i in range(len(self.osadata.matalalista)):
                # Useampi kuin yksi harvinaisuus korjaus
                if self.matlohk[0] > 0:
                    self.osadata.matalamaarat[0] = self.osadata.matalamaarat[0]*1.08
                if self.matlohk[1] > 0:
                    self.osadata.matalamaarat[1] = self.osadata.matalamaarat[1]*1.2
                if self.matlohk[6] > 0:
                    self.osadata.matalamaarat[6] = self.osadata.matalamaarat[6]*1.1
                if self.matlohk[7] > 0:
                    self.osadata.matalamaarat[7] = self.osadata.matalamaarat[7]*1.4
                if self.matlohk[11] > 0:
                    self.osadata.matalamaarat[11] = self.osadata.matalamaarat[11]*1.2
                # lohkojen luonti
                if (self.aluLohk[2] - sum(self.matlohk))//\
                (self.osadata.matalamaarat[i]+random.randint(0, 6)) > 0: 
                    self.matlohk[i] = self.matlohk[i]+1
                if sum(self.matlohk) == self.aluLohk[2]:
                    break
        while sum(self.natlohk) < self.aluLohk[1]:
            for i in range(len(self.osadata.normaalilista)):
                # Useampi kuin yksi harvinaisuus korjaus
                if self.natlohk[2] > 0:
                    self.osadata.normaalimaarat[2] = self.osadata.normaalimaarat[2]*1.1
                if self.natlohk[4] > 0:
                    self.osadata.normaalimaarat[4] = self.osadata.normaalimaarat[4]*1.12
                if self.natlohk[5] > 0:
                    self.osadata.normaalimaarat[5] = self.osadata.normaalimaarat[5]*1.38
                if self.natlohk[10] > 0:
                    self.osadata.normaalimaarat[10] = self.osadata.normaalimaarat[10]*1.055
                # lohkojen luonti
                if (self.aluLohk[1] - sum(self.natlohk))//\
                (self.osadata.normaalimaarat[i]+random.randint(0, 6)) > 0: 
                    self.natlohk[i] = self.natlohk[i]+1
                if sum(self.natlohk) == self.aluLohk[1]:
                    break
        while sum(self.katlohk) < self.aluLohk[0]:
            for i in range(len(self.osadata.korkealista)):
                # Useampi kuin yksi harvinaisuus korjaus
                if self.katlohk[3] > 0:
                    self.osadata.korkeamaarat[3] = self.osadata.korkeamaarat[3]*1.2
                if self.katlohk[14] > 0:
                    self.osadata.korkeamaarat[14] = self.osadata.korkeamaarat[14]*1.12
                if self.katlohk[16] > 0:
                    self.osadata.korkeamaarat[16] = self.osadata.korkeamaarat[16]*1.04
                # lohkojen luonti
                if (self.aluLohk[0] - sum(self.katlohk))//\
                (self.osadata.korkeamaarat[i]+random.randint(0, 6)) > 0: 
                    self.katlohk[i] = self.katlohk[i]+1
                if sum(self.katlohk) == self.aluLohk[0]:
                    break
                
    def alulist(self):
        for i in range(42): self.alulis.append([])
        for i in range(len(self.matlohk)):
            for j in range(self.matlohk[i]):
                typ = self.osadata.aluetyypit[0][i]
                self.alulis[typ].append(self.Alue(str(j), self.osadata.matalalista[i], typ, 350, '@', i))
        for i in range(len(self.natlohk)):
            for j in range(self.natlohk[i]):
                typ = self.osadata.aluetyypit[1][i]
                self.alulis[typ].append(self.Alue(str(j), self.osadata.normaalilista[i], typ, 450, '$', i))
        for i in range(len(self.katlohk)):
            for j in range(self.katlohk[i]):
                typ = self.osadata.aluetyypit[2][i]
                self.alulis[typ].append(self.Alue(str(j), self.osadata.korkealista[i], typ, 550, 'x', i))
        self.alulis[41].append(self.Alue('meri', "meri", 99, 0, '~', -1))         
    class Alue:
        def __init__(self,nim='', typ="",typnum=[], asuluku=0, tih='',tinu=0):
            self.nimi = nim
            self.tyyppi = typ
            self.tyyppinum = typnum
            self.asukasluku = asuluku
            self.tihe = tih
            self.tihnum = tinu
    
    class Kaupunginosat:
        def __init__(self):
            self.matalalista = ["Civic district", "Civic district, ruined",
                           "Elf neighborhood", "Embassy district",
                           "Finance district", "Fine shops", "Lord’s keep",
                           "Lord’s keep, vacant", "Magic district",
                           "Noble estates", "Park district", "University",
                           "Wealthy residential"]
            
            self.normaalilista = ["Average residential", "Dwarf neighborhood",
                             "Garrison", "Gnome neighborhood",
                             "Guildhall district", "Guildhall district, former",
                             "Halfling encampment", "Marketplace",
                             "Professionals", "Shops", "Temple district"]
            
            self.korkealista = ["Adventurer’s quarter", "Anglers’ wharf",
                           "Apartment homes", "Caravan district",
                           "Goblinoid ghetto", "Inn district",
                           "Red light district", "Shantytown",
                           "Slave quarter", "Slum", "Tannery district",
                           "Tavern district", "Tenement district",
                           "Theater district", "Undercity",
                           "Warehouse district", "Waterfront district"]

            self.aluenimet= ["Civic district", "Civic district, ruined",
                           "Elf neighborhood", "Embassy district",
                           "Finance district", "Fine shops", "Lord’s keep",
                           "Lord’s keep, vacant", "Magic district",
                           "Noble estates", "Park district", "University",
                           "Wealthy residential","Average residential", "Dwarf neighborhood",
                             "Garrison", "Gnome neighborhood",
                             "Guildhall district", "Guildhall district, former",
                             "Halfling encampment", "Marketplace",
                             "Professionals", "Shops", "Temple district","Adventurer’s quarter", "Anglers’ wharf",
                           "Apartment homes", "Caravan district",
                           "Goblinoid ghetto", "Inn district",
                           "Red light district", "Shantytown",
                           "Slave quarter", "Slum", "Tannery district",
                           "Tavern district", "Tenement district",
                           "Theater district", "Undercity",
                           "Warehouse district", "Waterfront district"]
            
            self.matalamaarat = [4, 22, 12, 10, 8, 4, 2, 12, 9, 2, 4, 12, 1]

            self.normaalimaarat = [1, 12, 2, 14, 2, 5, 10, 2, 4, 2, 2]

            self.korkeamaarat = [14, 22, 2, 4, 36, 13, 14, 8, 17, 4, 23, 22,
                                 1, 26, 9, 2, 2]
            self.aluetyypit = [[0,1,2,3,4,5,6,7,8,9,10,11,12],
                               [13,14,15,16,17,18,19,20,21,22,23],
                               [24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]]

          
    class Aluedata:
        def __init__(self):
            self.asukastyypit = ["Bbn", "Brd", "Clr", "Drd", "Ftr", "Mnk",
                            "Pal", "Rgr", "Rog", "Sor", "Wiz", "Adp",
                            "Ari", "Com", "Exp", "War"]
            self.tyypitalue = [[[0, 3,  3, 0,  8, 0, 1, 0,  8, 2, 3, 2, 10, 232, 30, 48],
                                [0, 2,  4, 0,  8, 0, 0, 0,  8, 2, 4, 4,  4, 249, 25, 40],
                                [0, 2,  2, 2,  8, 0, 0, 2,  7, 1, 4, 2,  4, 241, 30, 45],
                                [0, 3,  4, 0,  9, 1, 1, 1,  9, 2, 4, 2, 50, 230, 14, 20],
                                [0, 2,  3, 0,  5, 0, 1, 0, 10, 2, 3, 0, 10, 249, 50, 15],
                                [0, 0,  0, 0,  6, 0, 0, 0, 12, 4, 6, 3,  6, 243, 50, 20],
                                [0, 3,  5, 0, 20, 0, 0, 0,  0, 0, 0, 0, 20, 197, 30, 75],
                                [0, 3,  3, 0, 10, 0, 0, 0,  8, 0, 0, 0,  4, 257, 25, 40],
                                [0, 4,  5, 2,  6, 0, 0, 0,  7, 6, 8, 8,  6, 208, 35, 55],
                                [0, 3,  0, 0, 17, 0, 3, 0,  5, 0, 0, 0, 40, 207, 30, 45],
                                [0, 2,  3, 2,  6, 1, 1, 2,  7, 1, 3, 4,  5, 258, 25, 30],
                                [0, 5,  6, 1,  6, 2, 1, 0,  6, 3, 6, 5, 10, 239, 30, 30],
                                [0, 2,  3, 0,  8, 0, 1, 0,  7, 2, 4, 2, 15, 226, 30, 50]],
                               [[1, 3,  4, 1,  9, 1, 1, 1,  9, 2, 4,  4, 4, 341, 25, 40],
                                [3, 1,  4, 0, 18, 0, 1, 0,  7, 1, 1,  2, 4, 318, 30, 60],
                                [1, 2,  4, 0, 14, 1, 2, 1,  6, 2, 3,  1, 8, 230, 25, 150],
                                [0, 2,  3, 1, 10, 0, 0, 1, 10, 2, 6,  4, 2, 344, 25, 40],
                                [0, 3,  0, 0,  6, 0, 0, 0, 12, 2, 3,  0, 5, 329, 50, 40],
                                [0, 5,  0, 0, 12, 0, 0, 0, 12, 2, 3,  0, 2, 324, 50, 40],
                                [0, 2,  4, 1, 12, 0, 0, 1, 16, 2, 1,  4, 2, 340, 25, 40],
                                [1, 4,  3, 0,  9, 1, 1, 1, 12, 1, 3,  6, 0, 338, 30, 40],
                                [0, 2,  3, 1,  8, 0, 1, 0, 11, 3, 7,  5, 6, 323, 50, 30],
                                [0, 3,  5, 1,  9, 1, 0, 0, 11, 2, 4,  5, 0, 359, 35, 15],
                                [0, 3, 16, 5,  9, 4, 3, 2,  5, 3, 5, 10, 5, 290, 35, 55]],
                               [[5, 9, 12, 5, 25, 2, 2, 3, 25, 4, 8, 10, 2, 338, 40, 60],
                                [0, 0,  2, 0,  8, 0, 0, 0,  8, 0, 0,  6, 0, 490, 16, 20],
                                [2, 3,  4, 1, 11, 1, 1, 1, 13, 2, 5,  5, 0, 446, 20, 35],
                                [4, 5,  3, 1, 12, 2, 0, 2, 15, 3, 5,  4, 4, 405, 25, 60],
                                [5, 0,  3, 0, 10, 0, 0, 0,  8, 0, 0,  4, 0, 425, 15, 80],
                                [2, 8,  3, 1,  9, 1, 1, 2, 16, 2, 6,  5, 5, 439, 30, 20],
                                [4, 8,  2, 0,  9, 0, 0, 0, 16, 2, 3,  5, 0, 426, 25, 50],
                                [0, 0,  0, 0,  0, 0, 0, 0,  4, 0, 0,  2, 0, 542,  0,  2],
                                [2, 0,  0, 0, 12, 0, 0, 0,  8, 0, 0,  0, 0, 483, 25, 20],
                                [2, 1,  1, 0,  8, 0, 0, 0, 12, 1, 0,  8, 0, 480,  5, 32],
                                [2, 2,  1, 1, 10, 0, 0, 0, 15, 2, 1,  6, 0, 455, 25, 30],
                                [2, 8,  3, 0,  9, 0, 0, 1, 16, 2, 3,  4, 0, 437, 25, 40],
                                [3, 3,  4, 1, 11, 0, 0, 1, 16, 2, 3,  5, 0, 471, 10, 20],
                                [0, 7,  0, 0, 12, 0, 0, 0, 15, 0, 0,  4, 0, 442, 30, 40],
                                [4, 2,  5, 0, 16, 1, 0, 1, 24, 3, 6,  8, 2, 403, 25, 50],
                                [0, 2,  0, 0, 12, 0, 0, 0, 24, 0, 0,  5, 0, 437, 20, 50],
                                [2, 5,  3, 1, 12, 1, 1, 0, 16, 1, 2,  5, 0, 436, 25, 40]]]

class Kartta:
    def __init__(self, kaupa):
        self.kaup = kaupa
        self.kokluokorj = 0
        self.laskkokkorj()
        self.xkok = int(round(math.sqrt(sum(self.kaup.aluLohk))*(random.randint(*self.kokluokorj)/10),0))
        self.ykok = int(round(math.sqrt(sum(self.kaup.aluLohk))*(random.randint(*self.kokluokorj)/10),0))
        self.aluli = self.kaup.alulis
        self.kartta = []
        self.tyhjälist = []
        self.karttalist= []
        self.koordlist=[]
        self.todmat = [[[70, 0], [25, 1], [5,  2]],
              [[25, 0], [60, 1], [15, 2]],
              [[5,  0], [15, 1], [80, 2]]]
        self.tarktodmat = [[5, 1, 6, 8, 7, 9, 7, 4, 5, 9, 4, 2, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 3, 4, 3, 4, 6, 7, 5, 4, 9, 4, 4, 4, 5, 3, 1, 2, 4, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [6, 3, 5, 4, 6, 7, 3, 2, 7, 8, 7, 4, 4, 2, 1, 1, 3, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [8, 4, 4, 5, 7, 9, 4, 1, 5, 5, 4, 3, 8, 1, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [7, 3, 6, 7, 7, 6, 3, 1, 7, 8, 3, 2, 7, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [9, 4, 7, 9, 6, 6, 3, 1, 7, 6, 3, 2, 5, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                           [7, 6, 3, 4, 3, 3, 4, 3, 2, 2, 8, 3, 5, 2, 5, 7, 1, 3, 3, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                           [4, 7, 2, 1, 1, 1, 3, 1, 6, 4, 8, 4, 3, 1, 4, 7, 2, 3, 7, 1, 4, 2, 2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                           [5, 5, 7, 5, 7, 7, 2, 6, 5, 5, 6, 8, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [9, 4, 8, 5, 8, 6, 2, 4, 5, 8, 4, 2, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                           [4, 9, 7, 4, 3, 3, 8, 8, 6, 4, 5, 7, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                           [2, 4, 4, 3, 2, 2, 3, 4, 8, 2, 7, 7, 3, 3, 2, 1, 4, 4, 2, 1, 2, 6, 4, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [3, 4, 4, 8, 7, 5, 5, 3, 4, 7, 4, 3, 8, 2, 3, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 4, 2, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 5, 4, 2, 4, 6, 3, 4, 8, 6, 7, 5, 1, 1, 4, 1, 1, 2, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2],
                           [1, 5, 1, 3, 2, 1, 5, 4, 1, 1, 1, 2, 3, 4, 3, 5, 3, 4, 3, 2, 5, 7, 7, 4, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1],
                           [1, 3, 1, 2, 1, 1, 7, 7, 1, 1, 1, 1, 1, 2, 5, 4, 2, 2, 4, 3, 7, 7, 7, 3, 5, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
                           [1, 1, 3, 2, 2, 1, 1, 2, 1, 1, 1, 4, 2, 4, 3, 2, 7, 4, 2, 5, 6, 8, 6, 4, 4, 1, 3, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 4, 1, 1, 1],
                           [2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 4, 2, 6, 4, 2, 4, 4, 2, 4, 7, 7, 7, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
                           [1, 4, 1, 1, 1, 1, 3, 7, 1, 1, 1, 2, 1, 3, 3, 4, 2, 2, 1, 3, 6, 4, 6, 5, 4, 1, 5, 3, 2, 3, 1, 1, 1, 1, 1, 3, 4, 1, 1, 3, 1],
                           [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 3, 5, 4, 3, 5, 6, 8, 6, 4, 6, 1, 3, 4, 2, 3, 1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1],
                           [1, 2, 1, 1, 1, 2, 2, 4, 1, 1, 1, 2, 2, 8, 5, 7, 6, 7, 6, 6, 5, 5, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 2, 2, 1, 2, 2, 3, 2, 1, 1, 1, 6, 1, 6, 7, 7, 8, 7, 4, 8, 5, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 4, 2, 7, 7, 7, 6, 7, 6, 6, 5, 3, 5, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [2, 2, 2, 1, 2, 1, 1, 5, 1, 1, 1, 2, 1, 5, 4, 3, 4, 7, 5, 4, 2, 1, 1, 7, 3, 1, 6, 1, 2, 1, 1, 2, 2, 2, 1, 3, 5, 2, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 4, 3, 4, 6, 1, 1, 2, 3, 6, 1, 4, 4, 3, 6, 4, 2, 1, 3, 1, 6, 4, 3, 2, 3, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,15, 5, 1, 1, 1, 1, 9, 1, 9, 6, 1, 5, 1, 1, 3,15],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 3, 1, 5, 3, 1, 1, 1, 6, 4, 5, 6, 3, 2, 3, 3, 4, 2, 3, 2, 5, 3, 4, 1, 6, 3],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 4, 1, 1, 2, 1, 4, 1, 3, 3, 4, 6, 7, 5, 6, 5, 3, 6, 3, 1, 1, 8, 3],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 3, 1, 2, 4,13, 5, 5, 9, 7, 9, 7, 1, 1, 1, 2, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 3, 3, 1, 1, 1, 1, 6, 1, 3, 6, 5, 7, 6, 3, 2, 3, 1, 7, 5, 5, 2, 1, 6],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 3, 7, 5, 6, 6, 6, 4, 6, 2, 7, 4, 5, 2, 3, 4],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 9, 4, 5, 9, 3, 6, 6, 3, 5, 3, 4, 3, 2, 3, 4, 4],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 6, 7, 2, 4, 3, 8,12, 7, 4, 3, 2, 4, 4, 5],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 9, 3, 5, 9, 3, 6, 5,12, 4, 5, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 2, 3, 7, 1, 2, 3, 7, 5,12, 2, 3, 1, 7, 7, 7],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 2, 1, 3, 3, 1, 1, 1, 3, 6, 1, 5, 6, 1, 7, 7, 4, 4, 2, 2, 5, 3, 5, 2, 2, 2],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 2, 4, 3, 1, 1, 1, 5, 4, 5, 3, 3, 1, 5, 4, 3, 3, 2, 3, 3, 9, 2, 2, 5, 7],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 3, 1, 1, 1, 2, 3, 1, 4, 1, 1, 5, 5, 2, 2, 1, 1, 5, 2,13,15, 4, 5],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 3, 4, 2, 7, 2, 2,15,15, 9, 5],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 3, 6, 8, 1, 1, 3, 4, 4, 2, 7, 2, 5, 4, 9, 8, 4],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,15, 3, 3, 1, 6, 4, 4, 5, 2, 7, 2, 7, 5, 5, 4, 1]]
        self.lupo()
        self.mer()
        self.joki()
        self.onkotilaa()
        self.torit()
        self.ryhm()

    def laskkokkorj(self):
        if self.kaup.kokluo==1:
            self.kokluokorj=(10,90)
        elif self.kaup.kokluo==2:
            self.kokluokorj=(10,70)
        elif self.kaup.kokluo==3:
            self.kokluokorj=(10,50)
        elif self.kaup.kokluo==4:
            self.kokluokorj=(10,40)
        elif self.kaup.kokluo==5:
            self.kokluokorj=(10,30)
        elif self.kaup.kokluo==6:
            self.kokluokorj=(10,25)

    def onkotilaa(self):
        self.tyhjät()
        tilaa=len(self.tyhjälist)
        if tilaa < laske(self.aluli):
            tarvitaan=laske(self.aluli)-tilaa
            for j in range(math.ceil(tarvitaan/self.xkok)):
                for i in range(len(self.kartta)):
                    self.kartta[i].extend([])
        
    def lupo(self):
        for i in range(self.xkok):
            self.kartta.append([])
            for j in range(self.ykok):
                self.kartta[i].append([])
        self.koordlis()

    def koordlis(self):
        for i in range(len(self.kartta)):
            for j in range(len(self.kartta[i])):
                    self.koordlist.append([i, j])
                
    def tyhjät(self):
        for i in range(len(self.kartta)):
            for j in range(len(self.kartta[i])):
                if self.kartta[i][j] == []:
                    self.tyhjälist.append([i, j])

    def karli(self):
        for i in range(len(self.kartta)):
            for j in range(len(self.kartta[i])):
                if self.kartta[i][j] != []:
                    self.karttalist.append([i, j, self.kartta[i][j]])

    def tyyppilista(self, tyyp):
        self.karli()
        retlis=[]
        for i in range(len(self.karttalist)):
            if self.karttalist[i][2].tyyppinum == tyyp: retlis.append([self.karttalist[i][0],self.karttalist[i][1]])
        return retlis
    
    def mer(self):
        logtie.write('mer\n')
        x, y = 0,0
        xraj=int(round(self.xkok/2,0))
        yraj=int(round(self.ykok/2,0))
        if yraj<=3:yraj=4
        if xraj<=3:xraj=4
        meret=[]
        while x<=xraj:
            if x ==xraj:
                meret.append([x,1])
            else:
                for i in range(random.randint(3,yraj)):
                    meret.append([x,i])
            x=x+1
        meret =self.joklisput(0,0,meret)
        meret =self.joklisput(0,1,meret)
        meret =self.joklisput(1,0,meret)
        meret =self.joklisput(1,1,meret)
        for i in range(len(meret)):
            self.kartta[meret[i][0]][meret[i][1]]= self.aluli[41][0]
        

    def joki(self):
        logtie.write('joki\n')
        merlist=[]
        joklis=[]
        summat=[]
        välike=[]
        testrt=[]
        summaluku=0
        ymut=0
        xmut=0
        yvah = (-3, 6)
        xvah = (-3, 6)
        escape=0
        merlist.extend(self.tyyppilista(99))
        for i in range(len(merlist)):
            summat.append([int(round(math.sqrt((merlist[i][0]-(self.xkok/2))**2+(merlist[i][1]-(self.ykok/2))**2),0)),i])
        summat.sort(key=lambda x: x[0])
        summaluku= summat[0][0]
        while summat[0][0]==summaluku:
            välike.append(summat.pop(0))
        todte=random.randint(0, len(välike)-1)
        x, y =self.karttalist[välike[todte][1]][0],self.karttalist[välike[todte][1]][1]
        while not((x==self.xkok)or(y==self.ykok)) :
            xmut =int(round((random.randint(*xvah))*(2/random.randint(1,self.ykok)),0))             
            ymut =int(round((random.randint(*yvah))*(4/random.randint(1,self.xkok)),0))
            if xmut==0 and ymut==0:
                xmut=xmut+6
                ymut=ymut+6
            
            joklis.extend(self.xylis((x+xmut),(y+ymut),x,y))
            x=x+xmut
            y=y+ymut
            testrt.append([x,y])
            escape=escape+1
            if escape==1000:
                logtie.write('escriv\n')
                break
        joklis.extend(self.xylis((x+xmut),(y+ymut),x,y))
        for i in range(len(joklis)):
            if joklis[i]==[]: continue
            self.kartta[joklis[i][0]][joklis[i][1]]= self.aluli[41][0]
        del self.aluli[41]

    def joklisput(self,ind,suun,lis):
        teslis=[]
        lisa = []
        if suun ==0:
            test=0
            for i in range(len(lis)):
                if lis[i][ind]<test:teslis.extend([i])
        if suun ==1:
            if ind ==0:           
                test=self.xkok-1
                for i in range(len(lis)):
                    if lis[i][ind]>test:teslis.extend([i])
            if ind ==1:           
                test=self.ykok-1
                for i in range(len(lis)):
                    if lis[i][ind]>test:teslis.extend([i])            
        if teslis!=[]:
            teslis.reverse()
            for i in range(len(teslis)):
                del lis[teslis[i]]
        return lis
    
    def xylis(self, xuus, yuus,x,y):
        logtie.write(str(xuus)+str(yuus)+str(x)+str(y)+'xylis\n')
        pallis=[]
        xdel=abs(xuus-x)
        ydel=abs(yuus-y)
        case = None
        if x<xuus:
            xpuol=x+(xdel/2)
            poist=[x,xuus]            
        else:
            xpuol=xuus+(xdel/2)
            poist=[x,xuus]
        if y<yuus:
            ypuol=y+(xdel/2)
            poist.extend([y, yuus])
        else:
            ypuol=yuus+(xdel/2)
            poist.extend([yuus, y])
        rad=math.sqrt((xdel/2)**2+(ydel/2)**2)
        
        for i in range(len(self.koordlist)):
            if (rad-0.5)<math.sqrt((self.koordlist[i][0]-xpuol)**2+(self.koordlist[i][1]-ypuol)**2)<(rad+1.5):
                pallis.append(self.koordlist[i])
        ## poist listan sisältö: matala x, korkea x, matala y, korkea y
        if x == xuus: # poistaa vain ylä- tai alakaaren
            case=random.randint(0,1)
            if case == 1:
                for i in range(len(pallis)):
                    if pallis[i][0]>x: pallis[i]=[]
            else:
                for i in range(len(pallis)):
                    if pallis[i][0]<x: pallis[i]=[]
        elif y == yuus: # poistaa vain vasen tai oikean
            case=random.randint(0,1)
            if case == 1:
                for i in range(len(pallis)):
                    if pallis[i][1]>y: pallis[i]=[]
            else:
                for i in range(len(pallis)):
                    if pallis[i][1]<y: pallis[i]=[]
        elif x<xuus: # poistaa joko yläoikean tai alavasemman
            case=random.randint(0,1)
            if case == 1:
                for i in range(len(pallis)):
                    if ((pallis[i][0]<poist[0])and(pallis[i][1]<poist[3]))or((pallis[i][0]>poist[0])and(pallis[i][1]>poist[3])):
                        pallis[i]=[]
            else:
                for i in range(len(pallis)):
                    if ((pallis[i][0]>poist[0])and(pallis[i][1]<poist[2]))or((pallis[i][0]>poist[1])and(pallis[i][1]<poist[3])):
                        pallis[i]=[]
        else: # poistaa joka ylävas tai alaoik
            case=random.randint(0,1)
            if case == 1:
                for i in range(len(pallis)):
                    if ((pallis[i][0]<poist[0])and(pallis[i][1]<poist[3]))or((pallis[i][0]>poist[0])and(pallis[i][1]<poist[2])):
                        pallis[i]=[]
            else:
                for i in range(len(pallis)):
                    if ((pallis[i][0]>poist[0])and(pallis[i][1]>poist[3]))or((pallis[i][0]>poist[1])and(pallis[i][1]<poist[3])):
                        pallis[i]=[]
        return pallis


    def torit(self):
        logtie.write('torit\n')
        if len(self.aluli[20])==0:return None
        else:
            merlist=[]
            mahdlist=[]
            torilist=[]
            summat=[]
            todtest=0
            self.tyhjät()
            self.karli()
            for i in range(len(self.karttalist)):
                if self.karttalist[i][2].tyyppinum == 99: merlist.append([self.karttalist[i][0],self.karttalist[i][1]])
            for i in range(len(self.tyhjälist)):    
                for j in range(len(merlist)):
                    summat.append([math.sqrt((merlist[j][0]-self.tyhjälist[i][0])**2+(merlist[j][1]-self.tyhjälist[i][1])**2),i])
            for i in range(len(summat)):
                if 1<summat[i][0]<3:
                    mahdlist.append(self.tyhjälist[summat[i][1]])
            torilist.append(mahdlist[random.randint(0,len(mahdlist)-1)])
            while len(torilist)<=len(self.aluli[20])//2:
                logtie.write('tyhmtor')
                self.tyhjät()
                for i in range(len(self.tyhjälist)):
                    for j in range(len(torilist)):
                        if 4<math.sqrt((torilist[j][0]-self.tyhjälist[i][0])**2+(torilist[j][1]-self.tyhjälist[i][1])**2)<8:
                            mahdlist.append(self.tyhjälist[i])
                torilist.append(mahdlist[random.randint(0,len(mahdlist)-1)])
            for i in range(len(torilist)):
                self.kartta[torilist[i][0]][torilist[i][1]] = self.aluli[20][0]
                self.aluli[20].pop()            
                                    
                     
    def ryhm(self):
        logtie.write('ryhm\n')
        alklist=[]
        x, y = self.suuntval()
        self.todmatputs()
        tyyp = self.tyyppi()
        lask = 0
        escape=0
        while laske(self.aluli) != 0:
            if self.aluli[tyyp]==[]:tyyp = self.tyyppi(tyyp)
            if tyyp == 40 or tyyp == 26:## Tarkistetaan vaatiiko aluetyyppi merta
                if self.onkomer(x, y, 99):
                    pass
                else:
                    while not self.onkomer(x, y, 99):
                        x, y = self.suuntval()
            self.kartta[x][y] = self.aluli[tyyp][0]
            self.aluli[tyyp].pop()
            self.todmatputs()
            x, y = self.suuntval(x, y)
            typi = self.ympär(x, y, tyyp)
            if typi == 99: tyyp = 40
            elif typi == 98: tyyp = 26
            else:tyyp = self.tyyppi(typi)
            if tyyp == -3:
                break
            lask = lask +1
            if lask == 6+random.randint(0,4):
                x, y = self.suuntval()
            escape=escape+1
            if escape==1000:
                logtie.write('esc')
                escape=0
                x,y = self.suuntval()
                

    def todmatputs(self):
        logtie.write('todmatputs\n')
        for i in range(len(self.aluli)):
            if len(self.aluli[i])== 0:
                for j in range(len(self.tarktodmat)):
                    self.tarktodmat[j][i] = 0
                                   
    def tyyppi(self, a=-1):
        logtie.write(str(a)+'tyyppi\n')
        if a == -1 or a >41:
            for i in range(len(self.aluli)):
                if len(self.aluli[i])>0:
                    tyyp = i
                    break
        elif sum(self.tarktodmat[a]) == 0:
            b = 0
            for i in range(len(self.tarktodmat)):
                b = sum(self.tarktodmat[i])
            if b == 0: return -3      
            for i in range(len(self.aluli)):
                if len(self.aluli[i])>0:
                    tyyp = i
                    break
        else: tyyp = a
        todyht = sum(self.tarktodmat[tyyp])
        todnäk = random.randint(1,todyht)
        for i in range(len(self.tarktodmat[tyyp])):
            if todnäk <= sum(self.tarktodmat[tyyp][:i+1]):
                typo = i
                return typo
            
    def suuntvalmer(self, xa=-1, ya=-1):
        logtie.write(str(xa)+str(ya)+'suuntvalmer\n')
        xm = self.xkok-1
        ym = self.ykok-1
        test = []
        tesran=random.randint(2,25)
        for i in range(tesran):
            for j in range(tesran):
                if abs(math.sqrt((i-xa)**2+(j-ya)**2))<math.sqrt(tesran):test.append([i,j])
        return test
     
    def onkomer(self, xa=-1, ya=-1, aa=99):
        logtie.write(str(xa)+str(ya)+str(aa)+'onkomer\n')
        self.karli()
        tutkilist =[]
        test=[]
        for i in range(len(self.karttalist)):
            if self.karttalist[i][2].tyyppinum == aa:
                tutkilist.append([self.karttalist[i][0],self.karttalist[i][1]])
        for i in range(len(tutkilist)):
            if math.sqrt((tutkilist[i][0]-xa)**2+(tutkilist[i][1]-ya)**2)<2:
                test.append(tutkilist[i])
        if test == []: return False
        else: return True 
        
        
          
                    
    def suuntval(self, xa=-1, ya=-1):
        luk = luk+1
        logtie.write(str(xa)+str(ya)+'kert:'+str(luk)+'  '+'suuntval\n')
        xm = self.xkok-1
        ym = self.ykok-1
        valmat = []
        alklist=[]
        if xa == -1:
            self.karli()
            self.tyhjät()
            test = []
            logtie.write('tyhmäsuuntval')
            for i in range(len(self.karttalist)):
                if self.karttalist[i][2].tyyppinum == 20 and self.ympärtyh(self.karttalist[i][0],self.karttalist[i][1]):
                    alklist.append([self.karttalist[i][0],self.karttalist[i][1]])
            if alklist==[]:
                s =random.randint(0, len(self.tyhjälist)-1)
                return self.tyhjälist[s][0],self.tyhjälist[s][1]
            xa,ya = alklist[0]
            for i in range(len(self.tyhjälist)):
                if math.sqrt((self.tyhjälist[i][0]-xa)**2+(self.tyhjälist[i][1]-ya)**2)<=7:
                    test.append(self.tyhjälist[i])
            if test == []:
                test.append(self.tyhjälist[random.randint(0, len(self.tyhjälist)-1)])
            valmat = test
            if len(valmat)<=1: a = 0
            else: a = random.randint(0, len(valmat)-1)
            return valmat[a][0], valmat[a][1]
        if xa+1 < xm:
            if self.kartta[xa+1][ya] == []:
                valmat.append([xa+1, ya])
        if xa-1 >= 0:
            if self.kartta[xa-1][ya] == []:
                valmat.append([xa-1, ya])
        if ya+1 < ym:
            if self.kartta[xa][ya+1] == []:
                valmat.append([xa, ya+1])
        if ya-1 >= 0:
            if self.kartta[xa][ya-1] == []:
                valmat.append([xa, ya-1])
        if valmat == []:
            self.tyhjät()
            test = []
            for i in range(len(self.tyhjälist)):
                if math.sqrt((self.tyhjälist[i][0]-xa)**2+(self.tyhjälist[i][1]-ya)**2)<12:
                    test.append(self.tyhjälist[i])
            if test == []:
                test.append(self.tyhjälist[random.randint(0, len(self.tyhjälist)-1)])
            valmat = test
        if len(valmat)<=1: a = 0
        else: a = random.randint(0, len(valmat)-1)
        return valmat[a][0], valmat[a][1]

    def ympär(self, xa, ya, typ):
        logtie.write('ympär\n')
        xm = self.xkok-1
        ym = self.ykok-1
        typmat = []
        if xa+1 < xm:
            if self.kartta[xa+1][ya] != []:
                typmat.append(self.kartta[xa+1][ya].tyyppinum)
            if ya-1 >= 0:
                if self.kartta[xa+1][ya-1] != []:
                    typmat.append(self.kartta[xa+1][ya-1].tyyppinum)
            if ya+1 < ym:
                if self.kartta[xa+1][ya-1] != []:
                    typmat.append(self.kartta[xa+1][ya-1].tyyppinum)
        if xa-1 >= 0:
            if self.kartta[xa-1][ya] != []:
                typmat.append(self.kartta[xa-1][ya].tyyppinum)
            if ya-1 >= 0:
                if self.kartta[xa-1][ya-1] != []:
                    typmat.append(self.kartta[xa-1][ya-1].tyyppinum)
            if ya+1 < ym:
                if self.kartta[xa-1][ya+1] != []:
                    typmat.append(self.kartta[xa-1][ya+1].tyyppinum)
        if ya+1 < ym:
            if self.kartta[xa][ya+1] != []:
                typmat.append(self.kartta[xa][ya+1].tyyppinum)
            if xa-1 >= 0:
                if self.kartta[xa-1][ya+1] != []:
                    typmat.append(self.kartta[xa-1][ya+1].tyyppinum)
            if xa+1 < xm:
                if self.kartta[xa+1][ya+1] != []:
                    typmat.append(self.kartta[xa+1][ya+1].tyyppinum)
        if ya-1 >= 0:
            if self.kartta[xa][ya-1] != []:
                typmat.append(self.kartta[xa][ya-1].tyyppinum)
            if xa-1 >= 0:
                if self.kartta[xa-1][ya-1] != []:
                    typmat.append(self.kartta[xa-1][ya-1].tyyppinum)
            if xa+1 < xm:
                if self.kartta[xa+1][ya-1] != []:
                    typmat.append(self.kartta[xa+1][ya-1].tyyppinum)
        if len(typmat) == 0: return typ
        else:
            typmat.reverse()
            mertes = []
            for i in range(len(typmat)):
                if typmat[i] == 99:
                    mertes.append(i)
                    if self.aluli[40] != 0:
                        return 99
                    if self.aluli[26] != 0:
                        return 98
            while mertes !=[]:        
               typmat.remove(99)
               mertes.pop()           
        return typmat[0]
    
    def ympärtyh(self, xa, ya):
        logtie.write('ympärtyh\n')
        xm = self.xkok-1
        ym = self.ykok-1
        typmat = []
        if xa+1 < xm:
            if self.kartta[xa+1][ya] != []:
                typmat.append(1)
            if ya-1 >= 0:
                if self.kartta[xa+1][ya-1] != []:
                    typmat.append(1)
            if ya+1 < ym:
                if self.kartta[xa+1][ya-1] != []:
                    typmat.append(1)
        if xa-1 >= 0:
            if self.kartta[xa-1][ya] != []:
                typmat.append(1)
            if ya-1 >= 0:
                if self.kartta[xa-1][ya-1] != []:
                    typmat.append(1)
            if ya+1 < ym:
                if self.kartta[xa-1][ya+1] != []:
                    typmat.append(1)
        if ya+1 < ym:
            if self.kartta[xa][ya+1] != []:
                typmat.append(1)
            if xa-1 >= 0:
                if self.kartta[xa-1][ya+1] != []:
                    typmat.append(1)
            if xa+1 < xm:
                if self.kartta[xa+1][ya+1] != []:
                    typmat.append(1)
        if ya-1 >= 0:
            if self.kartta[xa][ya-1] != []:
                typmat.append(1)
            if xa-1 >= 0:
                if self.kartta[xa-1][ya-1] != []:
                    typmat.append(1)
            if xa+1 < xm:
                if self.kartta[xa+1][ya-1] != []:
                    typmat.append(1)
        if len(typmat) == 12: return False
        else: return True

    def tulosta(self):
        logtie.write('tulosta\n')
        kuali = []
        koali = []
        sir = ""
        for g in range(len(self.kartta)):
            for h in range(len(self.kartta[g])):
                if self.kartta[g][h] != []:
                    kuali.append(self.kartta[g][h].tyyppinum)
                    kuali.sort()
        for i in range(41):
            koali.append(kuali.count(i))
    
        for i in range(len(koali)):
            sir = sir+str(self.kaup.osadata.aluenimet[i])+": "+str(koali[i])+"\n"
        sr = ''
        for i in range(len(self.kartta)):
            for j in range(len(self.kartta[i])):
                if self.kartta[i][j] != []:
                    sr=sr + str(self.kartta[i][j].tyyppinum).zfill(2)+' '
                else:
                    sr= sr +'**'+' '
            sr= sr +"\n"
        ser = str(sr)
        tulos = [ser, sir]
        return tulos
    
def suoritus(a):
    logtie.write('suoritus\n')
    kaupunki = Kaupunki('kaup',a)
    b = Kartta(kaupunki)
    print(b.tulosta()[0],b.tulosta()[1])
    sar='kaupa.txt'
    kaupkartteks =open(sar, 'w')
    kaupkartteks.write(b.tulosta()[0])
    return kaupunki, b

def tutki(kaupma):
    mapp = kaupma[1]
    x=0
    while x != -1:
        print('Anna x')
        x = int(input())
        print('Anna y')
        y = int(input())
        if x > mapp.xkok or y > mapp.xkok:
            print('Ulkona')
            pass
        elif mapp.kartta[x][y] == []:
            print('Tyhjä')
            pass
        else:print(mapp.kartta[x][y].tyyppi,mapp.kartta[x][y].nimi)
        
log='log.txt'
logtie=open(log, 'w')
global luk
luk = 0
for i in range(1):
    suoritus(6)
    