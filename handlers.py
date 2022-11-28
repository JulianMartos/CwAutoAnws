from math import radians

from telethon.client import messages
from settings import cw_id, wolf_pve_bot_id, withdraw_group, moon_orderbot_id, ss_chat_id, orderbot_id, squad_id
from patterns import show_me_pattern, full_stamina_pattern, quest_pattern, pledge_pattern, no_stamina_pattern, foray_pattern, mods_pattern, alive_pattern, dead_pattern, trader_pattern, withdraw_pattern, withdrawing_pattern
import asyncio, schedule
from random import randint, choice
from scripter import statsPlayer
from telethon import events, types, Button

schedule1 = schedule.Scheduler()
stats = {}
loop = asyncio.get_event_loop()

rango1 = '/ga_def'
rango2 = '/ga_def'
rango3 = '/ga_def'



def getOrder(stat):
    if stat.lvl < 40:
        return rango1
    elif stat.lvl >60:
        return rango3
    else: return rango2

def startArenas(cliente):
    loop.create_task(doArenas(cliente))

def rangerAtk():
    for id in stats:
        if stats[id].rangerAtkTime == True:
            loop.create_task(get_target_and_atk(stats[id]))

def RegularAtk():
    for id in stats:
        if stats[id].atk == None:
            pass
        elif stats[id].atk:
            loop.create_task(get_target_and_atk(stats[id]))
        else:
            loop.create_task(send_def(stats[id].client))
    stats[745224074].hunt = True

    loop.create_task(forward_msg(stats[745224074].client, '/g_list', '**🌑Sharks Rise**'))

def getInfoFromMe(st):
    tulevel = 0
    currenthp = 0
    currentstam = 0
    maxhp = 0 
    maxstam = 0
    idx = st.find("Stamina: ")
    idy = st.find("⏰",idx)
    if idy == -1:
        idy = st.find("\n",idx)

    subs = st[idx+9:idy]
    currentstam = (int)(subs.split("/")[0])
    maxstam = (int)(subs.split("/")[1])

    idx = st.find("🏅Level: ")
    tulevel = (int)(st[idx + 8:idx +10])

    idx = st.find("❤️Hp: ")
    idy = st.find("Stamina: ")
    subs = st[idx+6:idy-1]
    
    currenthp = (int)(subs.split("/")[0])
    maxhp = (int)(subs.split("/")[1]) 

    return [currentstam,tulevel,maxhp, maxstam, currenthp]

async def basic_info(client, text, order):
    me = await client.get_me()
    print(me.username)
    print(text)
    print(order)
    print('\n\n\n')

async def register(client, attack=None, quest=None, hunt=None, arenaTime=None, favQuest=None, forwardMobsTo= None, traderId = None, rngrAtk=None, alliance = False):
    global stats
    user = await client.get_me()
    stats[user.id] = statsPlayer(client, atk=attack, doQuest=quest, hunt=hunt, arenaTime=arenaTime, favQuest=favQuest, forwardMobsTo=forwardMobsTo, traderId=traderId, rangerAtkTime=rngrAtk, alliance=alliance)
    print('registro de %i' %user.id)

async def getId(client):
    user = await client.get_me()
    return user.id

async def send_orders(client, order):
    if order != '🛡Defend' and order != '/g_def SIR':
        await client.send_message('chtwrsbot',"⚔Attack")
    await asyncio.sleep(3)
    await client.send_message('chtwrsbot',order)

async def doArenas(cliente):
    await cliente.send_message('chtwrsbot', '▶️Fast fight'),
    await asyncio.sleep(randint(350, 400))
    await cliente.send_message('chtwrsbot', '▶️Fast fight'),
    await asyncio.sleep(randint(350, 400))
    await cliente.send_message('chtwrsbot', '▶️Fast fight'),
    await asyncio.sleep(randint(350, 400))
    await cliente.send_message('chtwrsbot', '▶️Fast fight'),
    await asyncio.sleep(randint(350, 400))
    await cliente.send_message('chtwrsbot', '▶️Fast fight'),

async def scheduleArenas():
    global schedule1
    await asyncio.sleep(20)
    for scripter in stats:
        if stats[scripter].arenaTime is not None:
            stats[scripter].arenaDeamon = schedule1.every().day.at(stats[scripter].arenaTime).do(startArenas, cliente=stats[scripter].client)
            print('Las Arenas empezaran a las %s' %stats[scripter].arenaTime)
    schedule1.every().day.at('10:15').do(rangerAtk)
    schedule1.every().day.at('18:15').do(rangerAtk)
    schedule1.every().day.at('02:15').do(rangerAtk)
    schedule1.every().day.at('10:56:15').do(RegularAtk)
    schedule1.every().day.at('18:56:15').do(RegularAtk)
    schedule1.every().day.at('02:56:15').do(RegularAtk)
    
