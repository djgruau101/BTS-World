'''This program is an ARMY's best friend'''

from math import ceil
import time
from datetime import datetime
from random import shuffle
import gc

statsnames = ['Empathy', 'Passion', 'Stamina', 'Wisdom']
statssymbols = ['♥', '☼', 'ϟ', '♪']

class member(object):
    '''A BTS member.'''
    def __init__(self, name, abr, line):
        self._name = name
        self.cards = list()
        self.__abr = abr
        self.__rollcalled = False
        self.rollcallstat = 0
        self.rollcallboost = 0
        if line.casefold() in ['hyung', 'maknae']:
            self.__line = line.casefold().capitalize()
        else:
            raise ValueError('Either hyung or maknae')
        
    def __repr__(self):
        return 'member(' + self._name + ')'
    
    def __str__(self):
        return self._name

    def getAbr(self):
        return self.__abr

    def getLine(self):
        return self.__line
    
    def showCards(self, function='f'):
        '''Shows the list of collected cards.'''
        longest_length = max([len(c.name + ':') for c in self.cards])
        fmt = '{:' + str(longest_length) + 's}'
        n = 1
        for card in self.cards:
            s = card.getStrengthSymbol() + "  " + fmt.format(card.name + ':') + ' LV ' + str(card.level)
            if function == 'm':
                if card.level >= 10:
                    s += ' (' + str(n) + ')'
                else:
                    s += '  (' + str(n) + ')' #alternative to formatted printing because I'm lazy
                n += 1
            print(s)
            
    def nbCards(self):
        '''Returns the number of cards collected.'''
        return len(self.cards)

    def hasCard(self, cardname, stars):
        '''Checks if member already has a card of the given name and stars.'''
        if cardname in [c.name for c in self.cards]:
            dupeindex = [c.name for c in self.cards].index(cardname)
            dupecard = self.cards[dupeindex]
            if dupecard._stars == stars:
                return True
        return False
        
    def addCard(self):
        '''Appends a card on the text file.'''
        rep = 'yes' #declare variable
        while rep == 'yes':
            if self.rollCalled():
                print("Make sure to input pre-boost stats!!!")
            n = input('Name: ') #string
            s = input('Number of stars: ') #number from 1 to 5
            if not (s in [str(n) for n in range(1,6)]):
                raise ValueError('Star number must be an integer from 1 to 5.')
            if self.hasCard(n, int(s)):
                print('Duplicate card.')
                break
            e1 = int(input('Empathy: ')) #MUST BE INTEGERS
            p1 = int(input('Passion: '))
            s1 = int(input('Stamina: '))
            w1 = int(input('Wisdom: '))
            nb = input('Strong stat: Empathy (1), Passion (2), Stamina (3), Wisdom (4): ')
            if int(nb) not in range(1,5):
                raise IndexError("Invalid number.")
            strength = statsnames[int(nb) - 1]
            lvl = int(input('Level: '))
            if int(s) in [1,2]:
                if not lvl in range(1,31):
                    raise ValueError("Level must be between 1 and 30 for 1* and 2* cards.")
            elif int(s) in [3,4,5]:
                maxlevel = 50
                t2 = False
                for name in card.tier2list:
                    if n.startswith(name):
                        t2 = True
                        maxlevel = 60
                        break
                if not t2 and lvl in range(51,61):
                    raise ValueError("Not a tier 2 card. Max level is 50.")
                if not lvl in range(1, maxlevel+1):
                    raise ValueError("Level must be between 1 and {} for this card.".format(maxlevel))
            print()
            print('Member:', self._name)
            print('Name:', n)
            print(s + '*')
            print('Empathy:', e1)
            print('Passion:', p1)
            print('Stamina:', s1)
            print('Wisdom:', w1)
            print('Strong stat: ' + strength)
            print('Level', lvl)
            confirm = input('Confirm: (yes): ')
            if confirm.casefold() == 'yes':
                if n in [c.name for c in cards]: #if duplicate
                    print("Same card name as another member's.")
                    n = self.__abr + n
                line = '\n' + self._name + '; ' + n + '; ' + s + '; ' + str(e1) + '; ' + str(p1) + '; ' + str(s1) + '; ' +  str(w1) + '; ' + strength
                if lvl > 1:
                    line += '; ' + str(lvl)
                card_info = line.strip().split('; ')
                cards_info.append(card_info)
                if lvl == 1:
                    newcard = card(card_info[0], card_info[1], int(card_info[2]), int(card_info[3]), int(card_info[4]), int(card_info[5]), int(card_info[6]), card_info[7])
                else:
                    newcard = card(card_info[0], card_info[1], int(card_info[2]), int(card_info[3]), int(card_info[4]), int(card_info[5]), int(card_info[6]), card_info[7], int(card_info[8]))
                file = open(filename, 'a')
                file.write(line)
                file.close()
                i = membernames.index(self._name) #find index
                members[i].attachCard(newcard) #add card to member object
                cards.append(newcard) #add card to the global cards
                print('New card added.\n')
                rep = input('Add another card for ' + self._name + '?\(y)es, (n)o: ')
            else:
                break
            
    def attachCard(self, card):
        '''Attach card from text file to the instance.'''
        self.cards.append(card)
        
    def removeCard(self):
        '''Removes a card from a member.'''
        self.showCards('m')
        print()
        c = int(input('Type the number of a card to remove it: ')) - 1
        self.cards.pop(c)
        cards.pop(c)
        print('Card removed.')

    def manageCards(self):
        options = ['s', 'sl', 'l', 'u', 'c', 'q']
        action = 'c' #declare variable
        while action == 'c':
            print('Choose card:\n')
            self.showCards('m')
            i = input('\nType a number or card name: ')
            if i.isdigit():
                if int(i) in range(1, self.nbCards()+1):
                    i = int(i) - 1 #for indexing
                    c = self.cards[i] #card object
            elif i in [c.name for c in self.cards]:
                c = self.cards[[c.name for c in self.cards].index(i)]
            else:
                break
            print()
            print('Card:', c)
            while action != 'q':
                print()
                action = input('Show stats (s), set level (sl), level up (l), undo level up (u), choose another card (c) or done (q): ') #most card methods will be used here
                print()
                if action in options:
                    if action == 's':
                        c.profile()
                    elif action == 'sl':
                        level = input('Set level: ')
                        if level == "max":
                            c.setMax()
                        else:
                            c.setLevel(int(level))
                    elif action == 'l':
                        c.levelUp()
                    elif action == 'u':
                        c.undoLevelUp()
                    elif action == 'c':
                        break
                else:
                    print('Invalid input')

    def rollCall(self, stat, boost):
        '''October 2019 update: the stat value for the cards of one member gets boosted for one day.'''
        if self.__rollcalled:
            self.undoRollCall() # reset, change roll call
        if boost in [100, 200, 400, 1.03, 1.05, 1.1]:
            self.rollcallboost = boost
        else:
            raise ValueError("Boost value does not exist.")
        if stat in range(1, 5):
            for card in self.cards: # cards are mutable so it's great
                if isinstance(boost,float):
                    number = card._statsnbs[stat-1] * boost
                    if number%1 > 0.99999: # because Python bs
                        number = int(number)+1
                    else:
                        number = int(number)
                    card._statsnbs[stat-1] = number
                else:
                    card._statsnbs[stat-1] = card._statsnbs[stat-1] + boost
        elif stat == 5: #all stats get boosted
            for card in self.cards:
                if isinstance(boost,float):
                    card._statsnbs = [nb*boost for nb in card._statsnbs]
                    for i in range(len(card._statsnbs)):
                        if card._statsnbs[i]%1>0.99999:
                            card._statsnbs[i] = int(card._statsnbs[i])+1
                        else:
                            card._statsnbs[i] = int(card._statsnbs[i])
                else:
                    card._statsnbs = [nb+boost for nb in card._statsnbs]
        else:
            raise ValueError('Stat value must be between 1 and 4.')
        self.__rollcalled = True
        self.rollcallstat = stat

    def undoRollCall(self):
        if self.rollCalled():
            for card in self.cards:
                card.undoRollCall()
            self.__rollcalled = False
            self.rollcallstat = 0
            self.rollcallboost = 0
            
    def rollCalled(self):
        return self.__rollcalled
        
