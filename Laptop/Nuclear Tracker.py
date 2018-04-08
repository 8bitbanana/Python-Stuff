import requests, json, time, os
from pprint import pprint

steamid = '[redacted]'
nuclearid = '[redacted]'

nturl = 'https://tb-api.xyz/stream/get?s={}&key={}'.format(steamid, nuclearid)

weplist = [None,
           'Revolver',
           'Triple Machinegun',
           'Wrench',
           'Machinegun',
           'Shotgun',
           'Crossbow',
           'Grenade Launcher',
           'Double Shotgun',
           'Minigun',
           'Auto Shotgun',
           'Auto Crossbow',
           'Super Crossbow',
           'Shovel',
           'Bazooka',
           'Sticky Launcher',
           'SMG',
           'Assault Rifle',
           'Disc Gun',
           'Laser Pistol',
           'Laser Rifle',
           'Slugger',
           'Gatling Slugger',
           'Assault Slugger',
           'Energy Sword',
           'Super Slugger',
           'Hyper Rifle',
           'Screwdriver',
           'Laser Minigun',
           'Blood Launcher',
           'Splinter Gun',
           'Toxic Bow',
           'Sentry Gun',
           'Wave Gun',
           'Plasma Gun',
           'Plasma Cannon',
           'Energy Hammer',
           'Jackhammer',
           'Flak Cannon',
           'Golden Revolver',
           'Golden Wrench',
           'Golden Machinegun',
           'Golden Shotgun',
           'Golden Crossbow',
           'Golden Grenade Launcher',
           'Golden Laser Pistol',
           'Chicken Sword',
           'Nuke Launcher',
           'Ion Cannon',
           'Quadruple Machinegun',
           'Flamethrower',
           'Dragon',
           'Flare Gun',
           'Energy Screwdriver',
           'Hyper Launcher',
           'Laser Cannon',
           'Rusty Revolver',
           'Lightning Pistol',
           'Lightning Rifle',
           'Lightning Shotgun',
           'Super Flak Cannon',
           'Sawed-off Shotgun',
           'Splinter Pistol',
           'Super Splinter Gun',
           'Lightning SMG',
           'Smart Gun',
           'Heavy Crossbow',
           'Blood Hammer',
           'Lightning Cannon',
           'Pop Gun',
           'Plasma Rifle',
           'Pop Rifle',
           'Toxic Launcher',
           'Flame Cannon',
           'Lightning Hammer',
           'Flame Shotgun',
           'Double Flame Shotgun',
           'Auto Flame Shotgun',
           'Cluster Launcher',
           'Grenade Shotgun',
           'Grenade Rifle',
           'Rogue Rifle',
           'Party Gun',
           'Double Minigun',
           'Gatling Bazooka',
           'Auto Grenade Shotgun',
           'Ultra Revolver',
           'Ultra Laser Pistol',
           'Sledgehammer',
           'Heavy Revolver',
           'Heavy Machinegun',
           'Heavy Slugger',
           'Ultra Shovel',
           'Ultra Shotgun',
           'Ultra Crossbow',
           'Ultra Grenade Launcher',
           'Plasma Minigun',
           'Devastator',
           'Golden Plasma Gun',
           'Golden Slugger',
           'Golden Splinter Gun',
           'Golden Screwdriver',
           'Golden Bazooka',
           'Golden Assault Rifle',
           'Super Disc Gun',
           'Heavy Auto Crossbow',
           'Heavy Assault Rifle',
           'Blood Cannon',
           'Dog',
           'Dog',
           'Incinerator',
           'Super Plasma Cannon',
           'Seeker Pistol',
           'Eraser',
           'Guitar',
           'Bouncer SMG',
           'Bouncer Shotgun',
           'Hyper Slugger',
           'Super Bazooka',
           'Frog Pistol',
           'Black Sword',
           'Golden Nuke Launcher',
           'Golden Disc Gun',
           'Heavy Grenade Launcher',
           'Gun Gun']
for x in range(0,100):
    weplist.append(None)
weplist[201] = 'Golden Frog Pistol'

enemylist = ['Bandit',
             'Maggot',
             'Rad Maggot',
             'Big Maggot',
             'Scorpion',
             'Gold Scorpion',
             'Big Bandit',
             'Rat',
             'Rat King',
             'Green Rat',
             'Gator',
             'Exploder',
             'Toxic Frog',
             'Mom',
             'Assasin',
             'Raven',
             'Salamander',
             'Sniper',
             'Big Dog',
             'Spider',
             '???',
             'Laser Crystal',
             'Hyper Crystal',
             'Snow Bandit',
             'Snowbot',
             'Wolf',
             'Snowtank',
             'Lil Hunter',
             'Freak',
             'Explo Freak',
             'Rhino Freak',
             'Necromancer',
             'Turret',
             'Technomancer',
             'Guardian',
             'Explo Guardian',
             'Dog Guardian',
             'The Nuclear Throne',
             'Throne II',
             'Bone Fish',
             'Crab',
             'Turtle',
             'Venus Grunt',
             'Venus Sarge',
             'Fireballer',
             'Super Fireballer',
             'Jock',
             'Cursed Spider',
             'Cursed Crystal',
             'Mimic',
             'Health Mimic',
             'IDPD Grunt',
             'IDPD Inspector',
             'IDPD Shielder',
             'Crown Guardian',
             'Explosion',
             'Small Explosion',
             'Fire Trap',
             'Shield',
             'Toxin',
             'Horror',
             'Barrel',
             'Toxic Barrel',
             'Golden Barrel',
             'Car',
             'Venus Car',
             'Venus Car',
             'Venus Car',
             'Car',
             'Thrown Car',
             'Mine',
             'Crown of Death',
             'Portal Strike',
             'Blood Launcher',
             'Blood Cannon',
             'Blood Hammer',
             'Disc',
             'Curse Eat',
             'Big Dog Missile',
             'Halloween Bandit',
             'Lil Hunter Death',
             'Throne Explosion',
             'Jungle Bandit',
             'Jungle Assassin',
             'Jungle Fly',
             'Crown of Hatred',
             'Ice Flower',
             'Cursed Ammo Pickup',
             'Underwater Lightning',
             'IDPD Elite Grunt',
             'Blood Gamble',
             'IDPD Elite Shielder',
             'IDPD Elite Inspector',
             'Captain',
             'IDPD Van',
             'Buff Gator',
             'Generator',
             'Lightning Crystal',
             'Golden Snowtank',
             'Small Generator',
             'Golden Disc',
             'Big Dog Explosion',
             'IDPD Freak',
             'Throne II Death',
             '???']