async def check_schedule():
    while True:
        schedule1.run_pending()
        await asyncio.sleep(2)

async def get_target_and_atk(stat):
    stat.hunt = (False if stat.hunt != None else None)
    stat.doQuest = (False if stat.doQuest != None else None)
    if(stat.alliance):
        order = getOrder(stat)
        await send_alliance_orders(stat.client, order)
    else:
        await stats[745224074].client.get_dialogs()
        chat = await stats[745224074].client.get_entity(ss_chat_id)
        message = await stats[745224074].client.get_messages(chat, ids=types.InputMessagePinned())

        if ('⚔' in message.text):
            if ('⚔🌑' in message.text):
                target = '🛡Defend'
            else:        
                indexo = message.text.find("⚔")
                target = message.text[indexo+1:indexo+3]
        else:
            target= '🛡Defend'
        
        await asyncio.sleep(10)
        await send_orders(stat.client, target)

async def send_alliance_orders(cliente, orders):
    await asyncio.sleep(3)
    await cliente.send_message('chtwrsbot',orders)

async def send_def(cliente):
    await send_orders(cliente, '/g_def SIR')

async def forward_msg(client, msg_to_bot, msg_from_bot):
    await asyncio.sleep(120)
    async with client.conversation('chtwrsbot', timeout=300) as conv:
        await conv.send_message(msg_to_bot)
        msg = await conv.get_response()
        while (msg_from_bot not in msg.text):
            await conv.send_message(msg_to_bot)
            msg = await conv.get_response()

        await client.get_dialogs()
        chat = await client.get_entity(1280361206)
        await client.forward_messages(chat, msg)

#Bot Handlers

@events.register(events.NewMessage(pattern='/start'))
async def handle_StartBot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    welcomeMsg = 'Este es el bot de Control del Script\nLos comandos son:\n\n/status Para ver el estado de tus variables\n\n'
    if stat.atk is not None:
        welcomeMsg+= "/atk_on para coger las ordenes\n/atk_off para defender SIR\n/no_atk para no coger ordenes de attaque\n\n"
    if stat.doQuest  is not None:
        welcomeMsg+= "/quest_on para iniciar el autoquest\n/quest_off para detener el autoquest\n\n"
    if stat.hunt  is not None:
        welcomeMsg+= "/hunt_on para iniciar la caza de Mobs\n/hunt_off para detener la caza\n\n"
    if stat.arenaTime  is not None:
        welcomeMsg+= "/set_arena_time [hh:mm] para cambiar la hora que se hace las arenas(valido a partir del proximo dia)\n\n"
    if stat.traderId  is not None:
        welcomeMsg+= "/set_trader_id para cambiar el item del trader\n\n"
    if stat.favQuest  is not None:
        welcomeMsg+= "/change_quest_target para cambiar el lugar donde se va en Quest"
    await event.respond(welcomeMsg)

@events.register(events.NewMessage(pattern='/quest_on'))
async def handle_quest_on_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.doQuest = True
    await event.respond(str(stat))


@events.register(events.NewMessage(pattern='/test'))
async def handle_test(event):
    print('start Test')


@events.register(events.NewMessage(pattern='/set_order', incoming=True))
async def set_order(event):
    global rango1,rango2,rango3
    async with event.client.conversation(event.message.peer_id.user_id, timeout=300) as conv:
        await conv.send_message('Envie la orden Para el rango 20-40')
        orden1 = await conv.get_response()
        await conv.send_message('Envie la orden Para el rango 40-60')
        orden2 = await conv.get_response()
        await conv.send_message('Envie la orden Para el rango 60+')
        orden3 = await conv.get_response()

        rango1 = orden1.text
        rango2 = orden2.text
        rango3 = orden3.text

        await conv.send_message('Rango 1 = %s\n\nRango 2 = %s\n\nRango3 = %s'%(rango1, rango2, rango3))


@events.register(events.NewMessage(pattern='/get_orders'))
async def handle_get_orders(event):
    await event.respond('Rango 1 = %s\n\nRango 2 = %s\n\nRango3 = %s'%(rango1, rango2, rango3))

@events.register(events.NewMessage(pattern='/quest_off'))
async def handle_quest_off_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.doQuest = False
    await event.respond(str(stat))

@events.register(events.NewMessage(pattern='/hunt_on'))
async def handle_hunt_on_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.hunt = True
    await event.respond(str(stat))

@events.register(events.NewMessage(pattern='/hunt_off'))
async def handle_hunt_off_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.hunt = False
    await event.respond(str(stat))


@events.register(events.NewMessage(pattern='/no_atk'))
async def handle_no_atk_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.atk = None
    await event.respond(str(stat))