class card(object):
    tier2list = ["Dreamland ", "Red Carpet ",
                "Boy of Summer ", "Boy In Luv ",
                "Let's Do This ", "Romantic ",
                "DOPE ", "FAKE LOVE ", "Autumn Snap ",
                 "Winter Wonderland "]
    def __init__(self, member, name, stars, empathy, passion, stamina, wisdom, strength, level=1):
        self.member = member
        self.name = name
        self.level = level
        self._stars = stars #a number from 1 to 5
        self.isTier2 = False
        if self._stars in [1,2]:
            self.__max = 30
        elif self._stars in [3,4,5]:
            self.__max = 50
            if self._stars == 5:
                for suit in card.tier2list:
                    if self.name.startswith(suit):
                        self.isTier2 = True
                        self.__max = 60
                        break
        ups = [16, 20, 23, 26, 30]
        strongups = [24, 30, 35, 39, 45] #*3/2 factor (not exactly)
        self.up = ups[self._stars - 1] #weak stats increment by this much after level up
        self.strongup = strongups[self._stars - 1] #strong stat increments by this much after level up
        self.__norcempathy = empathy # for resetting roll call
        self.__norcpassion = passion
        self.__norcstamina = stamina
        self.__norcwisdom = wisdom
        self.__empathy = self.__norcempathy
        self.__passion = self.__norcpassion
        self.__stamina = self.__norcstamina
        self.__wisdom = self.__norcwisdom
        self._statsnbs = [self.__empathy, self.__passion, self.__stamina, self.__wisdom]
        # No rc stats
        self._norcstatsnbs = [self.__norcempathy, self.__norcpassion, self.__norcstamina, self.__norcwisdom]
        self.__strength = strength #strong stat: not necessarily the strongest at level 1
        self.__strongsymbol = statssymbols[statsnames.index(strength)]
        self.__statnamenb = dict(zip(statsnames, self._statsnbs))

    def __repr__(self):
        return 'card' + str((self.member, self.name, self._stars,
                             self.__empathy, self.__passion, self.__stamina, self.__wisdom,
                             self.getStrength(), self.level))
    
    def __str__(self):
        '''Name of the card.'''
        return self.name

    def copy(self):
        return self

    def undoRollCall(self):
        self.__empathy = self.__norcempathy
        self.__passion = self.__norcpassion
        self.__stamina = self.__norcstamina
        self.__wisdom = self.__norcwisdom
        self._statsnbs = [self.__empathy, self.__passion, self.__stamina, self.__wisdom]
        self.__statnamenb = dict(zip(statsnames, self._statsnbs))
    
    def profile(self):
        '''Shows name, *, level and stats of a card.'''
        print('Name: ' + self.name)
        print(str(self._stars) + '*')
        print('LV', self.level)
        for name, nb in zip(statsnames, self._statsnbs):
            if name == self.getStrength():
                name = name.upper()
            print(name, nb, sep=': ')

    def strongestStats(self):
        self.__statnamenb
        print(self.getStrength() + ', ' + 'f')

    def getStrength(self):
        return self.__strength

    def getStrengthSymbol(self):
        return self.__strongsymbol

    def __changeStats(self, levelchange):
        '''Sets stats based on level. Called after self.level changes.'''
        i = statsnames.index(self.getStrength())
        self.statsnbs_initial = self._norcstatsnbs.copy() #store initial values (for print statement at the end)
        for n in range(len(self._statsnbs)):
            if n == i: # strong stat
                self._norcstatsnbs[n] += (levelchange)*self.strongup
            else:
                self._norcstatsnbs[n] += (levelchange)*self.up
        self.__norcempathy, self.__norcpassion, self.__norcstamina, self.__norcwisdom = self._norcstatsnbs
        self._statsnbs = self._norcstatsnbs.copy()
        BTSmember = members[[m._name for m in members].index(self.member)]
        if BTSmember.rollCalled():
            if BTSmember.rollcallstat in range(1, 5):
                if BTSmember.rollcallboost >= 100:
                    self._statsnbs[BTSmember.rollcallstat-1] += BTSmember.rollcallboost
                else:
                    number = self._statsnbs[BTSmember.rollcallstat-1]*BTSmember.rollcallboost
                    if number%1>0.99999:
                        number = int(number)+1
                    else:
                        number = int(number)
                    self._statsnbs[BTSmember.rollcallstat-1] = number
            else: # 5: all stats
                if BTSmember.rollcallboost >= 100:
                    for n in range(4):
                        self._statsnbs[n] += BTSmember.rollcallboost
                else:
                    self._statsnbs = [s*BTSmember.rollcallboost for s in self._statsnbs]
                    for n in range(4):
                        number = self._statsnbs[n]
                        if number%1>0.99999:
                            number = int(number)+1
                        else:
                            number = int(number)
                    self._statsnbs[n] = number

    def __updateCardsInfo(self):
        '''For updating text file contents.'''
        l = [self.member, self.name, str(self._stars), self.__norcempathy, self.__norcpassion, self.__norcstamina, self.__norcwisdom, self.getStrength(), str(self.level)]
        line = '; '.join([str(field) for field in l])
        member_name_stars = [info[:3] for info in cards_info] #member, name, stars
        info_index = member_name_stars.index(l[:3])
        cards_info[info_index] = l #replace 
    
    def setLevel(self, level):
        '''Set a card to a certain level.'''
        if isinstance(level, int) and 0 < level <= self.__max:
            current_level = self.level #initial
            self.level = level #update
            level_increment = self.level - current_level
            if level_increment == 0:
                print("Level did not change!")
                return
            ### changing stats
            self.__changeStats(level_increment)
            if level_increment > 0:
                print('Level up! ' + str(current_level) + ' → ' + str(self.level) + '\n')
            elif level_increment < 0:
                print('Card set to level ' + str(self.level) + '.\n' + str(current_level) + ' → ' + str(self.level))
            init = list()
            g = list()
            for name,i in zip(statsnames, self.statsnbs_initial):
                gain = self.up*level_increment
                if name == self.getStrength():
                    gain = self.strongup*level_increment #effect on number of characters
                init.append(len(str(i)))
                g.append(len(str(gain)))
            fmt1 = '{:' + str(max(init)) + 's}'
            fmt2 = '{:' + str(max(g)) + 's}'
            for name,i,f in zip(statsnames, self.statsnbs_initial, self._norcstatsnbs):
                gain = self.up*level_increment
                if name == self.getStrength():
                    name = name.upper()
                    gain = self.strongup*level_increment
                if level_increment > 0:
                    print('{:7s}'.format(name) + ': ' + fmt1.format(str(i)) + '+' + fmt2.format(str(gain)) + ' → ' + str(f)) #'wisdom' is shorter than all other stat names
                else:
                    print('{:7s}'.format(name) + ': ' + fmt1.format(str(i)) + fmt2.format(str(gain)) + ' → ' + str(f)) #gain is a negative number
            self.__updateCardsInfo()
            updateCardsLevel(filename)
            #print("\nDon't forget to updateCardsLevel('" + filename + "')")
        elif level > self.__max:
            print('Max level is', str(self.__max))
        else:
            print('Invalid input')
        
    def levelUp(self):
        '''Level increment = +1'''
        self.setLevel(self.level + 1)
        
    def undoLevelUp(self):
        '''Only if levelled up by mistake.'''
        if self.level != 1:
            self.setLevel(self.level - 1)

    def setMax(self):
        self.setLevel(self.__max)
            
### MAIN PROGRAM ################################################## 
#BTS members
RM = member('RM', 'RM', 'hyung')
Jin = member('Jin', 'SJ', 'hyung')
SG = member('Suga', 'SG', 'hyung')
JH = member('J-Hope', 'JH', 'hyung')
JM = member('Jimin', 'JM', 'maknae')
V = member('V', 'V', 'maknae')
JK = member('Jungkook', 'JK', 'maknae')
members = [RM, Jin, SG, JH, JM, V, JK] #list of member objects
membernames = [artist._name for artist in members] #list of members' names as str
cards_info = list() #the contents of the text file are stored there
norollcallcards = list()
cards = list()

player = input("Player: ")
filename = 'BTS_World_' + player + '.txt'
fp = open(filename)
print("Hi " + player + "!")
rcOps = ['y','n']
rc = input("Roll call? (y)es, (n)o ").casefold()

### GROUP STATS ###
groupstatslevel = [int(n) for n in fp.readline().strip().split(", ")]
if not all([n in range(1,81) for n in groupstatslevel]):
    raise ValueError("At least one group stat is not an integer between 1 and 80.")
groupstatspoints = [(n-1)*13+100 if n<50 else (n-1)*13+103 for n in groupstatslevel]
statname_statnb = dict(zip(statsnames, groupstatspoints))
####################

## TO REWORK ON
def levelUpStat(n):
    '''1: Empathy, 2: Passion, 3: Stamina, 4: Wisdom'''
    s = statsnames[n-1]
    groupstatslevel[statsnames.index(s)] += 1
    if groupstatslevel[statsnames.index(s)] == 50: # level up from 49 to 50
        statname_statnb[s] += 3
    statname_statnb[s] += 13
    gr = open("BTS_World_" + player + ".txt", 'w')
    gr.write(str(groupstatslevel)[1:-1]+'\n')
    for l in cards_info: # stat numbers come before cards in the same text file
        line = "; ".join([str(field) for field in l])
        if l != cards_info[-1]:
            gr.write(line + '\n')
        else:
            gr.write(line)
    gr.close()
    for item in zip(statsnames, groupstatslevel):
        print(item[0], item[1], sep=": level ")

def undoLevelUpStat(n):
    '''1: Empathy, 2: Passion, 3: Stamina, 4: Wisdom'''
    s = statsnames[n-1]
    groupstatslevel[statsnames.index(s)] -= 1
    if groupstatslevel[statsnames.index(s)] == 49: # level up from 50 to 49
        statname_statnb[s] -= 3
    statname_statnb[s] -= 13
    gr = open("BTS_World_" + player + ".txt", 'w')
    gr.write(str(groupstatslevel)[1:-1]+'\n')
    for l in cards_info: # stat numbers come before cards in the same text file
        line = "; ".join([str(field) for field in l])
        if l != cards_info[-1]:
            gr.write(line + '\n')
        else:
            gr.write(line)
    gr.close()
    for item in zip(statsnames, groupstatslevel):
        print(item[0], item[1], sep=": level ")

