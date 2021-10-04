from math import trunc
from re import A
from data import api_id, api_hash, bot_string_session, my_string_session, alt_string_session, cathy_string_session, samuel_string_session, massi_string_session, isma_string_session, bilbo_string_session, japs_string_session, noris_string_session,electro_string_session, carola_string_session, shay_string_session, manu_string_sessio, muffin_string_session, manualt_string_session, carlos_all_ss, carlos_all_marta_ss, carlos_lugo_ss, yisus_string_session, yisus_clau_ss, yisus_babi_ss, yisus_charly_ss, yisus_soyclau_ss, shay1_string_session, shay2_string_session, shay3_string_session, shay4_string_session, carlos_all_angela_ss, lachy_all_ss, noris2_string_session, alt_andrea_string_session
import asyncio, time, logging,handlers, schedule
from telethon import TelegramClient
from telethon.sessions import StringSession

a = lambda: loop.create_task(handlers.check_schedule())

async def me(list):
    await asyncio.sleep(20)
    meh = 1
    for client in list:
        print(meh)
        await client.send_message('chtwrsbot',"🏅Me")
        meh+=1

loop = asyncio.get_event_loop()
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


#CLIENTES
controlBot = TelegramClient(StringSession(bot_string_session), api_id, api_hash)
andrea = TelegramClient(StringSession(alt_andrea_string_session), api_id, api_hash)
yo = TelegramClient(StringSession(my_string_session), api_id, api_hash)
cathy = TelegramClient(StringSession(cathy_string_session), api_id, api_hash)
alt = TelegramClient(StringSession(alt_string_session), api_id, api_hash)
sam = TelegramClient(StringSession(samuel_string_session), api_id, api_hash)
mass = TelegramClient(StringSession(massi_string_session), api_id, api_hash)
isma = TelegramClient(StringSession(isma_string_session), api_id, api_hash)
bilbo = TelegramClient(StringSession(bilbo_string_session), api_id, api_hash)
japz = TelegramClient(StringSession(japs_string_session), api_id, api_hash)
noris = TelegramClient(StringSession(noris_string_session), api_id, api_hash)
noris2 = TelegramClient(StringSession(noris2_string_session), api_id, api_hash)
electro = TelegramClient(StringSession(electro_string_session), api_id, api_hash)
caro = TelegramClient(StringSession(carola_string_session), api_id, api_hash)
shay = TelegramClient(StringSession(shay_string_session), api_id, api_hash)
manu = TelegramClient(StringSession(manu_string_sessio), api_id, api_hash)
muffin = TelegramClient(StringSession(muffin_string_session), api_id, api_hash)
manualt =  TelegramClient(StringSession(manualt_string_session), api_id, api_hash)
carlos1 =  TelegramClient(StringSession(carlos_all_ss), api_id, api_hash)
carlos2 =  TelegramClient(StringSession(carlos_all_marta_ss), api_id, api_hash)
carlos3 =  TelegramClient(StringSession(carlos_lugo_ss), api_id, api_hash)
carlos5 =  TelegramClient(StringSession(carlos_all_angela_ss), api_id, api_hash)
y_soyKlau =  TelegramClient(StringSession(yisus_soyclau_ss), api_id, api_hash)
y_charly =  TelegramClient(StringSession(yisus_charly_ss), api_id, api_hash)
y_babi =  TelegramClient(StringSession(yisus_babi_ss), api_id, api_hash)
y_clau =  TelegramClient(StringSession(yisus_clau_ss), api_id, api_hash)
yisus =  TelegramClient(StringSession(yisus_string_session), api_id, api_hash)
shay1 =  TelegramClient(StringSession(shay1_string_session), api_id, api_hash)
shay2 =  TelegramClient(StringSession(shay2_string_session), api_id, api_hash)
shay3 =  TelegramClient(StringSession(shay3_string_session), api_id, api_hash)
shay4 =  TelegramClient(StringSession(shay4_string_session), api_id, api_hash)
lachy =  TelegramClient(StringSession(lachy_all_ss), api_id, api_hash)
print(time.asctime(), '-', 'Auto-replying...')


all_list = [yo, alt, andrea, cathy, sam , mass, isma, bilbo, japz, noris, noris2, electro, caro, shay, manu, muffin, manualt, carlos1,carlos2, carlos3, carlos5, y_soyKlau, y_charly, y_babi, y_clau, yisus, shay1, shay2,shay3,shay4, lachy]

quest_list = [yo, alt, cathy, andrea, mass, isma, bilbo, japz, noris2, electro, caro, shay, manu, muffin, manualt, carlos1, carlos2, carlos3, carlos5, y_soyKlau, y_charly, y_babi, yisus, shay1, shay2, shay3, shay4, lachy]

