from PIL import Image
from back import get_traits
import threading
import random


#Sequence > background , bear den , arms , legs , body-trats, necks , mouths, ears , head, eye, rare

def overlap(img1 , img2):
    img3 = img1
    img3.paste(img2 , (0 , 0) , mask = img2)
    return img3

def generate_valentine(token , banned ):
    #print("here")
    traits = get_traits(token)
    fl = 0 
    img = 0
    bear_den = 'salmon'
    eye_flag = 0 
    ear_flag = 0
    suitId = random.randint(0,4)
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
        if type == 'Bear Den':
            fl = 1
            img = Image.open(f"./Traits/{type}/{value}-bear-head.png")
            img2 = Image.open(f"./Traits/{type}/{value}-bear-body.png")
            if suitId == 1:
                img = overlap(img2 , img)
            continue 

        if fl == 0 : 
            img = Image.open(f"./Traits/{type}/{value}.png")
            fl = 1
        img1 = Image.open(f"./Traits/{type}/{value}.png")
        img = overlap(img , img1)

    #####Looop endss
    img1 = Image.open(f"./Layers/vday/{suitId}.png")
    img = overlap(img , img1)
    if ear_flag == 0 :
        img1 = Image.open(f"./Traits/Ears/normal-ears/{bear_den}-normal-ears.png")
        img = overlap(img , img1)
    if eye_flag == 0 :
        img1 = Image.open(f"./Traits/Eyes/normal-eyes.png")
        img = overlap(img , img1)
    #img.save(f'./merge/{token}.png')


    return img