#process all cards from the text file
for line in fp:
    card_info = line.strip().split('; ')
    if card_info[0] in membernames:
        i = membernames.index(card_info[0]) #find index
        mb, name, stars, empathy, passion, stamina, wisdom, strength = card_info[:8] #without including level
        if len(card_info) == 9: #if level is indicated. Otherwise level 1
            level = int(card_info[-1])
        else:
            level = 1 #default level
        members[i].attachCard(card(mb, name, int(stars), int(empathy), int(passion), int(stamina), int(wisdom), strength, level))
        cards_info.append(card_info)
        
### ROLL CALL ###
def BTSrollCall(stat, boost): # if all members get called
    for m in members:
        m.rollCall(stat, boost)

def newRollCall(BTSmember, stat, boost):
    rcmessage = str()
    if BTSmember not in [m.getAbr() for m in members]+[m._name for m in members]+["BTS"]:
        raise ValueError("{} is not a BTS member!".format(BTSmember))
    if stat not in range(1, 6):
        raise ValueError("Invalid stat.")
    if boost not in [100, 200, 400, 1.03, 1.05, 1.1]:
        message = " is not a boost value."
        if boost < 100:
            message = '%'+message    
        raise ValueError("+{}".format(boost) + message)
    if BTSmember != "BTS":
        for m in members:
            m.undoRollCall()
        if BTSmember in [m.getAbr() for m in members]:
            rcmember = members[[m.getAbr() for m in members].index(BTSmember)]
        else:
            rcmember = members[[m._name for m in members].index(BTSmember)]
        rcmessage += (rcmember._name + ": ")
        rcmember.rollCall(stat, boost)
    else:
        rcmessage += "BTS: "
        BTSrollCall(stat, boost)
    if stat in range(1, 5):
        rcmessage += (statsnames[stat-1]+" +")
    else:
        rcmessage += "All stats +"
    if boost >= 100:
        rcmessage += str(boost)
    else:
        boost_text = {1.03: "3%", 1.05: "5%", 1.1: "10%"}
        rcmessage += boost_text[boost]
    rc = 'y'
    print(rcmessage)

def removeRollCall():
    for m in members:
        m.undoRollCall()
    rc = 'n'

if rc in rcOps:
    while rc == 'y':
        message = "Select roll call member:\n"
        for m in members:
            message += (m._name + " (" + str(members.index(m)+1) + "), ")
        message += "BTS (8)\n"
        memberindex = input(message)
        if memberindex not in [str(n) for n in range(1, 9)]:
            rc = 'n'
            break
        statindex = input("Roll call stat:\nEmpathy (1), Passion (2), Stamina (3), Wisdom (4), All stats (5)\n")
        if statindex not in [str(n) for n in range(1, 6)]:
            rc = 'n'
            break
        rollCallStat = int(statindex)
        boostindex = input("Roll call boost:\n+100 (1), +200 (2), +400 (3), +3% (4), +5% (5), +10% (6)\n")
        if boostindex not in [str(n) for n in range(1, 7)]:
            rc = 'n'
            break
        rollCallBoost = [100, 200, 400, 1.03, 1.05, 1.1][int(boostindex)-1]
        rollCallMessage = str()
        if int(memberindex) != 8:
            rollCallMember = members[int(memberindex)-1]
            rollCallMember.rollCall(rollCallStat, rollCallBoost)
            rollCallMessage = rollCallMember._name + ": "
        else:
            BTSrollCall(rollCallStat, rollCallBoost)
            rollCallMessage = "BTS: "
        if rollCallStat != 5:
            rollCallMessage += (statsnames[rollCallStat-1] + " ")
        else:
            rollCallMessage += "All stats "
        rollCallMessage += ["+100", "+200", "+400", "+3%", "+5%", "+10%"][int(boostindex)-1]
        print(rollCallMessage)
        break
else:
    raise ValueError("Invalid input.")

#################
for lst_c in [m.cards for m in members]:
    cards += lst_c
fp.close()

# PRINT GROUP STATS LEVELS
print()
for item in zip(statsnames, groupstatslevel):
    print(item[0], item[1], sep=": level ")

print(len(cards), 'cards\n')

def updateCardsLevel(file):
    '''Replace cards in text file by the same cards of a different level.'''
    fp = open(file, 'w')
    fp.write(str(groupstatslevel)[1:-1]+"\n")
    for l in cards_info:
        line = "; ".join([str(field) for field in l])
        if l != cards_info[-1]:
            fp.write(line + '\n')
        else:
            fp.write(line)
    fp.close()

### mission class only implemented here because it needs to use cards (global)
class mission(object):
    '''Abstract class. Indicate required stats as follows: Empathy = 1, passion = 2, stamina = 3, wisdom = 4.'''
    __moves = cards
    def __init__(self, reqst1, reqst2=None):
        if reqst1 == reqst2:
            raise ValueError('The two required stats must be different.')
        self.__reqst1 = statsnames[reqst1 - 1] #Name of required stat 1
        self.__boostvalues = [1,1,1,1]
        self.__reqst2 = None #declare variable
        self.__weakstatsnames = statsnames.copy()
        self.__weakstatsnames.remove(self.__reqst1)
        if reqst2:
            self.__reqst2 = statsnames[reqst2 - 1] #Name of required stat 2 if it exists
            self.__weakstatsnames.remove(self.__reqst2)
            self.__nonreq1 = self.__weakstatsnames[0]
            self.__nonreq2 = self.__weakstatsnames[1]
        self.__stats_boosts = dict(zip(statsnames, self.__boostvalues))

    def __repr__(self):
        tup = (self.__reqst1, self.__reqst2)
        return 'mission' + str(tup)

    def __str__(self):
        return 'Abstract mission: ' + self.__reqst1 + ' and ' + self.__reqst2

    def copy(self): #mission objects are mutable
        return self

    def getStat1(self):
        return self.__reqst1

    def getStat2(self):
        return self.__reqst2

    def getWeak1(self):
        return self.__nonreq1

    def getWeak2(self):
        return self.__nonreq2

    def getWeakStatsNames(self):
        return self.__weakstatsnames

    def getStatsBoosts(self):
        return self.__stats_boosts

    def getMoves(self):
        return self.__moves

    def points(self, cardname, fct='f'):
        '''Calculates the number of points that a card of name cardname gives.
        fct is either for printing/checking card performance (p) or for returning the number of points (f)
        weak is either 1 (non-required stat 1 is weaker), 2 (non-required stat 2 is weaker) or None (both non-required stats are equally weak).'''
        ### use the dictionary to apply boosts ###
        if cardname not in [c.name for c in self.getMoves()]:
            raise ValueError('Card is not playable or does not exist.')
        i = [c.name for c in self.getMoves()].index(cardname)
        card = self.getMoves()[i] #the card we're working with
        final_statsnbs = card._statsnbs.copy() #I'm still afraid of list mutability
        n = 0
        for boost in self.getStatsBoosts().values():
            result = boost*final_statsnbs[n] # Python behaves weirdly with float multiplication/division
            if result%1>0.99999: # because fuck this shit
                result = int(result)+1
            final_statsnbs[n] = int(result) # if decimal is .0000002 then rounds down
            n += 1
        if fct == 'p':
            print(card.getStrengthSymbol() + " " + card.member + ': ' + str(card._stars) + '*', card.name, 'LV ' + str(card.level), sep=', ')
            print()
            n = 0
            for name, nb_init, boost in zip(statsnames, card._statsnbs, self.getStatsBoosts().values()):
                if name == card.getStrength():
                    name = name.upper()
                init = '{:7s}'.format(name) + ': ' + str(nb_init)
                max_len = max(len(number) for number in [str(n) for n in card._statsnbs])
                maxboost = max(self.getStatsBoosts().values())
                maxboostlen = 0 # declare variable
                if 1 <= maxboost <= 10:
                    maxboostlen = 3
                else: # assume boost < 10000%
                    maxboostlen = 4
                maxboostlen = max(len(number) for number in [str(n) for n in self.getStatsBoosts().values()])
                fmt1 = '{:' + str(max_len) + '}'
                if boost != 1:
                    percentage = boost*100
                    if percentage%1>0.99999:
                        percentage = int(percentage)+1
                    else:
                        percentage = int(percentage)
                    init = '{:7s}'.format(name) + ': ' + fmt1.format(str(nb_init)) + ' * ' + ('{:'+str(maxboostlen)+'s}').format(str(percentage) + '%') + ' = ' + str(final_statsnbs[n])
                print(init, 'pts')
                n += 1
            print(sum(final_statsnbs), 'pts\n')
        elif fct == 'f':
            return sum(final_statsnbs)
        else:
            raise ValueError('Invalid fct.')

    def solve(self, nbcards, fct='p'): #'p': makes it a void method
        '''Chooses the cards that give the most points for a mission. If fct = f, return the max amount of points.'''
        if fct not in ['p', 'f', 'pn']:
            raise ValueError('Invalid fct.')
        if nbcards < 1:
            raise ValueError("Must play at least 1 card.")
        listofpoints = [self.points(card.name) for card in self.getMoves()]
        card_points = dict(zip(self.getMoves(), listofpoints))
        descending_cards = sorted(card_points.items(), key=lambda x: x[1], reverse=True) #list
        self.__best_cards = descending_cards[:nbcards] #list of tuples: (card object, points)
        self.__calculatePoints(fct)
        if fct == 'f':
            return self.__total

    def __calculatePoints(self, fct='p'):
        self.__total = 0
        for card,points in self.__best_cards:
            if fct == 'p':
                self.points(card.name, 'p')
                print()
            elif fct == 'pn':
                l1 = max([len(c[0].member) for c in self.__best_cards])
                l2 = max([len(c[0].name) for c in self.__best_cards])
                f1 = ('{:' + str(l1) + 's}').format(card.member)
                f2 = ('{:' + str(l2) + 's}').format(card.name)
                print(card.getStrengthSymbol() + f1 + ': ' + str(card._stars) + '*', f2, 'LV ' + '{:2s}'.format(str(card.level)) + '\n', sep=', ')
            self.__total += points
        if fct == 'p':
            print('Total (without group stats):', self.__total, 'pts\n')
        self.__total += self.groupStatsPts(fct)
        if fct in ['p', 'pn']:
            print('TOTAL: ', self.__total, 'pts')

    def groupStatsPts(self, fct='p'):
        if fct=='p':
            print('GROUP STATS:\n')
        groupstats = statname_statnb.copy() #dictionary
        for stat,boost in self.getStatsBoosts().items(): #index 0: get value
            groupstats[stat] = int(groupstats[stat]*boost)
        if fct=='p':
            for statname,init,boost,final in zip(statsnames, statname_statnb.values(), self.getStatsBoosts().values(), groupstats.values()):
                noboost = '{:7s}'.format(statname) + ': ' + str(init)
                if boost != 1:
                    noboost += ' * ' + '{:4s}'.format(str(int(boost*100)) + '%') + ' = ' + str(final)
                noboost += ' pts'
                print(noboost)
        return sum(groupstats.values())

    def solvable(self, required, nbcards, fct='f'):
        if fct not in ['f', 'p']:
            raise ValueError('Invalid fct.')
        if self.solve(nbcards, 'f') >= required:
            if fct == 'p':
                print(str(self) + ' is solvable.')
            else:
                return True
        else:
            if fct == 'p':
                text = str(self) + ' needs ' + str(required - self.solve(nbcards, 'f')) + ' more points.'
                if (required - self.solve(nbcards, 'f') > 1):
                    print(text) #plural
                else:
                    print(text[:-2] + '.') #singular
            else:
                return False

