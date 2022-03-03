
from PIL import Image
from back import get_traits
import threading
import random
from valentine_gen import generate_valentine
# Opening the primary image (used in background)
#img1 = Image.open(r"gunmetal.png")
  
# Opening the secondary image (overlay image)
# img12 = Image.open(r"gunmetal-normal-ears.png")
# img = overlap(img1, img12)

# Displaying the image
#img.show()
#img1.save("hat-with-ear.png")

#Sequence > background , bear den , arms , legs , body-trats, necks , mouths, ears , head, eye, rare



def overlap(imgBack , imgFor , shiftX = 0 , shiftY = 0):
    img3 = imgBack
    img3.paste(imgFor , (shiftX , shiftY) , mask = imgFor)
    return img3

def generate(token , banned , version = 0):
    #print("here")
    traits = get_traits(token)
    fl = 0 
    img = 0
    bear_den = 'salmon'
    eye_flag = 0 
    ear_flag = 0
    for type,value in traits:
        if type == 'Bear Den':
            bear_den = value
    for type, value in traits : 
        if type in banned:
            continue

        if type == 'Mouth':
            if value == 'freckles':
                img1 = Image.open(f"./Traits/{type}/freckles/{bear_den}-{value}.png")
            else:
                img1 = Image.open(f"./Traits/{type}/{value}.png")
            img = overlap(img , img1)
            continue

        
        if type == 'Ears':
            ear_flag = 1
            if value == 'right-ear-stitches':
                img1 = Image.open(f"./Traits/{type}/normal-ears/{bear_den}-normal-ears.png")
                img = overlap(img , img1)
                img1 = Image.open(f"./Traits/{type}/normal-ear-traits/stitched-ear.png")
                img = overlap(img , img1)
                continue
            if value == 'bitten-ears-gold-earring':
                img1 = Image.open(f"./Traits/{type}/bitten-ears/{bear_den}-bitten-ears.png")
                img = overlap(img , img1)
                img1 = Image.open(f"./Traits/{type}/bitten-ear-traits/left-ear-gold-earring.png")
                img = overlap(img , img1)
                continue
            if value == 'bitten-ears-diamond-earring':
                img1 = Image.open(f"./Traits/{type}/bitten-ears/{bear_den}-bitten-ears.png")
                img = overlap(img , img1)
                img1 = Image.open(f"./Traits/{type}/bitten-ear-traits/left-ear-diamond-earring.png")
                img = overlap(img , img1)
                continue
            if value == 'bitten-ears-silver-earring':
                img1 = Image.open(f"./Traits/{type}/bitten-ears/{bear_den}-bitten-ears.png")
                img = overlap(img , img1)
                img1 = Image.open(f"./Traits/{type}/bitten-ear-traits/left-ear-silver-earring.png")
                img = overlap(img , img1)
                continue
            if value == 'bitten-ears':
                img1 = Image.open(f"./Traits/{type}/bitten-ears/{bear_den}-{value}.png")
                img = overlap(img , img1)
                continue
            img1 = Image.open(f"./Traits/{type}/normal-ears/{bear_den}-normal-ears.png")
            img2 = Image.open(f"./Traits/{type}/normal-ear-traits/{value}.png")
            img1 = overlap(img1 , img2)
            img = overlap(img , img1)
            continue
        if type == 'Eyes':
            eye_flag = 1
        if fl == 0 : 
            img = Image.open(f"./Traits/{type}/{value}.png")
            fl = 1
        img1 = Image.open(f"./Traits/{type}/{value}.png")
        img = overlap(img , img1)
    if ear_flag == 0 :
        img1 = Image.open(f"./Traits/Ears/normal-ears/{bear_den}-normal-ears.png")
        img = overlap(img , img1)
    if eye_flag == 0 :
        img1 = Image.open(f"./Traits/Eyes/normal-eyes.png")
        img = overlap(img , img1)
    #img.save(f'./merge/{token}.png')
    return img













def changeBackground(token , address):
    imgFor = generate(token , ['Background Color'])
    imgBack = Image.open(f'{address}')
    img = overlap(imgBack , imgFor)
    return img

def valentine(token):
    img = changeBackground(str(token),f'./Layers/Valentine/bg.png')
    bemy = Image.open(f'./Layers/Valentine/bemy.png')
    logo = Image.open(f'./Layers/Valentine/logo.png')
    img = overlap(img , bemy)
    img = overlap(img , logo)
    #img = img.resize((1000 , 1000))
    return img

def valentineV2(token):
    imgFor = generate_valentine(token , ['Background Color' , 'Arms' , 'Body'  , 'Rare' , 'Legs'] )
    imgback = Image.open(f'./Layers/vday/bg.png')
    img = overlap(imgback , imgFor)
    #img = img.resize((1000 , 1000))
    return img

def removeBackground(token):
    img = generate(token , ['Background Color'])
    #img = img.resize((1000 , 1000))
    return img

def monsterlab(img):
    imgbg = Image.open(f'./Layers/monsterlab-1/kraken-bg.png')
    img = img.resize((3800 ,3800))
    img = overlap(imgbg , img , 950 , 80 )
    boat = Image.open(f'./Layers/monsterlab-1/boat.png')
    img = overlap(img , boat)
    return img

def will_u_be(img):
    imgback = Image.open(f'./Layers/vday/bg.png')
    img = overlap(imgback , img)
    #img = img.resize((1000 , 1000))
    return img
def normal_background(img, token) : 
    traits = get_traits(token)
    for type, value in traits:
        if type == 'Background Color':
            img1 = Image.open(f"./Traits/{type}/{value}.png")
            img = overlap(img1 , img)
            return img

#valentineV2("6969").show()
#Accessories

def valentine_suit(token):
    imgFor = generate_valentine(token , ['Background Color' , 'Arms' , 'Body'  , 'Rare' , 'Legs'] )
    #img = img.resize((1000 , 1000))
    return imgFor