crownlist = [None,
             None,
             'Death',
             'Life',
             'Haste',
             'Guns',
             'Hatred',
             'Blood',
             'Destiny',
             'Love',
             'Risk',
             'Curses',
             'Luck',
             'Protection']

charlist = [None,
            'Fish',
            'Crystal',
            'Eyes',
            'Melting',
            'Plant',
            'Yung Venuz',
            'Steroids',
            'Robot',
            'Chicken',
            'Rebel',
            'Horror',
            'Rogue',
            'Skeleton',
            'Frog']

mutlist = ['Heavy Heart',
           'Rhino Skin',
           'Extra Feet',
           'Plutonium Hunger',
           'Rabbit Paw',
           'Throne Butt: {}',
           'Lucky Shot',
           'Blootlust',
           'Gamma Guts',
           'Second Stomach',
           'Back Muscle',
           'Scarier Face',
           'Euphoria',
           'Long Arms',
           'Boiling Veins',
           'Shotgun Shoulders',
           'Recycle Gland',
           'Laser Brain',
           'Last Wish',
           'Eagle Eyes',
           'Impact Wrists']

areadict = {100:'Crown Vault',
            1:'Desert',
            101:'Oasis',
            2:'Sewers',
            102:'Pizza Sewers',
            3:'Scrapyard',
            103:'Y.V\'s Mansion',
            4:'Crystal Caves',
            104:'Cursed Crystal Caves',
            5:'Frozen City',
            105:'Jungle',
            6:'Labs',
            7:'The Palace',
            107:'Y.V\'s Crib'}

skindict = {0:'A',
            1:'B',
            2:'C'}



def printrun(nt, current=True):
    character = charlist[nt['char']]
    world = areadict[nt['world']]
    area = nt['level']
    skin = skindict[nt['skin']]
    loop = nt['loops']
    wepA = weplist[nt['wepA']]
    wepB = weplist[nt['wepB']]
    health = nt['health']
    healthstr = '['+'#'*health+']'
    if health == 0:
        healthstr = ''
    crown = crownlist[int(nt['crown'])]
    radlevel = nt['charlvl']
    mutraw = nt['mutations']
    mutations = []
    for x in range(0,len(mutraw)):
        if mutraw[x] == '1':
            mutations.append(mutlist[x].format(character))
    runtype = nt['type']
    lasthitindex = nt['lasthit']
    if lasthitindex == -1:
        lasthit = None
    else:
        lasthit = enemylist[lasthitindex]
    if current:
        if runtype == 'daily':
            print('CURRENT RUN (DAILY)')
        elif runtype == 'weekly':
            print('CURRENT RUN (WEEKLY)')
        elif runtype == 'hard':
            print('CURRENT RUN (HARD)')
        else:
            print('CURRENT RUN')
    else:
        if runtype == 'daily':
            print('PREVIOUS RUN (DAILY)')
        elif runtype == 'weekly':
            print('PREVIOUS RUN (WEEKLY)')
        elif runtype == 'hard':
            print('PREVIOUS RUN (HARD)')
        else:
            print('PREVIOUS RUN')
    print('='*20)
    print()
    print('CHARACTER - ' + character)
    print('HEALTH {} - {}'.format(healthstr,str(health)))
    print('LEVEL ' + str(radlevel))
    print()
    print('{} - {}'.format(world,str(area)))
    print()
    if wepA != None:
        print('Weapon A - ' + wepA)
    if wepB != None:
        print('Weapon B - ' + wepB)
    if wepA == None and wepB == None:
        print('No weapon!')
    if crown != None:
        print('Crown - Crown of ' + crown)
    print()
    if lasthit != None:
        if health == 0:
            print('Died to - ' + lasthit)
        else:
            print('Last hit - ' + lasthit)
    print()
    if mutations != []:
        print('Mutations - ')
        for x in mutations:
            print('   ' + x)
    
def getjson(url):
    page = requests.get(url).text
    nt = json.loads(page)
    current = nt['current']
    previous = nt['previous']
    return current, previous

while True:
    time.sleep(0.5)
    current, previous = getjson(nturl)
    print('\n'*40)
    if previous != None:
        printrun(previous, False)
        print('\n\n')
    if current != None:
        printrun(current, True)
    else:
        print('Nothing running')