class missionwithchapter(mission):
    '''Abstract class: chapter with mission'''
    def __init__(self, chapter, number, reqst1, reqst2=None):
        self.__chapter = chapter
        self.__number = number
        super().__init__(reqst1, reqst2)

    def __str__(self): #to be overriden
        return 'Abstract mission chapter ' + str(self.__chapter) + ': ' + self.getStat1() + ' and ' + self.getStat2()

    def getChapter(self):
        return self.__chapter

    def getNumber(self):
        return self.__number
       
class bmission(missionwithchapter):
    '''BTS Story mission chapter 1-7. Indicate required stats and weakest stat as follows: Empathy = 1, passion = 2, stamina = 3, wisdom = 4.'''
    def __init__(self, chapter, number, reqst1, reqst2=None, weak=None):
        if chapter not in range(1,8):
            raise ValueError('Enter a number between 1 and 7.')
        super().__init__(chapter, number, reqst1, reqst2)
        ###
        if self.getChapter() > 1 and not reqst2:
            raise ValueError('Chapters 2 and above have two required stats.')
        self.__boostvalues = [1,1,1,1]
        if self.getChapter() in [1,2,4,6]: #handicaps are equal
            if self.getChapter() == 1:
                self.__boostvalues[reqst1-1] = 1.8
                if reqst2:
                    self.__boostvalues[reqst1-1] = 1.5
                    self.__boostvalues[reqst2-1] = 1.5
            elif self.getChapter() == 2:
                self.__boostvalues[reqst1-1] = 1.8
                self.__boostvalues[reqst2-1] = 1.5
                self.__boostvalues[statsnames.index(self.getWeak1())] = 0.5
                self.__boostvalues[statsnames.index(self.getWeak2())] = 0.5
            elif self.getChapter() in [4,6]:
                self.__boostvalues[reqst1-1] = 2
                self.__boostvalues[reqst2-1] = 1.5
                self.__boostvalues[statsnames.index(self.getWeak1())] = 0.5
                self.__boostvalues[statsnames.index(self.getWeak2())] = 0.5
        else:
            if not weak:
                raise ValueError("The two weak stats have different handicap values.")
            if statsnames[weak-1] not in [self.getWeak1(), self.getWeak2()]:
                raise ValueError("The weakest stat cannot be a strong stat.")
            rem = list(range(1,5))
            if self.getChapter() == 3:
                handicaps = [0.5, 0.8]
                self.__boostvalues[reqst1-1] = 1.8
                self.__boostvalues[reqst2-1] = 1.5
            elif self.getChapter() == 5:
                handicaps = [0.3, 0.7]
                self.__boostvalues[reqst1-1] = 2
                self.__boostvalues[reqst2-1] = 1.5
            elif self.getChapter() == 7:
                handicaps = [0.2, 0.3]
                self.__boostvalues[reqst1-1] = 2.2
                self.__boostvalues[reqst2-1] = 1.8
            self.__boostvalues[weak-1] = handicaps[0]
            for i in [reqst1, reqst2, weak]:
                rem.remove(i)
            self.__boostvalues[rem[0]-1] = handicaps[1]
        self.__stats_boosts = dict(zip(statsnames, self.__boostvalues))
        
    def getStatsBoosts(self): #overriding
        return self.__stats_boosts

    def __str__(self):
        return "BTS Story {}-{}: {} and {}".format(self.getChapter(), self.getNumber(), self.getStat1(), self.getStat2())
        
class amission(missionwithchapter):
    '''Another Story season 1 mission. Indicate required stats and weakest stat as follows: Empathy = 1, passion = 2, stamina = 3, wisdom = 4.
Indicate member as follows: RM (RM), SJ (Jin), SG (Suga), JH (J-Hope), JM (Jimin), V (V), JK (Jungkook).'''
    def __init__(self, member, chapter, number, reqst1, reqst2, weak=None):
        if chapter not in range(1,7):
            raise ValueError('Another Story missions have 6 chapters.')
        if member not in [m.getAbr() for m in members]:
            raise ValueError('Inappropriate member name.')
        self.__member = members[[m.getAbr() for m in members].index(member)]
        self.__moves = self.__member.cards
        super().__init__(chapter, number, reqst1, reqst2)
        self.__boostvalues = [1,1,1,1]
        self.__boostvalues[reqst1-1] = 2
        if self.getChapter() in [1,3,5]: #handicaps are equal
            if self.getChapter() == 1:
                self.__boostvalues[reqst2-1] = 1.5
                self.__boostvalues[statsnames.index(self.getWeak1())] = 0.3
                self.__boostvalues[statsnames.index(self.getWeak2())] = 0.3
            elif self.getChapter() == 3:
                self.__boostvalues[reqst2-1] = 1.8
                self.__boostvalues[statsnames.index(self.getWeak1())] = 0.2
                self.__boostvalues[statsnames.index(self.getWeak2())] = 0.2
            elif self.getChapter() == 5:
                self.__boostvalues[reqst1-1] = 2
                self.__boostvalues[reqst2-1] = 2
                self.__boostvalues[statsnames.index(self.getWeak1())] = 0.1
                self.__boostvalues[statsnames.index(self.getWeak2())] = 0.1
        else:
            if weak==None:
                raise ValueError("The two weak stats have different handicap values.")
            if statsnames[weak-1] not in [self.getWeak1(), self.getWeak2()]:
                raise ValueError("The weakest stat cannot be a strong stat.")
            rem = list(range(1,5))
            if self.getChapter() == 2:
                handicaps = [0.1, 0.3]
                self.__boostvalues[reqst2-1] = 1.7
            elif self.getChapter() == 4:
                handicaps = [0.1, 0.2]
                self.__boostvalues[reqst2-1] = 1.8
            elif self.getChapter() == 6:
                handicaps = [0.05, 0.2]
                self.__boostvalues[reqst2-1] = 2
            self.__boostvalues[weak-1] = handicaps[0]
            for i in [reqst1, reqst2, weak]:
                rem.remove(i)
            self.__boostvalues[rem[0]-1] = handicaps[1]
        self.__stats_boosts = dict(zip(statsnames, self.__boostvalues))

    def __str__(self):
        return self.__member._name + ' Story {}-{}: {} and {}'.format(self.getChapter(), self.getNumber(), self.getStat1(), self.getStat2())

    def getMoves(self):
        return self.__moves

    def getStatsBoosts(self): #overriding
        return self.__stats_boosts

