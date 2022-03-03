import imp
from logging import raiseExceptions
from discord import client
from discord.ext import commands
from discord.ext.commands.errors import DisabledCommand
from config import *
from generator import *
from PIL import Image
import discord
bot = commands.Bot(command_prefix='!')

fun_layers = ['valentine','removebg','monsterlab','suit','be_my' , 'no_bg' , 'peace_suit' , 'peacebg' , 'peace']

items = ['suit' , 'peace_suit']

backgrounds = ['monsterlab','be_my' , 'peacebg']

utils = ['valentine','removebg' ,'peace']

@bot.event
async def on_ready():
    #bot.load_extension('cog1')
    print("Happy Land Bot Up")

@bot.command()
async def info(ctx):
    
    message =  '''```Thanks for using the Happy Land Gammy Bot
Usage: !call <token_id> <accessory_keywords>

Available Accessories : 

Type 1: Items
- suit - Bears come up with four possible suit items with flowers in hands
- peace_suit - Bears come up with two possible peace loving suit 

Type 2: Backgrounds
- monsterlab - CML x HLGB collab
- be_my - Be my valentine background
- peacebg - Love peace not war background

Type 3: Utility

-removebg : Removes background
-valentine : 4 valentines outfits & background 
-peace : 2 Peace outfits & background

Example - !call 1234 suit+monsterlab     --> valentines with CML x HLGBcollab
```''' 
    await ctx.send(message)
@bot.command()
async def call(ctx, token , layers=''):

    try:
        if ctx.channel.id!=935741545796223016:
            await ctx.send("Please use Bear-lair channel")
            return

    except:
        await ctx.send("Please use Bear-lair channel")
        return
    try:
     
        all = layers.split('+')
        if layers == '':
            all = []
        all = list(set(all))
        first = []
        second = []
        third = []
    
        for indi in all : 
            if indi in items:
                first.append(indi)
            elif indi in backgrounds:
                second.append(indi)
            elif indi in utils:
                third.append(indi)
            else:
                raiseExceptions()
        
        a = len(first) 
        b = len(second)
        c = len(third)
     
        if b > 1 : 
            await ctx.send("Please use at most one background")
            return
        if c > 1 :
            await ctx.send("You can use at most one Utils")
            return
        if c == 1 and (a >= 1 or b>=1):
            await ctx.send("Utils are special features and can not be merged with other items")
            return
        if c == 1:
            layer = third[0]
            if layer == 'removebg':
                await ctx.send("Removing background")
                img = removeBackground(str(token))
                img = img.resize((1000 , 1000))
                img.save(f'./temp/{token}-{layer}-temp.png')
                file = discord.File(f'./temp/{token}-{layer}-temp.png')
                await ctx.send(file = file)
            elif layer == 'valentine':
                await ctx.send("Generating your Valentine :heart:")
                img = valentineV2(str(token))
                img = img.resize((1000 , 1000))
                img.save(f'./temp/{token}-{layers}-temp.png', quality = 50)
                file = discord.File(f'./temp/{token}-{layers}-temp.png')
                await ctx.send(file = file)
            elif layer == 'peace':
                await ctx.send("Love Peace X Not War")
                img = peace_combo(str(token))
                img = img.resize((1000 , 1000))
                img.save(f'./temp/{token}-{layers}-temp.png', quality = 50)
                file = discord.File(f'./temp/{token}-{layers}-temp.png')
                await ctx.send(file = file)
            else:
                raiseExceptions()
            return
        img1 = 0
        image_flag = 0
        for i in first:
            if i == 'suit':
                img = valentine_suit(str(token))
                if image_flag == 0 : 
                    image_flag = 1
                    img1 = img
                else:
                    img1 = overlap(img1 ,img)
            if i == 'peace_suit':
                img = peace_suit(str(token))
                if image_flag == 0 : 
                    image_flag = 1
                    img1 = img
                else:
                    img1 = overlap(img1 ,img)
                
        if a == 0 :
            img1 = generate(str(token) , ['Background Color'])
   
        for i in second:
            if i == 'monsterlab':
                img1 = monsterlab(img1)
            if i == 'be_my':
                img1 = will_u_be(img1)
            if i == 'peacebg':
                img1 = peace_back(img1)
        if b == 0:
            img1 = normal_background(img1 , token)
        
        img1 = img1.resize((1000 , 1000))
        img1.save(f'./temp/{token}-{layers}-temp.png', quality = 50)
        file = discord.File(f'./temp/{token}-{layers}-temp.png')
        await ctx.send(file = file)
        
    except Exception as e:
        print(e)
        await ctx.send("Invalid keywords")


bot.run(discord_bot_token)