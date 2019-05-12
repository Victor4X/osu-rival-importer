import os
from ConfigParser import SafeConfigParser

config = SafeConfigParser()

key = ""
osudir = ""

if os.path.isfile('./config.ini'):
    config.read('config.ini')

    print("Would you like to import your previous osu! directory and api key? (y/n)") 

    if str(input()).lower() == "y":
        try:
            key = config.get('main', 'key')
        except:
            key = ""
        try:
            osudir = config.get('main', 'osudir')
        except:
            osudir = ""
    
    checksettings()

else:
    config.read('config.ini')
    config.add_section('main')

    print("Please input your osu! api key:")
    key = str(input())
    config.set('main', 'key', key)

    print("Please input your osu! directory location:")
    osudir = str(input())
    config.set('main', 'osudir', osudir)

    checksettings()

        
def checksettings():

    try:
        config.add_section('main')
    except:
        pass

    if key == "" or not len(key) == 40:
        print("key corrupt of missing, please input your osu! api key: (https://osu.ppy.sh/p/api)")
        key = str(input())
        config.set('main', 'osudir', osudir)
    
    else:
        with open('config.ini', 'w') as f:
            config.write(f)

    if not os.path.exists(osudir):
        print("osu! directory corrupt of missing, please input your osu! directory:")
        key = str(input())
        keyfile = open('key.txt', 'w')
        keyfile.write(key)

    else:
        with open('config.ini', 'w') as f:
            config.write(f)

    checksettings()

print("please input the username or id of your rival:")
rival = str(input())




