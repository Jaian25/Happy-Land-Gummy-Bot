import json
from signal import set_wakeup_fd

priority = {
    "Background Color" : 1 , 
    "Arms" : 3 ,
    "Bear Den" : 2 ,
    "Body" : 5, 
    "Ears" : 8 , 
    "Eyes" : 10,
    "Head" : 9,
    "Legs" : 4,
    "Mouth" : 7,
    "Neck" : 6,
    "Rare" : 11
}

def get_traits(token):
    f = open('./happyland-gummy-bears-official.json')
    jsonn = json.load(f)
    traits = []
    eyesFlag = 0 
    earsFlag = 0 
    body = 0 
    for data in jsonn[token]:
        type = data[0]
        value = data[1]
        traits.append((type , value))
        if type == 'Eyes':
            eyesFlag = 1
        if type == 'Ears':
            earsFlag = 1
        if type == 'Bear Den':
            body = value


    if eyesFlag == 0 :
        traits.append(('Eyes' , 'normal-eyes'))
    if earsFlag == 0 :
        traits.append(('Ears' , f'normal-ears/{body}-normal-ears'))
    traits = Sort(traits)
    #GETISHHHH
    if(('Eyes' , 'normal-eyes') in traits) and (('Head' , 'eye-head-bandage') in traits):
        eye = traits.index(('Eyes' , 'normal-eyes'))
        head = traits.index(('Head' , 'eye-head-bandage'))
        traits[eye], traits[head] = traits[head] , traits[eye]

    return traits

def Sort(ab):
    for i in range(len(ab)):
        for j in range(len(ab)):
            if priority[ab[i][0]] < priority[ab[j][0]]:
                temp = ab[i]
                ab[i] = ab[j]
                ab[j] = temp
    return ab

#print(get_traits('9345'))
#print(get_traits("60"))