forward_mobs_list =  [yo, alt, cathy, mass, cathy, isma, bilbo, japz, noris2, caro, muffin, yisus, y_soyKlau]

hunt_list = [yo, cathy, isma, noris, electro, manu, muffin, yisus, y_soyKlau]

pledge_accept_list = [yo, sam, noris, electro, shay, manu, lachy] 

trader_list = [isma, yisus, andrea]

for client in all_list:
    client.add_event_handler(handlers.handle_updateMe)
    client.add_event_handler(handlers.handle_Stop_Foray)

for client in all_list:
    client.add_event_handler(handlers.handle_Full_Stamina)
    client.add_event_handler(handlers.handle_stam_deplete)
    client.add_event_handler(handlers.Handle_Do_quest)

for client in hunt_list:
    client.add_event_handler(handlers.handle_bichos_hunt)
    client.add_event_handler(handlers.handle_if_alive)
    client.add_event_handler(handlers.handle_if_death)

for client in pledge_accept_list:
    client.add_event_handler(handlers.handle_pldege_accept)

for client in trader_list:
    client.add_event_handler(handlers.handle_trader)

for client in forward_mobs_list:
    client.add_event_handler(handlers.handle_Mods)

yo.add_event_handler(handlers.handle_withdrawing)
yo.add_event_handler(handlers.handle_withdraw)
yo.add_event_handler(handlers.handle_click_pve)

electro.add_event_handler(handlers.handle_click_pve)

shay.add_event_handler(handlers.handle_order3)
shay.add_event_handler(handlers.handle_order2)


controlBot.add_event_handler(handlers.handle_StartBot)
controlBot.add_event_handler(handlers.handle_atk_on_bot)
controlBot.add_event_handler(handlers.handle_atk_off_bot)
controlBot.add_event_handler(handlers.handle_quest_off_bot)
controlBot.add_event_handler(handlers.handle_quest_on_bot)
controlBot.add_event_handler(handlers.handle_hunt_off_bot)
controlBot.add_event_handler(handlers.handle_hunt_on_bot)
controlBot.add_event_handler(handlers.handle_set_arena_time_bot)
controlBot.add_event_handler(handlers.handle_set_default_order_bot)
controlBot.add_event_handler(handlers.handle_set_trader_id_bot)
controlBot.add_event_handler(handlers.handle_status_bot)
controlBot.add_event_handler(handlers.handle_no_atk_bot)
controlBot.add_event_handler(handlers.handle_quest_change_bot)
controlBot.add_event_handler(handlers.handleButtomBot)
controlBot.add_event_handler(handlers.handle_test)
controlBot.add_event_handler(handlers.set_order)
controlBot.add_event_handler(handlers.handle_get_orders)


print('Done')
controlBot.start()
try: #yo
    yo.start()
    loop.create_task(handlers.register(yo, quest=False, hunt=True, favQuest=[1,2], arenaTime='15:30', rngrAtk=True, alliance = True, forwardMobsTo=1420240083))
except: print(2)
try: #alt
    alt.start()
    loop.create_task(handlers.register(alt, attack=True, quest=True, favQuest=[0,1,2], arenaTime='15:00', forwardMobsTo=1420240083, alliance = True))
except: print(3)
try: #Cathy
    cathy.start()
    loop.create_task(handlers.register(cathy, attack=True, quest=True, hunt=False , favQuest=[0,1,2], arenaTime='08:00', forwardMobsTo=1420240083, alliance = True))
except: print(4)
try: #samuel
    sam.start()
    loop.create_task(handlers.register(sam, attack=True, alliance = True))
except: print(5)
try: #mass
    mass.start()
    loop.create_task(handlers.register(mass, attack=True, quest=True, favQuest=[0], arenaTime='15:45', forwardMobsTo=1420240083, alliance = True))
except: print(6)
try: #isma
    isma.start()
    loop.create_task(handlers.register(isma, attack=True ,quest=False, hunt=True, arenaTime='14:00', favQuest=[1,2], forwardMobsTo=745224074, traderId='08', alliance = True))
except: print(8)
try: #imsa alts
    bilbo.start()
    loop.create_task(handlers.register(bilbo, attack=True, quest=True, favQuest=[0,2],arenaTime='13:00'  , forwardMobsTo=1420240083, alliance = True))
    japz.start()
    loop.create_task(handlers.register(japz, attack=True, quest=True, favQuest=[0,2],arenaTime='13:00'  , forwardMobsTo=1420240083, alliance = True))