class cmission(mission):
    '''BTS Chapter 8 and above mission: boost factors are different from mission to mission.
Indicate stats from strongest to weakest.
If no criterion, put None or 0.'''
    __moves = cards.copy()
    def __init__(self, chapter, number, st1, st2, st3, st4, mul1, mul2, mul3, mul4, *criteria): #chapter number has no effect on stats: only used for __str__
        self.__chapter = chapter
        self.__number = number
        self.__mul1 = mul1
        self.__mul2 = mul2
        self.__mul3 = mul3
        self.__mul4 = mul4
        self.__boostvalues = [self.__mul1, self.__mul2, self.__mul3, self.__mul4]
        if self.__boostvalues != list(sorted(self.__boostvalues, reverse=True)):
            raise ValueError('Multiplicative values are not entered in descending order.')
        self.__statssorted = [st1, st2, st3, st4] #e.g. [3,2,4,1]
        if sorted(self.__statssorted) != list(range(1,5)):
            raise ValueError('Invalid stat value(s)')
        tuples = sorted(list(zip(self.__statssorted, self.__boostvalues)), key=lambda x: x[0]) #[(1, 0.65), (2, 1.15), (3, 1.7), (4, 0.95)]
        sortedboostvalues = [t[1] for t in tuples] #[0.65, 1.15, 1.7, 0.95]
        self.__stats_boosts = dict(zip(statsnames, sortedboostvalues)) #{'Empathy': 0.65, etc.}
        self.__criteria = () #declare
        if criteria not in [(None,), (0,), ()]:
            self.__criteria = criteria #[[c] for c in criteria]
            self.__criterioncards = list() #contains list(s) of criterion cards
            for c in self.__criteria:
                if c in [m.getAbr() for m in members] or c in range(1,5): #single criterion
                    critstatcards = list()
                    if c in [m.getAbr() for m in members]: #member required
                        critmember = members[[m.getAbr() for m in members].index(c)]
                        self.__criterioncards.append(critmember.cards) #member.cards is already a list. Just append that list 
                    else:
                        for move in self.getMoves(): #stat required
                            if move.getStrength() == statsnames[c-1]:
                                critstatcards.append(move)
                        self.__criterioncards.append(critstatcards)
                elif str(c)[0] in "([{" and len(c) == 2 and c[0] in [m.getAbr() for m in members] and c[1] in range(1,5): #iterable: double criteria
                    critmember = members[[m.getAbr() for m in members].index(c[0])]
                    critstatcards = list()
                    for move in self.getMoves():
                        if move.getStrength() == statsnames[c[1]-1]:
                            critstatcards.append(move)
                    self.__criterioncards.append(list(set(critmember.cards).intersection(critstatcards)))
                else:
                    raise ValueError('Invalid criteria')

    def __repr__(self):
        tup = list()
        for val in self.__boostvalues:
            for pair in self.__stats_boosts.items():
                if pair[1] == val and val > 1:
                    tup.append(pair[0])
        return 'mission' + str(tuple(tup))

    def __str__(self):
        text = "BTS Story " + "{}-{}: ".format(self.__chapter, self.__number)
        stats = list()
        for val in self.__boostvalues:
            for pair in self.__stats_boosts.items():
                if pair[1] == val and val > 1:
                    stats.append(pair[0])
        return text + str(stats).replace("'", "")[1:-1]

    def getStatsBoosts(self):
        return self.__stats_boosts

    def copy(self):
        return self

    def getCriteria(self):
        return list(self.__criteria)

    def getMoves(self):
        return self.__moves

    def solve(self, nbcards, fct='p'):
        if self.__criteria not in [(None,), (0,), ()]:
            if nbcards < len(self.__criteria):
                raise ValueError('nbcards cannot be smaller than number of criteria.')
        if fct not in ['p', 'f', 'pn']:
            raise ValueError('Invalid fct.')
        if nbcards < 1:
            raise ValueError("Must play at least 1 card.")
        listofpoints = [self.points(card.name) for card in self.__moves]
        card_points = dict(zip(self.__moves, listofpoints)) #dictionary (card object: points)
        descending_cards = sorted(card_points.items(), key=lambda x: x[1], reverse=True) #list of tuples: (card object, points)
        self.__best_cards = descending_cards[:nbcards] #sliced list
        reqcards = list() #picks the best card(s) among the list of required cards
        if self.__criteria:
            card_points1 = dict(zip(self.__criterioncards[0], [self.points(c.name) for c in self.__criterioncards[0]])) #first criterion
            descending_cards1 = sorted(card_points1.items(), key=lambda x: x[1], reverse=True)
            reqcard1 = descending_cards1[0] #tuple
            reqcards.append(reqcard1)
            if len(self.__criterioncards) == 2: #if there is a second criterion   
                card_points2 = dict(zip(self.__criterioncards[1], [self.points(c.name) for c in self.__criterioncards[1]]))
                descending_cards2 = sorted(card_points2.items(), key=lambda x: x[1], reverse=True)
                if reqcard1 == descending_cards2[0]: #if a same card is the strongest for both criteria
                    secondcards = [descending_cards1[1], descending_cards2[1]] # compare the second card of each criterion and select the stronger
                    secondcardspoints = [self.points(c[0].name) for c in secondcards]
                    maxpts = max(secondcardspoints)
                    reqcard2 = secondcards[secondcardspoints.index(maxpts)]
                else:
                    reqcard2 = descending_cards2[0]
                reqcards.append(reqcard2)
            cardstoadd = list() # cards not already in best cards will be appended here
            for reqcard in reqcards:
                if reqcard not in self.__best_cards:
                    cardstoadd.append(reqcard)
            i = -1 #replace worst card(s) in self.__best_cards by the cards to add :(
            for c in cardstoadd:
                if len(self.__criterioncards) == 2:
                    if self.__best_cards[i] in [reqcard1, reqcard2]: # special case: only one reqcard, and it's the worst among the best
                        i -= 1 # remove second worst of the best cards (the worst is a required card)
                self.__best_cards[i] = c
                i -= 1 #now self.__best_cards contains the cards to be played
        self.__total = 0
        for card,points in self.__best_cards:
            if fct in ['p', 'pn'] and card in [c[0] for c in reqcards]:
                print("REQUIRED CARD")
            if fct == 'p':
                self.points(card.name, 'p')
                print()
            elif fct == 'pn':
                l1 = max([len(c[0].member) for c in self.__best_cards])
                l2 = max([len(c[0].name) for c in self.__best_cards])
                f1 = ('{:' + str(l1) + 's}').format(card.member)
                f2 = ('{:' + str(l2) + 's}').format(card.name)
                print(card.getStrengthSymbol() + f1 + ': ' + str(card._stars) + '*', f2, 'LV ' + '{:2s}'.format(str(card.level)) + '\n', sep=', ')
            self.__total += points
        if fct == 'p':
            print('Total (without group stats):', self.__total, 'pts\n')
        self.__total += self.groupStatsPts(fct)
        if fct in ['p', 'pn']:
            print('TOTAL: ', self.__total, 'pts')
        if fct == 'f':
            return self.__total