@events.register(events.NewMessage(pattern='/atk_on'))
async def handle_atk_on_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.atk = True
    await event.respond(str(stat))

@events.register(events.NewMessage(pattern='/atk_off'))
async def handle_atk_off_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.atk = False
    await event.respond(str(stat))

@events.register(events.NewMessage(pattern='/set_arena_time'))
async def handle_set_arena_time_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.arenaTime = event.message.text.split(' ')[1]
    schedule1.cancel_job(stat.arenaDeamon)
    stat.arenaDeamon = schedule1.every().day.at(stat.arenaTime).do(startArenas, cliente=stat.client)    
    await event.respond(str(stat))

@events.register(events.NewMessage(pattern='/set_default_order'))
async def handle_set_default_order_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.defaultOrder = event.message.text.split(' ')[1]
    await event.respond(str(stat))

@events.register(events.NewMessage(pattern='/set_trader_id'))
async def handle_set_trader_id_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    stat.traderId = event.message.text.split(' ')[1]
    await event.respond(str(stat))

@events.register(events.NewMessage(pattern='/status'))
async def handle_status_bot(event):
    id = event.peer_id.user_id
    stat = stats[id]
    await event.respond(str(stat))


buttonList = [Button.inline('Forest', data='Forest'),Button.inline('Swamp', data='Swamp'),Button.inline('valley', data='Valley')]
@events.register(events.NewMessage(pattern='/change_quest_target'))
async def handle_quest_change_bot(event):
    id = event.peer_id.user_id
    listEvents = stats[id].favQuest
    await event.reply( '0 = 🌲Forest\n1 = 🍄Swamp\n2 = 🏔Mountain Valley\nTu lista Actual es: %s' %listEvents, buttons=[buttonList])

@events.register(events.CallbackQuery())
async def handleButtomBot(event):
    listEvents = stats[event.original_update.user_id].favQuest
    if event.data == b'Forest':
        if 0 in listEvents:
            listEvents.remove(0)
        else: listEvents.append(0)
    elif event.data == b'Swamp':
        if 1 in listEvents:
            listEvents.remove(1)
        else: listEvents.append(1)
    elif event.data == b'Valley':
        if 2 in listEvents:
            listEvents.remove(2)
        else: listEvents.append(2)
    listEvents.sort()
    await event.edit(text='0 = 🌲Forest\n1 = 🍄Swamp\n2 = 🏔Mountain Valley\nTu lista Actual es: %s' %listEvents, buttons=buttonList)
    await event.answer('Quest Favorito Cambiado!', alert=True) 


#scrips Handlers

@events.register(events.NewMessage(from_users=cw_id, pattern=show_me_pattern, incoming=True))
async def handle_updateMe(event):
    me = getInfoFromMe(event.message.text)
    id = await getId(event.client)
    stat = stats[id]
    stat.stam = me[0]
    stat.hp = me[4]
    stat.maxHp = me[2]
    stat.lvl = me[1]

@events.register(events.NewMessage(from_users=cw_id, pattern=full_stamina_pattern, incoming=True))
async def handle_Full_Stamina(event):     
    id = await getId(event.client)
    stat = stats[id]
    stat.doQuest = True
    await event.respond("🗺Quests") 

@events.register(events.NewMessage(from_users=cw_id, incoming=True))
async def handle_stam_deplete(event):      
    msg = event.message
    if ("You received:" in msg.message and "stands victorious over" not in msg.message) or "It was a really nice and sunny day," in msg.message or "Looking at the overcast sky you decide to take a day off" in msg.message or "You fell asleep and in your dream there was a" in msg.message or "Walking through the swamp, you found yourself surrounded by" in msg.message or "As you were about to head out for an adventure" in msg.message  or "Mrrrrgl mrrrgl mrrrrrrgl mrrrgl. Mrrrrrrrrrrrgl mrrrrgl mrrrrrrrgl mrrrrrrgl mrrrrrrrrl. Mrrrrrgl." in msg.message or "As you were strolling through the forest" in msg.message or "It was a cool and refreshing night" in msg.message or "In the forest you came across a tavern" in msg.message or "In the forest you met a redhead woman" in msg.message or "Nothing interesting happened." in msg.message or "You found yourself in a land you where you did not want to appear again." in msg.message or "Wandering around, you saw a little golden ball flying around" in msg.message:  
        id = await getId(event.client)
        stat = stats[id]
        if stat.doQuest:
            await asyncio.sleep(randint(10,15))
            await event.respond("🗺Quests")

