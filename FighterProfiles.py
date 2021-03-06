from PIL import Image, ImageTk

from HeroClass import*

batman = Hero("BATMAN")
batman.setPower("Strength", 10, 0.95)
batman.setPower("Tech", 60, 0.4)
batman.setPower('Batarang', 40, 0.7)
batman.setPower('Upper cut', 25, 0.9)
batman.color = 'Black'
batman_img = Image.open('Fighters/BatmanIcon.png')
batman_img = batman_img.resize((100, 100), Image.ANTIALIAS)

joker = Hero("JOKER")
joker.setPower("Dogs", 30, 0.6)
joker.setPower("Acid Gun", 50, 0.5)
joker.setPower('Poison', 25, 0.8)
joker.setPower('Sneak', 15, 1.0)
joker.color = 'Green'
joker_img = Image.open('Fighters/JokerIcon.png')
joker_img = joker_img.resize((100,100),Image.ANTIALIAS)

superman = Hero('SUPERMAN')
superman.setPower('Heat vision', 40, 0.6)
superman.setPower('Super strength', 50, 0.7)
superman.setPower('Flying punch', 30, 0.75)
superman.setPower('Super breath', 20, 0.85)
superman.color = 'red'
superman_img = Image.open('Fighters/SupermanIcon.png')
superman_img = superman_img.resize((100,100),Image.ANTIALIAS)

bane = Hero('BANE')
bane.setPower('Charge', 35, .9)
bane.setPower('Throw', 25, 1)
bane.setPower('Bane Bomb', 70, 0.3)
bane.setPower('Merc Elbow', 30, .95)
bane.color = 'grey'
bane_img = Image.open('Fighters/BaneIcon.png')
bane_img = bane_img.resize((100,100),Image.ANTIALIAS)

aquaman = Hero('AQUAMAN')
aquaman.setPower('Trident Slash', 20, 0.95)
aquaman.setPower('Shark attack', 55, 0.6)
aquaman.setPower('Atlantean rage', 70, 0.45)
aquaman.setPower('Tidal wave', 40, 0.65)
aquaman.color = 'teal'
aquaman_img = Image.open('Fighters/AquamanIcon.png')
aquaman_img = aquaman_img.resize((100,100),Image.ANTIALIAS)

darkseid = Hero('DARKSEID')
darkseid.setPower('Omega Blast', 50, 0.55)
darkseid.setPower('Flying knee', 35, 0.75)
darkseid.setPower('Dark lord', 45, 0.45)
darkseid.setPower('Dark matter', 15, 1.0)
darkseid.color = 'black'
darkseid_img = Image.open('Fighters/DarkseidIcon.png')
darkseid_img = darkseid_img.resize((100,100),Image.ANTIALIAS)

fighters = [batman, joker, superman, bane, aquaman, darkseid]