class magicshop(cmission):
    '''Need to have >99% of margin score to get 7 gems.
Only the solve method works differently.
Assume criteria are by member only.'''
    def solve(self, target, nbcards, speed, *manualcards): #'p': makes it a void method
        if speed not in ['f',100]:
            raise ValueError("speed must either be f or 100.")
        starttime = time.time()
        shuffle(self.getMoves())
        movesnames = [members[membernames.index(c.member)].getAbr() for c in self.getMoves()]
        print("Finding card combination...\n")
        print("If it takes over 1 minute, close and restart the program.\n")
        cardstarget = target-self.groupStatsPts('f') # will help reduce size of dpTable
        critlist = self.getCriteria().copy() # assumed that nbcards >= len(critlist)
        toplay = list()
        for i in range(manualcards.count('s')): # automatically select strongest card
            highestindex = [self.points(c.name) for c in self.getMoves()].index(max([self.points(c.name) for c in self.getMoves()]))
            highestcard = self.getMoves()[highestindex]
            overshoot = cardstarget-self.points(highestcard.name) < min([self.points(c.name) for c in self.getMoves()])
            if (members[membernames.index(highestcard.member)].getAbr() not in critlist and nbcards<=len(critlist)) or overshoot:
                highestunplayable = [highestcard]
                self.getMoves().remove(highestcard)
                while True:
                    h2 = self.getMoves().index(max([self.points(c.name) for c in self.getMoves()])) # from remcards
                    hc2 = self.getMoves()[h2]
                    overshoot2 = cardstarget-self.points(hc2.name) < min([self.points(c.name) for c in self.getMoves()])
                    if (members[membernames.index(hc2.member)].getAbr() not in critlist and nbcards<=len(critlist)) or overshoot2:
                        self.getMoves().remove(hc2)
                        highestunplayable.append(hc2)
                    else:
                        for c in highestunplayable:
                            self.getMoves().append(c) # add them back in
                        highestcard = hc2
                        break
            self.getMoves().remove(highestcard)
            nbcards -= 1
            toplay.append(highestcard)
            mcmember = members[membernames.index(highestcard.member)].getAbr()
            if mcmember in critlist:
                critlist.remove(mcmember)   
        for mc in manualcards:
            if isinstance(mc, str):
                if mc in [c.name for c in self.getMoves()]:
                    mcardindex = [c.name for c in self.getMoves()].index(mc)
                    mc = self.getMoves()[mcardindex] # mc is now of type card
                else:
                    continue
            else:
                if mc not in self.getMoves():
                    continue
            mcmember = members[membernames.index(mc.member)].getAbr()
            if cardstarget-self.points(mc.name) >= min([self.points(c.name) for c in self.getMoves()]): # don't want to overshoot
                if members[membernames.index(mc.member)].getAbr() not in critlist and nbcards<=len(critlist): # unplayable
                    continue
                self.getMoves().remove(mc)
                nbcards -= 1
                toplay.append(mc)
                cardstarget -= self.points(mc.name)
                if mcmember in critlist:
                    critlist.remove(mcmember)            
        if nbcards < len(self.getCriteria()):
            raise ValueError('nbcards cannot be smaller than number of criteria.')
        listofpoints = [self.points(card.name) for card in self.getMoves()]
        if cardstarget < min(listofpoints):
            return None
        card_points = list(zip(self.getMoves(), listofpoints))
        if len(critlist) > 0:
            #it = 0
            for i in range(len(card_points)):
                if members[membernames.index(card_points[i][0].member)].getAbr() in critlist:
                    card_points.insert(0, card_points.pop(i)) # cards respecting criteria will be given priority (partial insertion-sort)
                    #it += 1
        listofpoints = [p[1] for p in card_points]
        sortedcards = [c[0] for c in card_points]
        minpts = int(0.9901*cardstarget)+1
        maxpts = cardstarget+(cardstarget-minpts)
        absmargin = cardstarget # cardstarget-bestscore
        bestscore = 0
        bestindex = 0
        dpTable = []
        for i in range(len(self.getMoves())+1):
            dpTable.append([[nbcards,critlist]]) # eventual row
        for j in range(1, maxpts+1):
            dpTable[0].append([None,None])
        ### NOT ALL ROWS WILL BE OF EQUAL LENGTH. MAKE DPTABLE AS WE CALCULATE, SAVES TIME
        limitpts = 0 # sum(listofpts[:index])
        margin99 = False
        for i in range(1,len(self.getMoves())+1):
            #print(i)
            if limitpts <= maxpts:
                limitpts += listofpoints[i-1] # early stages: limitpts <<< maxpts
            for j in range(1,min(maxpts+1, limitpts+1, cardstarget+absmargin)):
                dpTable[i].append([None,None]) # may be modified. The new list is at index (i,j)
                if j<listofpoints[i-1]: # current card doesn't help
                    if len(dpTable[i-1]) > j: # index j not out of range
                        if dpTable[i-1][j] != [None,None]:
                            dpTable[i][j][0] = dpTable[i-1][j][0]
                            dpTable[i][j][1] = dpTable[i-1][j][1].copy() # None has no copy method
                else:
                    if len(dpTable[i-1]) > j:
                        if dpTable[i-1][j] != [None,None]: # if can get j points without current card
                            dpTable[i][j][0] = dpTable[i-1][j][0]
                            dpTable[i][j][1] = dpTable[i-1][j][1].copy()
                            continue
                    # ABSOLUTELY NEED CURRENT CARD
                    if len(dpTable[i-1]) > j-listofpoints[i-1]:
                        if dpTable[i-1][j-listofpoints[i-1]] != [None,None]: # card will help
                            if dpTable[i-1][j-listofpoints[i-1]][0] > 0: # still have room for cards
                                cardm = members[membernames.index(sortedcards[i-1].member)].getAbr()
                                playable = False
                                if cardm in dpTable[i-1][j-listofpoints[i-1]][1]: # crit respected
                                    playable = True
                                    dpTable[i][j][0] = dpTable[i-1][j-listofpoints[i-1]][0]-1 # we use this card
                                    dpTable[i][j][1] = dpTable[i-1][j-listofpoints[i-1]][1].copy()
                                    dpTable[i][j][1].remove(cardm)
                                elif dpTable[i-1][j-listofpoints[i-1]][0] > len(dpTable[i-1][j-listofpoints[i-1]][1]): # at least one slot without crit.
                                    playable = True
                                    dpTable[i][j][0] = dpTable[i-1][j-listofpoints[i-1]][0]-1 # we use this card
                                    dpTable[i][j][1] = dpTable[i-1][j-listofpoints[i-1]][1].copy()
                                if speed == 'f' and playable and minpts <= j <= maxpts: # fast solve
                                    margin99 = True
                                    absmargin = abs(cardstarget-j)
                                    bestscore = j
                                    bestindex = i
                                elif speed == 100 and playable and absmargin>abs(cardstarget-j):
                                    absmargin = abs(cardstarget-j)
                                    bestscore = j
                                    bestindex = i
            if absmargin == 0 or margin99: # solvable YAY!!!
                break
        endtime = time.time()
        if absmargin == 0:
            margin = "100"
        else:
            ratio = 10000*(target-absmargin)/target # max 9999.999990
            if ratio%1 > 0.99999: # bc Python bs
                ratio = int(ratio)+1
            ratio = int(ratio) # else truncate
            # ratio will have max value 9999
            margin = str(ratio)[:-2]+'.'+str(ratio)[-2:] # safe division by 100
        ### DISPLAY RESULT ###
        trackscore = bestscore
        trackindex = bestindex
        for c in toplay:
            self.getMoves().append(c)
        while trackscore != 0: # one of dpTable[trackindex-1][trackscore] or dpTable[trackindex-1][trackscore-pts] will have a non-null entry.
            try:
                if dpTable[trackindex-1][trackscore] == [None, None]:
                    toplay.append(sortedcards[trackindex-1])
                    trackscore -= listofpoints[trackindex-1]
                trackindex -= 1
            except IndexError: # the if statement would evaluate to True
                toplay.append(sortedcards[trackindex-1])
                trackscore -= listofpoints[trackindex-1]
                trackindex -= 1
        solution = dpTable[bestindex][bestscore] #[nb,[]]
        del dpTable
        gc.collect()
        for c in solution[1]: # unused crit. if solution[1] == []: all criteria slots filled
            critlist.remove(c) # remove unused crit. Only used for display
        for card in toplay:
            cardmember = members[membernames.index(card.member)].getAbr()
            if cardmember in critlist:
                critlist.remove(cardmember) # current card uses this crit slot
                print("REQUIRED CARD")
            #print(card.name)
            self.points(card.name, 'p')
            print()
        print('Total (without group stats):', bestscore, 'pts\n')
        bestscore += self.groupStatsPts('p')
        print('SCORE: ', bestscore, 'pts')
        print("Margin: {}%".format(margin))
        solvetime = endtime-starttime
        solvemessage = "Solved within {} second"
        if solvetime >= 2:
            solvemessage += 's' # plural
        print(solvemessage.format(format(endtime-starttime, ".2f"))+'.')

    def __str__(self):
        text = "Magic Shop " + "{}-{}: ".format(self.__chapter, self.__number)
        stats = list()
        for val in self.__boostvalues:
            for pair in self.__stats_boosts.items():
                if pair[1] == val and val > 1:
                    stats.append(pair[0])
        return text + str(stats).replace("'", "")[1:-1]

