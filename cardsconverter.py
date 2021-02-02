members = ["RM", "Jin", "Suga", "J-Hope", "Jimin", "V", "Jungkook"]
initials = {"RM":"RM", "Jin":"SJ", "Suga":"SG", "J-Hope":"JH", "Jimin":"JM", "V":"V", "Jungkook":"JK"}

traits = ["Empathy", "Passion", "Stamina", "Wisdom"]
### CARDS FOR WHICH THEIR TRAIT AT LEVEL 1 IS NOT STRICTLY BIGGER THAN ALL OTHER STATS
empathyexception = [('Jungkook', '5', "The Name's Jung Kook"),
                    ('RM', '5', 'Professional'), ('RM', '5', 'FAKE LOVE RM'),
                    ('V', '4', 'A Break'), ('Suga', '4', 'Metronome'),
                    ('Jimin', '3', 'Cupid'), ('Jin', '2', 'Pouty'),
                    ('Jimin', '2', 'Are You Watching'), ('RM', '1', "Let's Go")]

passionexception = [('Suga', '5', 'FAKE LOVE SUGA'), ('Jungkook', '5', 'To the Store'),
                    ('RM', '4', 'Handsome Dimple Guy'),
                    ('Suga', '3', 'Bespectacled Sunbae'), ('V', '3', 'Basketball Genius'),
                    ('V', '3', 'I Need a Nap'),('V', '2', 'Mischief Maker')]

staminaexception = [('Suga', '5', 'The Decisive Moment'), ('V', '5', 'FAKE LOVE V'),
                    ('J-Hope', '5', 'FAKE LOVE j-hope'), ('V', '5', 'Orchard Boy'),
                    ('RM', '4', 'Clear Skies After Rain'), ('Jimin', '4', 'Secret Recipe'),
                    ('Suga', '4', 'An Autumn Letter'), ('Jungkook', '4', 'Black Belt'),
                    ('J-Hope', '3', 'Hippity Hoppity'),
                    ('Jungkook', '3', "Don't Even Know"), ('J-Hope', '1', 'Confident!')]

wisdomexception = [('Jin', '5', 'FAKE LOVE Jin'), ('Jimin', '5', 'FAKE LOVE Jimin'),
                   ('Jin', '5', 'Pleased to Meet You'), ('Suga', '4', 'SUGA Rabbit'),
                   ('Jin', '4', 'Undercover'), ('Jin', '3', 'Man with a Passion'),
                   ('RM', '3', 'Stretching'), ('RM', '3', 'To Go See You'),
                   ('RM', '3', 'Inspired'), ('RM', '2', 'Brain Fully Activated'),
                   ('V', '1', 'Nice to Meet You')]

exception = [empathyexception, passionexception, staminaexception, wisdomexception]
#print(sum([len(e) for e in exception]))
##########################################################################################
manager = input("Manager name: ")
fp = open("cards_{}.txt".format(manager))
groupstats = list()
c = list()
names = list()
curline = fp.readline()

while len(groupstats) < 4: # get group stats
    if curline.strip().isdigit():
        groupstats.append(int(curline.strip()))
    curline = fp.readline()

while not (len(curline.strip().split('\t')) == 2 and curline.strip().split('\t')[0] in members and curline.strip().split('\t')[1][0].isdigit()):
    curline = fp.readline()

n = 0
while curline != '': # process cards
    member, star = curline.strip().split("\t")
    star = int(star[0])
    name = fp.readline().strip()
    if name in ["Deep in Thought", "Pit-A-Pat", "Let's Go"]:
        name = initials[member]+name
    elif name == "All Eyes on Me":
        name += str(star)
    ### JK has 2 cards called All Eyes on Me
    ### JK and Jin both have a Pit-A-Pat, Deep in Thought; RM and V both have Let's Go
    level = int(fp.readline().strip())
    stats = [int(n) for n in fp.readline().strip().replace(',','').split('\t')[:-1]]
    strength = stats.index(max(stats))
    for i in range(len(exception)):
        if (member, str(star), name) in exception[i]:
            strength = i
            break
    c.append([member, name, star, stats[0], stats[1], stats[2], stats[3], traits[i], level])
    curline = fp.readline()

fp.close()
### CONVERT POINTS TO LEVEL:
fw = open("BTS_World_{}.txt".format(manager), 'w')
levels = list()
for p in groupstats:
    if (p-103)%13 == 0: # level 50+
        levels.append((p-103)//13)
    elif (p-100)%13 == 0:
        levels.append((p-100)//13)
fw.write(str(levels)[1:-1]+"\n")

for l in c:
    for i in range(len(l)):
        fw.write(str(l[i]))
        if i != 8:
            fw.write("; ")
    fw.write('\n')
yay = input("Successfully created BTS_World_{}.txt, press enter to exit. ".format(manager))
fw.close()