@events.register(events.NewMessage(from_users=cw_id, pattern=quest_pattern, incoming=True))
async def Handle_Do_quest(event):
    id = await getId(event.client)
    stat = stats[id]
    if stat.doQuest:
        if '🔥' in event.message.text:
            temp = event.message.text.split('\n\n')
            for i in range(0,3):
                if '🔥' in temp[i]:
                    await asyncio.sleep(2)
                    await event.message.buttons[0][i].click()
        else:
            await asyncio.sleep(2)
            await event.message.buttons[0][choice(stat.favQuest)].click()

@events.register(events.NewMessage(from_users=cw_id, pattern=pledge_pattern, incoming=True))
async def handle_pldege_accept(event):
    await asyncio.sleep(randint(5,15))
    await event.respond("/pledge")   
        
@events.register(events.NewMessage(from_users=cw_id, pattern=foray_pattern, incoming=True))
async def handle_Stop_Foray(event):
    await asyncio.sleep(randint(15,30))
    await event.message.buttons[0][0].click()
    me = await event.client.get_me()
    print(me.username)

@events.register(events.NewMessage(from_users=cw_id, pattern=mods_pattern, incoming=True))
async def handle_Mods(event):
    id = await getId(event.client)
    stat = stats[id]
    if stat.forwardMobsTo is not None:
        await asyncio.sleep(1)
        await event.client.get_dialogs()
        temp = await event.client.get_entity(stat.forwardMobsTo)
        await asyncio.sleep(16)
        await event.client.forward_messages(temp, event.message)

@events.register(events.NewMessage(pattern=mods_pattern, incoming=True))
async def handle_bichos_hunt(event):
    p=event.text.find("lvl.")    
    level=int(event.text[p+4:p+6])
    id = await getId(event.client)
    stat = stats[id]
    if (level > stat.lvl-10 and level < stat.lvl+5) and stat.stam != 0 and stat.hp > stat.maxHp/2 and stat.hunt == True:
        await event.client.send_message('chtwrsbot',event.text) 

@events.register(events.NewMessage(from_users=cw_id, pattern=alive_pattern, incoming=True))
async def handle_if_alive(event):
    await asyncio.sleep(2)
    await event.message.buttons[0][0].click()
    await asyncio.sleep(2)
    await event.message.buttons[0][1].click()  
    await asyncio.sleep(2)
    await event.respond("🏅Me")

@events.register(events.NewMessage(from_users=cw_id, pattern=dead_pattern, incoming=True))
async def handle_if_death(event):
    await asyncio.sleep(2)
    await event.message.buttons[0][0].click()
    await asyncio.sleep(2)
    await event.message.buttons[0][1].click()  
    await asyncio.sleep(2)
    await event.respond("🏅Me")

@events.register(events.NewMessage(from_users=cw_id, pattern=trader_pattern, incoming=True))
async def handle_trader(event):
    id = await getId(event.client)
    stat = stats[id]
    if(stat.traderId is not None):
        idxq = event.message.text.find("carry")
        cant = event.message.text[idxq+6:idxq+9]
        await asyncio.sleep(2)
        await event.respond("/sc " + stat.traderId + " " + (str)(cant))

@events.register(events.NewMessage(from_users=wolf_pve_bot_id, incoming=True))
async def handle_click_pve(event):
    id = await getId(event.client)
    stat = stats[id]
    url = event.message.buttons[0][0].url
    if stat.stam != 0 and stat.hp > stat.maxHp/2 and stat.hunt == True:
        await event.client.send_message('chtwrsbot', url.split('=')[1])


#SACAR Y ENVIAR WITHDRAWS
@events.register(events.NewMessage(from_users=cw_id, pattern=withdrawing_pattern, incoming=True))
async def handle_withdrawing(event):
    await asyncio.sleep(1)
    await event.client.get_dialogs()
    temp = await event.client.get_entity(withdraw_group)
    await event.client.send_message(temp, event.message.text)

@events.register(events.NewMessage(chats=withdraw_group, pattern=withdraw_pattern, incoming=True))
async def handle_withdraw(event):
    await asyncio.sleep(1)
    await event.client.send_message('chtwrsbot', event.message.text)


@events.register(events.NewMessage(from_users=orderbot_id, chats=squad_id, incoming=True))
async def handle_order2(event):
    await stats[969228070].client.send_message('PastaPerla', event.message.text)
    await asyncio.sleep(2)
    await stats[969228070].client.send_message('lunarfeedbackbot', event.message.text)
    


@events.register(events.NewMessage(chats=1472420474, incoming=True))
async def handle_order3(event):
    await stats[745224074].client.get_dialogs()
    await stats[969228070].client.get_dialogs()
    b = await stats[745224074].client.get_entity(event.message.from_id)
    await event.client.get_dialogs()
    temp = await stats[969228070].client.get_entity(1586737785)
    await stats[969228070].client.send_message(temp, "%s\n%s" %(b.username, event.message.text ))
    

    #cloud@152.206.118.136