except: print(9)
try: #noris
    noris.start()
    loop.create_task(handlers.register(noris, rngrAtk=True, hunt=True, alliance = True))
except: print(10)
try: #noris alt
    noris2.start()
    loop.create_task(handlers.register(noris2, attack=True, quest=True, favQuest=[0], arenaTime='06:00', forwardMobsTo=1420240083, alliance = True))
except: print(10.1)
try: #electro gay
    electro.start()
    loop.create_task(handlers.register(electro, quest=True, favQuest=[0,1,2], hunt=True, arenaTime='04:30', rngrAtk=True))
except: print(11)
try: #caro
    caro.start()
    loop.create_task(handlers.register(caro, attack=True ,quest=True, favQuest=[0], arenaTime='05:00'  , forwardMobsTo=1420240083, alliance = True))
except: print(12)
try: #shay
    shay.start()
    loop.create_task(handlers.register(shay, quest=True, favQuest=[0,1,2]  ))
except: print(14)
try: #manu
    manu.start()
    loop.create_task(handlers.register(manu, hunt=True, quest=False, favQuest=[0,2],))
except: print(15)
try: #muffin
    muffin.start()
    loop.create_task(handlers.register(muffin, quest=False, hunt=True, arenaTime='05:00', favQuest=[1,2]  , forwardMobsTo=1420240083, rngrAtk=True, alliance = True))
except: print(16)
try: #manu alt
    manualt.start()
    loop.create_task(handlers.register(manualt, quest=True, favQuest=[0,1,2]))
except: print(17)
try: #carlos alts
    carlos1.start()
    loop.create_task(handlers.register(carlos1, quest=False, attack=True, favQuest=[0,1,2], arenaTime='05:17', alliance = True))
except: print(22)
try: 
    carlos2.start()
    loop.create_task(handlers.register(carlos2, attack=False, quest=False, favQuest=[0,1,2], arenaTime='05:18'))
except: print(23)
try: 
    carlos3.start()
    loop.create_task(handlers.register(carlos3, attack=False, quest=False, favQuest=[0,1,2], arenaTime='05:19'))
except: print(24)
try: 
    carlos5.start()
    loop.create_task(handlers.register(carlos5,attack=False, quest=False, favQuest=[0,1,2], arenaTime='13:19'))
except: print(26)
try: #yisus alts
    y_babi.start()
    loop.create_task(handlers.register(y_babi, quest=True,attack=True, favQuest=[0,1,2], arenaTime='05:40', alliance = True))
except: print(27)
try: 
    y_clau.start()
    loop.create_task(handlers.register(y_clau, quest=True, attack=True, favQuest=[0,1,2], arenaTime='05:41', alliance = True))
except: print(28)
try: 
    y_charly.start()
    loop.create_task(handlers.register(y_charly, quest=True, attack=True, favQuest=[0,1,2], arenaTime='05:42', alliance = True))
except: print(29)
try: #yisus
    yisus.start()
    loop.create_task(handlers.register(yisus, quest=False, hunt=True, arenaTime='06:00', favQuest=[0,1,2], traderId='08', rngrAtk=True, alliance = True, forwardMobsTo=1420240083))
except: print(30)
try: #soy_clau
    y_soyKlau.start()
    loop.create_task(handlers.register(y_soyKlau, quest=False, hunt=True, arenaTime='06:10', favQuest=[0,1,2], rngrAtk=True, alliance = True, forwardMobsTo=1420240083))
except: print(31)
try: #shay alts
    shay1.start()
    loop.create_task(handlers.register(shay1, quest=True, favQuest=[0,1,2], arenaTime='07:19'))
except: print(32)
try: 
    shay2.start()
    loop.create_task(handlers.register(shay2, quest=True, favQuest=[0,1,2], arenaTime='06:19'))
except: print(33)
try: 
    shay3.start()
    loop.create_task(handlers.register(shay3, quest=True, favQuest=[0,1,2], arenaTime='05:19'))
except: print(34)
try: 
    shay4.start()
    loop.create_task(handlers.register(shay4, quest=True, favQuest=[0,1,2], arenaTime='04:19'))
except: print(35)
try: #lachy
    lachy.start()
    loop.create_task(handlers.register(lachy, quest=True, attack=True, favQuest=[0,1,2], arenaTime='11:13', alliance = True))
except: print(36)
try: #andrea
    andrea.start()
    loop.create_task(handlers.register(andrea, quest=True, attack=False, favQuest=[0,1,2], traderId='02', arenaTime='11:35'))
except: print(38)




loop.create_task(handlers.scheduleArenas())
loop.create_task(me(all_list))

a()

yo.run_until_disconnected()

print(time.asctime(), '-', 'Stopped!')