#ANOTHER STORY SEASON 2 CHAPTER 1
ms1m2 = magicshop(1,2,3,4,1,2,1.55,1.55,0.9,0.9)
#ms1m2.solve(16506, 1, 'f')
ms1m4 = magicshop(1,4,4,2,1,3,4.55,0.7,0.3,0.05,'RM')
#ms1m4.solve(52129, 3, 'f')
#ms1m4.solve(52129, 3, 100)
ms1m6 = magicshop(1, 6, 3, 4, 2, 1, 5.95, 1.95, 0.35, 0.05, 'V')
#ms1m6.solve(87653, 4, 'f')
#ms1m6.solve(87653, 4, 100)
ms1m8 = magicshop(1, 8, 4, 2, 3, 1, 7.75, 0.95, 0.5, 0.35, "RM")
#ms1m8.solve(90552, 5, 'f')
#ms1m8.solve(90552, 5, 100)
ms1m10 = magicshop(1, 10, 2, 4, 3, 1, 9.55, 2.25, 0.5, 0.05)
#ms1m10.solve(80389, 2, 'f')
#ms1m10.solve(80389, 2, 100)
ms1m13 = magicshop(1, 13, 2, 3, 4, 1, 12, 1.65, 0.35, 0.05, "RM")
#ms1m13.solve(104266, 4, 'f')
#ms1m13.solve(104266, 4, 100)
ms1m15 = magicshop(1, 15, 2, 1, 3, 4, 8.5, 2.32, 0.82, 0.33, "RM", "JH")
#ms1m15.solve(153303, 5, 'f')
#ms1m15.solve(153303, 5, 100)
ms1m17 = magicshop(1, 17, 2, 1, 4, 3, 9.99, 3.95, 0.59, 0.02, "RM", "V")
#ms1m17.solve(146381, 6, 'f')
#ms1m17.solve(146381, 6, 100)
ms1m19 = magicshop(1, 19, 1, 3, 4, 2, 7.55, 2.25, 0.68, 0.1)
#ms1m19.solve(130712, 4, 'f')
#ms1m19.solve(130712, 4, 100)
ms1m21 = magicshop(1, 21, 1, 3, 2, 4, 3, 3, 2, 2)
#ms1m21.solve(93104, 3, 'f')
#ms1m21.solve(93104, 3, 100)
#CHAPTER 2
ms2m2 = magicshop(2, 2, 3, 4, 2, 1, 4.5, 3.5, 0.91, 0.9, "SG")
#ms2m2.solve(71181, 4, 'f')
#ms2m2.solve(71181, 4, 100)
ms2m4 = magicshop(2, 4, 4, 3, 2, 1, 4.55, 4.5, 0.7, 0.3, "SG")
#ms2m4.solve(79330, 5, 'f')
#ms2m4.solve(79330, 5, 100)
ms2m6 = magicshop(2, 6, 1, 4, 3, 2, 8.88, 1.95, 0.99, 0.14, "SG", "V")
#ms2m6.solve(156230, 4, 'f')
#ms2m6.solve(156230, 4, 100)
ms2m8 = magicshop(2, 8, 1, 2, 4, 3, 5.55, 4, 1, 0.15, "SG", "RM")
#ms2m8.solve(101599, 4, 'f')
#ms2m8.solve(101599, 4, 100)
ms2m10 = magicshop(2, 10, 3, 1, 4, 2, 5, 4.95, 0.9, 0.61, "SG", "RM")
#ms2m10.solve(87161, 5, 'f')
#ms2m10.solve(87161, 5, 100)
ms2m12 = magicshop(2, 12, 4, 1, 3, 2, 8.11, 7, 0.59, 0.5, "SG", "JM")
#ms2m12.solve(217663, 4, 'f')
#ms2m12.solve(217663, 4, 100)
ms2m14 = magicshop(2, 14, 4, 1, 3, 2, 5, 1.11, 0.55, 0.05, "SG")
#ms2m14.solve(89400, 5, 'f')
#ms2m14.solve(89400, 5, 100)
ms2m16 = magicshop(2, 16, 3, 2, 4, 1, 6.5, 4.55, 0.75, 0.15, "SG", "JH")
#ms2m16.solve(189718, 5, 'f')
#ms2m16.solve(189718, 5, 100)
ms2m18 = magicshop(2, 18, 2, 1, 3, 4, 6.66, 6.11, 0.7, 0.1, "JH", "JK")
#ms2m18.solve(148229, 4, 'f')
#ms2m18.solve(148229, 4, 100)
ms2m20 = magicshop(2, 20, 4, 2, 3, 1, 9, 0.5, 0.48, 0.35, "SG", "SJ")
#ms2m20.solve(59888, 4, 'f')
#ms2m20.solve(59888, 4, 100)
# CHAPTER 3
ms3m2 = magicshop(3, 2, 2, 3, 4, 1, 8.7, 6.5, 0.75, 0.21, "JM")
#ms3m2.solve(183545, 5, 'f')
#ms3m2.solve(183545, 5, 100)
ms3m4 = magicshop(3, 4, 1, 2, 4, 3, 5.05, 5.05, 3.59, 0.09, "JM")
#ms3m4.solve(83730, 4, 'f')
#ms3m4.solve(83730, 4, 100)
ms3m7 = magicshop(3, 7, 2, 3, 4, 1, 6.62, 3.79, 2.54, 1.11, 'V', "JM")
#ms3m7.solve(123254, 4, 'f')
ms3m9 = magicshop(3, 9, 1, 2, 4, 3, 3.59, 2.99, 0.65, 0.15, "JH", "JM")
#ms3m9.solve(74144, 4, 'f')
ms3m11 = magicshop(3, 11, 4, 3, 2, 1, 8.51, 5, 0.34, 0.05, "JM", "JH")
#ms3m11.solve(147960, 4, 'f')
ms3m13 = magicshop(3, 13, 4, 1, 2, 3, 8.19, 1.77, 1.57, 0.59, "RM")
#ms3m13.solve(152376, 4, 'f')
ms3m15 = magicshop(3, 15, 1, 3, 2, 4, 4.88, 3.5, 0.31, 0.31, "JM", "RM")
#ms3m15.solve(160808, 5, 'f')
ms3m17 = magicshop(3, 17, 3, 2, 4, 1, 7.01, 5.16, 0.89, 0.05, "SJ", "JM")
#ms3m17.solve(79636, 3, 'f')
ms3m19 = magicshop(3, 19, 4, 2, 3, 1, 7.06, 5.19, 0.7, 0.16, "JM", "SG")
#ms3m19.solve(83847, 3, 'f')
ms3m21 = magicshop(3, 21, 1, 4, 3, 2, 5.11, 4.53, 0.48, 0.3, "JM", "JK")
#ms3m21.solve(109580, 3, 'f')
# CHAPTER 4
ms4m2 = magicshop(4, 2, 1, 4, 3, 2, 8.72, 4, 0.98, 0.55, "SJ")
#ms4m2.solve(115322, 3, 'f')
ms4m5 = magicshop(4, 5, 4, 3, 2, 1, 4.57, 1.31, 0.05, 0.01, "SJ", 'V')
#ms4m5.solve(55221, 4, 'f')
ms4m7 = magicshop(4, 7, 1, 2, 3, 4, 6.77, 5.62, 1.53, 0.91, "SJ")
#ms4m7.solve(150279, 4, 'f')
ms4m9 = magicshop(4, 9, 4, 3, 2, 1, 8.71, 6.76, 0.32, 0.11, "RM", "SJ")
#ms4m9.solve(89856, 4, 'f')
ms4m11 = magicshop(4, 11, 3, 4, 2, 1, 7.98, 4.73, 0.85, 0.43, 'V')
#ms4m11.solve(141423, 3, 'f')
ms4m13 = magicshop(4, 13, 2, 1, 4 ,3, 7.17, 0.98, 0.55, 0.34, "JK")
#ms4m13.solve(115157, 5, 'f')
ms4m15 = magicshop(4, 15, 4, 3, 2, 1, 6.16, 0.51, 0.11, 0.05, "JK")
#ms4m15.solve(132239, 5, 'f')
ms4m17 = magicshop(4, 17, 1, 2, 3, 4, 9.97, 1.09, 0.91, 0.05, "JH")
#ms4m17.solve(150098, 3, 'f')
ms4m19 = magicshop(4, 19, 2, 1, 4, 3, 3.96, 3.06, 0.85, 0.33, "JH")
#ms4m19.solve(148667, 5, 'f')
ms4m21 = magicshop(4, 21, 2, 3, 1, 4, 9.21, 8.81, 1.18, 0.58, "SJ", "SG")
#ms4m21.solve(363713, 6, 'f')
# CHAPTER 5
ms5m2 = magicshop(5, 2, 3, 4, 2, 1, 8.1, 0.84, 0.55, 0.1, 'V', "JM")
#ms5m2.solve(125863, 4, 'f')
ms5m4 = magicshop(5, 4, 4, 1, 2, 3, 3.97, 0.89, 0.53, 0.32, 'V')
#ms5m4.solve(52090, 3, 'f')
ms5m6 = magicshop(5, 6, 3, 4, 1, 2, 4.36, 3.52, 2.91, 1.02, 'V')
#ms5m6.solve(63436, 2, 'f')
ms5m8 = magicshop(5, 8, 1, 4, 3, 2, 6.32, 5.72, 1.51, 0.1, 'V', 'V')
#ms5m8.solve(144459, 3, 'f')
ms5m10 = magicshop(5, 10, 3, 2, 4, 1, 3.59, 0.78, 0.3, 0.07, "JH")
#ms5m10.solve(30118, 4, 'f')
ms5m12 = magicshop(5, 12, 2, 1, 4, 3, 6.88, 4.13, 0.09, 0.04, "RM", 'V')
#ms5m12.solve(199870, 5, 'f')
ms5m15 = magicshop(5, 15, 4, 2, 3, 1, 6.01, 3.51, 0.5, 0.23, 'V', "SG")
#ms5m15.solve(103582, 4, 'f')
ms5m17 = magicshop(5, 17, 2, 4, 1, 3, 5.87, 4.68, 0.66, 0.05, "SJ")
#ms5m17.solve(202246, 6, 'f')
ms5m19 = magicshop(5, 19, 1, 3, 4, 2, 6.85, 4.19, 0.27, 0.15, 'V')
#ms5m19.solve(235293, 5, 'f')
ms5m21 = magicshop(5, 21, 2, 1, 3, 4, 4.41, 3.69, 2.62, 1.19, 'V', "JK")
#ms5m21.solve(98818, 3, 'f')

ms6m2 = magicshop(6, 2, 3, 1, 2, 4, 7.81, 4.56, 1.51, 0.84, "JH", "JK")
ms6m5 = magicshop(6, 5, 4, 2, 1, 3, 2.67, 1.98, 0.49, 0.12, "JH", "JH")
ms6m7 = magicshop(6, 7, 3, 4, 1, 2, 4.36, 3.52, 2.91, 1.02, "JK")
ms6m9 = magicshop(6, 9, 1, 4, 3, 2, 6.32, 5.72, 1.51, 0.1, "RM", "JK")
ms6m11 = magicshop(6, 11, 1, 3, 4, 2, 7.77, 1.77, 0.77, 0.71, "RM")
ms6m13 = magicshop(6, 13, 4, 1, 3, 2, 6.59, 4.81, 0.07, 0.05, "JM", "JH")
ms6m15 = magicshop(6, 15, 2, 4, 1, 3, 5.87, 3.69, 0.11, 0.05, "JH")
ms6m17 = magicshop(6, 17, 2, 4, 3, 1, 5.51, 3.15, 0.5, 0.09, "SJ")
ms6m19 = magicshop(6, 19, 4, 1, 3, 2, 8.11, 0.85, 0.33, 0.27, "V")
ms6m21 = magicshop(6, 21, 1, 2, 4, 3, 4.59, 3.59, 1, 0.19, "JK", "SG")

def getRollCall():
    it1 = 1
    if all([m.rollCalled() for m in members]):
        print("BTS", end=": ")
        rollcallmember = members[0]
    elif not any([m.rollCalled() for m in members]):
        print("No roll call.")
        return
    else:
        mindex = [m.rollCalled() for m in members].index(True) # there is only one True
        rollcallmember = members[mindex]
        print(rollcallmember._name, end=": ")
    boosttext = '+'
    perc_text = {1.03:"3%", 1.05:"5%", 1.1:"10%"}
    stattext = str()
    if rollcallmember.rollcallstat == 5:
        stattext = "All stats"
    else:
        stattext = statsnames[rollcallmember.rollcallstat-1]
    if rollcallmember.rollcallboost < 100:
        boosttext += perc_text[rollcallmember.rollcallboost]
    else:
        boosttext += str(rollcallmember.rollcallboost)
    print(stattext, boosttext)
            
def msmainmenu():
    global rc
    ms_m = {"1-2":(ms1m2,16506,1), "1-4":(ms1m4,52129,3), "1-6":(ms1m6,87653,4),
            "1-8":(ms1m8,90552,5), "1-10":(ms1m10,80389,2),"1-13":(ms1m13,104266,4),
            "1-15":(ms1m15,153303,5), "1-17":(ms1m17,146381,6), "1-19":(ms1m19,130712,4),
            "1-21":(ms1m21,93104,3), "2-2":(ms2m2,71181,4), "2-4":(ms2m4,79330,5),
            "2-6":(ms2m6,156230,4), "2-8":(ms2m8,101599,4), "2-10":(ms2m10,87161, 5),
            "2-12":(ms2m12,217663,4), "2-14":(ms2m14,89400,5), "2-16":(ms2m16,189718,5),
            "2-18":(ms2m18,148229,4), "2-20":(ms2m20,59888,4), "3-2":(ms3m2,183545,5),
            "3-4":(ms3m4,83730,4), "3-7":(ms3m7,123254,4), "3-9":(ms3m9,74144,4),
            "3-11":(ms3m11,147960,4), "3-13":(ms3m13,152376,4), "3-15":(ms3m15,160808,5),
            "3-17":(ms3m17,79636,3), "3-19":(ms3m19,83847,3), "3-21":(ms3m21,109580,3),
            "4-2":(ms4m2,115322,3), "4-5":(ms4m5,55221,4), "4-7":(ms4m7,150279,4),
            "4-9":(ms4m9,89856,4), "4-11":(ms4m11,141423,3), "4-13":(ms4m13,115157,5),
            "4-15":(ms4m15,132239,5), "4-17":(ms4m17,150098,3), "4-19":(ms4m19,148667,5),
            "4-21":(ms4m21,363713,6), "5-2":(ms5m2,125863,4), "5-4":(ms5m4,52090,3),
            "5-6":(ms5m6,63436,2), "5-8":(ms5m8,144459,3), "5-10":(ms5m10,30118,4),
            "5-12":(ms5m12,199870,5), "5-15":(ms5m15,103582,4), "5-17":(ms5m17,202246,6),
            "5-19":(ms5m19,235293,5), "5-21":(ms5m21,98818,3), "6-2":(ms6m2,183429,4),
            "6-5":(ms6m5,49828,4), "6-7":(ms6m7,93263,4), "6-9":(ms6m9,108489,3),
            "6-11":(ms6m11,174145,4), "6-13":(ms6m13,123139,5), "6-15":(ms6m15,49943,3),
            "6-17":(ms6m17,186209,5), "6-19":(ms6m19,44974,2)), "6-21":(ms6m21,52088,3)}
    print("Hi Manager-nim! Welcome to the Magic Shop Calculator ♥")
    print("So show me, I'll show you~")
    while True:
        print("-----------------------------")
        print("MAIN MENU\n")
        if rc == 'n':
            print("No roll call.\n")
        else:
            getRollCall()
            print()
        for item in zip(statsnames, groupstatslevel):
            print(item[0], item[1], sep=": level ")
        print()
        option = input('''For each question, type your answer and press Enter.

(1) Play a Magic Shop mission
(2) Change card level/view cards
(3) Add a new card
(4) Update/remove current roll call
(5) Change agency stat
(6) Exit\n''')
        if option == '1':
            print("Play a Magic Shop mission\n")
            missionnb = input("Type the mission number you would like to play (e.g. 2-12)\nOR press Enter to return to main menu: ")
            if missionnb == '':
                continue
            while missionnb not in ms_m.keys() and missionnb != 'e':
                print("\nNot a mission!\n")
                missionnb = input("Type the mission number you would like to play (e.g. 2-12): ")
            marginchoice = ''
            while marginchoice not in ['1', '2']:
                marginchoice = input("\n99% (1) or 100% (2)? (100% may crash for some missions)\nEnter margin choice: ")
                speed = ''
                print()
                if marginchoice == '1':
                    speed = 'f'
                elif marginchoice == '2':
                    speed = 100
            ms_m[missionnb][0].solve(ms_m[missionnb][1], ms_m[missionnb][2], speed)
        elif option == '2':
            print("Change card level/view cards\n")
            message = "Select a BTS member:\n"
            for m in members:
                message += (m._name + " (" + str(members.index(m)+1) + "), ")
            message = message[:-2]+"\nOR press Enter to return to main menu: "
            mb = input(message)
            if mb == '':
                continue
            while mb not in [str(n) for n in range(1, 8)]:
                print("\nNumber but be between 1 and 7.\n")
                mb = input(message)
            m = members[int(mb)-1]
            m.manageCards()
        elif option == '3':
            print("Add a new card\n")
            message = "Add a new card for which BTS member?\n"
            for m in members:
                message += (m._name + " (" + str(members.index(m)+1) + "), ")
            message = message[:-2]+"\nOR press Enter to return to main menu: "
            mb = input(message)
            if mb == '':
                continue
            while mb not in [str(n) for n in range(1, 8)]:
                print("\nNumber but be between 1 and 7.\n")
                mb = input(message)
            m = members[int(mb)-1]
            m.addCard()
        elif option == '4':
            print("Update/remove current roll call\n")
            option4 = ''
            while option4 not in ['1', '2']:
                option4 = input("Remove (1) or update (2) roll call?\nOR press Enter to return to main menu: ")
                print()
                if option4 == '':
                    break
                if option4 == '1':
                    removeRollCall()
                    rc = 'n'
                elif option4 == '2':
                    message = "Select a BTS member:\n"
                    for m in members:
                        message += (m._name + " (" + str(members.index(m)+1) + "), ")
                    message += "BTS (8)\nOR press Enter to return to main menu: "
                    mb = input(message)
                    while mb not in [str(n) for n in range(1, 9)]+['']:
                        print("\nNumber must be between 1 and 9.\n")
                        mb = input(message)
                    if mb == '':
                        break
                    if int(mb) == 9:
                        m = "BTS"
                    else:
                        m = members[int(mb)-1].getAbr()
                    statmessage = "Empathy (1), Passion (2), Stamina (3), Wisdom (4), All stats (5)\nOR press Enter to return to main menu: "
                    stat = input(statmessage)
                    while stat not in [str(n) for n in range(1, 6)]+['']:
                        print("\nNumber must be between 1 and 5.\n")
                        stat = input(statmessage)
                    if stat == '':
                        break
                    stat = int(stat)
                    boostlist = [100, 200, 400, 1.03, 1.05, 1.1]
                    boostmessage = "+100 (1), +200 (2), +400 (3), +3% (4), +5% (5), +10% (6)\nOR press Enter to return to main menu: "
                    boostindex = input(boostmessage)
                    while boostindex not in [str(n) for n in range(1, 7)]+['']:
                        print("\nNumber must be between 1 and 6.\n")
                        boostindex = input(boostmessage)
                    if boostindex == '':
                        break
                    boost = boostlist[int(boostindex)-1]
                    print()
                    newRollCall(m, stat, boost)
                    rc = 'y'
        elif option == '5':
            print("Change agency stat\n")
            while True:
                usr = input('''Type a number from 1 to 4 (Empathy (1), Passion (2), Stamina (3), Wisdom (4)),
followed by 'up' (level up) or 'down' (level down)\nOR press Enter to return to main menu: ''')
                if usr == '':
                    break
                if usr[0] in [str(n) for n in range(1, 5)]:
                    stat = int(usr[0])
                    if "up" in usr:
                        levelUpStat(stat)
                        break
                    elif "down" in usr:
                        undoLevelUpStat(stat)
                        break
                else:
                    print("\nNumber must be between 1 and 4.\n")
        elif option == '6':
            break

msmainmenu()
