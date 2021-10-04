from math import trunc
from re import A
from data import api_id, api_hash, bot_string_session, my_string_session, alt_string_session, cathy_string_session, samuel_string_session, massi_string_session, konesa_string_session, isma_string_session, bilbo_string_session, jaca_string_session, japs_string_session, noris_string_session,electro_string_session, carola_string_session, nadie_gf_string_session, shay_string_session, nadie_string_session, manu_string_sessio, muffin_string_session, manualt_string_session, kisame_string_session, carlos_all_ss, carlos_all_marta_ss, carlos_lugo_ss, yisus_string_session, yisus_clau_ss, yisus_babi_ss, yisus_charly_ss, yisus_soyclau_ss, shay1_string_session, shay2_string_session, shay3_string_session, shay4_string_session, carlos_all_angela_ss, carlos_all_m_ss, lachy_all_ss, noris2_string_session, alt_andrea_string_session
import asyncio, time, logging,handlers, schedule
from telethon import TelegramClient
from telethon.sessions import StringSession

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
nadieGF =  TelegramClient(StringSession(nadie_gf_string_session), api_id, api_hash)
jaca =  TelegramClient(StringSession(jaca_string_session), api_id, api_hash)
kisame =  TelegramClient(StringSession(kisame_string_session), api_id, api_hash)
carlos1 =  TelegramClient(StringSession(carlos_all_ss), api_id, api_hash)
carlos2 =  TelegramClient(StringSession(carlos_all_marta_ss), api_id, api_hash)
carlos3 =  TelegramClient(StringSession(carlos_lugo_ss), api_id, api_hash)
# carlos4 =  TelegramClient(StringSession(carlos_all_m_ss), api_id, api_hash)
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


all_list = [yo, alt, andrea, cathy,sam , mass, isma, bilbo, japz, noris, noris2, electro, caro, shay, manu, muffin, manualt, nadieGF, carlos1,carlos2, carlos3, carlos5, y_soyKlau, y_charly, y_babi, y_clau, yisus, shay1, shay2,shay3,shay4, lachy]

for client in all_list:
    client.add_event_handler(handlers.handle_updateMe)

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


#yo
yo.add_event_handler(handlers.handle_withdrawing)
yo.add_event_handler(handlers.handle_withdraw)
yo.add_event_handler(handlers.handle_Full_Stamina)
yo.add_event_handler(handlers.handle_stam_deplete)
yo.add_event_handler(handlers.Handle_Do_quest)
yo.add_event_handler(handlers.handle_Stop_Foray)
yo.add_event_handler(handlers.handle_Mods)
yo.add_event_handler(handlers.handle_bichos_hunt)
yo.add_event_handler(handlers.handle_if_alive)
yo.add_event_handler(handlers.handle_if_death)
yo.add_event_handler(handlers.handle_pldege_accept)
yo.add_event_handler(handlers.handle_click_pve)


#alt
alt.add_event_handler(handlers.handle_Full_Stamina)
alt.add_event_handler(handlers.handle_stam_deplete)
alt.add_event_handler(handlers.Handle_Do_quest)
alt.add_event_handler(handlers.handle_Stop_Foray)
alt.add_event_handler(handlers.handle_Mods)

#kathy
cathy.add_event_handler(handlers.handle_Full_Stamina)
cathy.add_event_handler(handlers.handle_stam_deplete)
cathy.add_event_handler(handlers.Handle_Do_quest)
cathy.add_event_handler(handlers.handle_Stop_Foray)
cathy.add_event_handler(handlers.handle_if_alive)
cathy.add_event_handler(handlers.handle_if_death)
cathy.add_event_handler(handlers.handle_bichos_hunt)
cathy.add_event_handler(handlers.handle_Mods)

#sam
sam.add_event_handler(handlers.handle_pldege_accept)
sam.add_event_handler(handlers.handle_Stop_Foray)

#mass
mass.add_event_handler(handlers.handle_Full_Stamina)
mass.add_event_handler(handlers.handle_stam_deplete)
mass.add_event_handler(handlers.Handle_Do_quest)
mass.add_event_handler(handlers.handle_Stop_Foray)
mass.add_event_handler(handlers.handle_Mods)


#isma
isma.add_event_handler(handlers.handle_Full_Stamina)
isma.add_event_handler(handlers.handle_stam_deplete)
isma.add_event_handler(handlers.Handle_Do_quest)
isma.add_event_handler(handlers.handle_Stop_Foray)
isma.add_event_handler(handlers.handle_Mods)
isma.add_event_handler(handlers.handle_bichos_hunt)
isma.add_event_handler(handlers.handle_if_alive)
isma.add_event_handler(handlers.handle_if_death)
isma.add_event_handler(handlers.handle_trader)


#bilbo
bilbo.add_event_handler(handlers.handle_Full_Stamina)
bilbo.add_event_handler(handlers.handle_stam_deplete)
bilbo.add_event_handler(handlers.Handle_Do_quest)
bilbo.add_event_handler(handlers.handle_Stop_Foray)
bilbo.add_event_handler(handlers.handle_Mods)

#japs
japz.add_event_handler(handlers.handle_Full_Stamina)
japz.add_event_handler(handlers.handle_stam_deplete)
japz.add_event_handler(handlers.Handle_Do_quest)
japz.add_event_handler(handlers.handle_Stop_Foray)
japz.add_event_handler(handlers.handle_Mods)

#noris
noris.add_event_handler(handlers.handle_pldege_accept)
noris.add_event_handler(handlers.handle_Stop_Foray)
noris.add_event_handler(handlers.handle_bichos_hunt)
noris.add_event_handler(handlers.handle_if_death)
noris.add_event_handler(handlers.handle_if_alive)

#norris
noris2.add_event_handler(handlers.handle_Full_Stamina)
noris2.add_event_handler(handlers.handle_stam_deplete)
noris2.add_event_handler(handlers.Handle_Do_quest)
noris2.add_event_handler(handlers.handle_Stop_Foray)
noris2.add_event_handler(handlers.handle_Mods)
 
#electro
electro.add_event_handler(handlers.handle_Stop_Foray)
electro.add_event_handler(handlers.handle_Mods)
electro.add_event_handler(handlers.handle_bichos_hunt)
electro.add_event_handler(handlers.handle_if_alive)
electro.add_event_handler(handlers.handle_if_death)
electro.add_event_handler(handlers.handle_pldege_accept)
electro.add_event_handler(handlers.handle_click_pve)

#carola
caro.add_event_handler(handlers.handle_Full_Stamina)
caro.add_event_handler(handlers.handle_stam_deplete)
caro.add_event_handler(handlers.Handle_Do_quest)
caro.add_event_handler(handlers.handle_Stop_Foray)
caro.add_event_handler(handlers.handle_Mods)


#shay
shay.add_event_handler(handlers.handle_Full_Stamina)
shay.add_event_handler(handlers.handle_stam_deplete)
shay.add_event_handler(handlers.Handle_Do_quest)
shay.add_event_handler(handlers.handle_Stop_Foray)
shay.add_event_handler(handlers.handle_pldege_accept)


#manu
manu.add_event_handler(handlers.handle_Stop_Foray)
manu.add_event_handler(handlers.handle_Mods)
manu.add_event_handler(handlers.handle_bichos_hunt)
manu.add_event_handler(handlers.handle_if_alive)
manu.add_event_handler(handlers.handle_if_death)
manu.add_event_handler(handlers.handle_pldege_accept)
manu.add_event_handler(handlers.handle_Full_Stamina)
manu.add_event_handler(handlers.handle_stam_deplete)
manu.add_event_handler(handlers.Handle_Do_quest)

#muffin
muffin.add_event_handler(handlers.handle_Full_Stamina)
muffin.add_event_handler(handlers.handle_stam_deplete)
muffin.add_event_handler(handlers.Handle_Do_quest)
muffin.add_event_handler(handlers.handle_Stop_Foray)
muffin.add_event_handler(handlers.handle_Mods)
muffin.add_event_handler(handlers.handle_bichos_hunt)
muffin.add_event_handler(handlers.handle_if_alive)
muffin.add_event_handler(handlers.handle_if_death)

#manualt
manualt.add_event_handler(handlers.handle_Full_Stamina)
manualt.add_event_handler(handlers.handle_stam_deplete)
manualt.add_event_handler(handlers.Handle_Do_quest)
manualt.add_event_handler(handlers.handle_Stop_Foray)

#nadieGf
nadieGF.add_event_handler(handlers.handle_Full_Stamina)
nadieGF.add_event_handler(handlers.handle_stam_deplete)
nadieGF.add_event_handler(handlers.Handle_Do_quest)
nadieGF.add_event_handler(handlers.handle_Stop_Foray)


#jaca
jaca.add_event_handler(handlers.handle_Stop_Foray)

#kisame
kisame.add_event_handler(handlers.handle_Full_Stamina)
kisame.add_event_handler(handlers.handle_stam_deplete)
kisame.add_event_handler(handlers.Handle_Do_quest)
kisame.add_event_handler(handlers.handle_Stop_Foray)
shay.add_event_handler(handlers.handle_order3)
shay.add_event_handler(handlers.handle_order2)

#carlos1
carlos1.add_event_handler(handlers.handle_Full_Stamina)
carlos1.add_event_handler(handlers.Handle_Do_quest)
carlos1.add_event_handler(handlers.handle_stam_deplete)
carlos1.add_event_handler(handlers.handle_Stop_Foray)

#carlos2
carlos2.add_event_handler(handlers.handle_Full_Stamina)
carlos2.add_event_handler(handlers.Handle_Do_quest)
carlos2.add_event_handler(handlers.handle_stam_deplete)
carlos2.add_event_handler(handlers.handle_Stop_Foray)

#carlos3
carlos3.add_event_handler(handlers.handle_Full_Stamina)
carlos3.add_event_handler(handlers.Handle_Do_quest)
carlos3.add_event_handler(handlers.handle_stam_deplete)
carlos3.add_event_handler(handlers.handle_Stop_Foray)

# #carlos4
# carlos4.add_event_handler(handlers.handle_Full_Stamina)
# carlos4.add_event_handler(handlers.Handle_Do_quest)
# carlos4.add_event_handler(handlers.handle_stam_deplete)
# carlos4.add_event_handler(handlers.handle_Stop_Foray)

#carlos5
carlos5.add_event_handler(handlers.handle_Full_Stamina)
carlos5.add_event_handler(handlers.Handle_Do_quest)
carlos5.add_event_handler(handlers.handle_stam_deplete)
carlos5.add_event_handler(handlers.handle_Stop_Foray)

#y_babi
y_babi.add_event_handler(handlers.handle_Full_Stamina)
y_babi.add_event_handler(handlers.Handle_Do_quest)
y_babi.add_event_handler(handlers.handle_stam_deplete)
y_babi.add_event_handler(handlers.handle_Stop_Foray)

#y_charly
y_charly.add_event_handler(handlers.handle_Full_Stamina)
y_charly.add_event_handler(handlers.Handle_Do_quest)
y_charly.add_event_handler(handlers.handle_stam_deplete)
y_charly.add_event_handler(handlers.handle_Stop_Foray)

#y_clau
y_clau.add_event_handler(handlers.handle_Full_Stamina)
y_clau.add_event_handler(handlers.Handle_Do_quest)
y_clau.add_event_handler(handlers.handle_stam_deplete)
y_clau.add_event_handler(handlers.handle_Stop_Foray)

#yisus
yisus.add_event_handler(handlers.handle_Full_Stamina)
yisus.add_event_handler(handlers.handle_stam_deplete)
yisus.add_event_handler(handlers.Handle_Do_quest)
yisus.add_event_handler(handlers.handle_Stop_Foray)
yisus.add_event_handler(handlers.handle_Mods)
yisus.add_event_handler(handlers.handle_bichos_hunt)
yisus.add_event_handler(handlers.handle_if_alive)
yisus.add_event_handler(handlers.handle_if_death)
yisus.add_event_handler(handlers.handle_trader)


#souklau
y_soyKlau.add_event_handler(handlers.handle_Full_Stamina)
y_soyKlau.add_event_handler(handlers.handle_stam_deplete)
y_soyKlau.add_event_handler(handlers.Handle_Do_quest)
y_soyKlau.add_event_handler(handlers.handle_Stop_Foray)
y_soyKlau.add_event_handler(handlers.handle_Mods)
y_soyKlau.add_event_handler(handlers.handle_bichos_hunt)
y_soyKlau.add_event_handler(handlers.handle_if_alive)
y_soyKlau.add_event_handler(handlers.handle_if_death)

#shay1
shay1.add_event_handler(handlers.handle_Full_Stamina)
shay1.add_event_handler(handlers.handle_stam_deplete)
shay1.add_event_handler(handlers.Handle_Do_quest)
shay1.add_event_handler(handlers.handle_Stop_Foray)

#shay2
shay2.add_event_handler(handlers.handle_Full_Stamina)
shay2.add_event_handler(handlers.handle_stam_deplete)
shay2.add_event_handler(handlers.Handle_Do_quest)
shay2.add_event_handler(handlers.handle_Stop_Foray)
#shay3
shay3.add_event_handler(handlers.handle_Full_Stamina)
shay3.add_event_handler(handlers.handle_stam_deplete)
shay3.add_event_handler(handlers.Handle_Do_quest)
shay3.add_event_handler(handlers.handle_Stop_Foray)
#shay4
shay4.add_event_handler(handlers.handle_Full_Stamina)
shay4.add_event_handler(handlers.handle_stam_deplete)
shay4.add_event_handler(handlers.Handle_Do_quest)
shay4.add_event_handler(handlers.handle_Stop_Foray)

#lachy
lachy.add_event_handler(handlers.handle_Full_Stamina)
lachy.add_event_handler(handlers.handle_stam_deplete)
lachy.add_event_handler(handlers.Handle_Do_quest)
lachy.add_event_handler(handlers.handle_Stop_Foray)
lachy.add_event_handler(handlers.handle_pldege_accept)

#andrea
andrea.add_event_handler(handlers.handle_Full_Stamina)
andrea.add_event_handler(handlers.handle_stam_deplete)
andrea.add_event_handler(handlers.Handle_Do_quest)
andrea.add_event_handler(handlers.handle_Stop_Foray)
andrea.add_event_handler(handlers.handle_trader)


print('Done')
controlBot.start()
try:
    yo.start()
    loop.create_task(handlers.register(yo, quest=False, hunt=True, favQuest=[1,2],arenaTime='15:30'  , rngrAtk=True, alliance = True))
except: print(2)
try:
    alt.start()
    loop.create_task(handlers.register(alt, attack=True, quest=True , favQuest=[0,1,2],arenaTime='15:00'  , forwardMobsTo=1420240083, alliance = True))
except: print(3)
try:
    cathy.start()
    loop.create_task(handlers.register(cathy, attack=True, quest=True, hunt=False , favQuest=[0,1,2], arenaTime='08:00'  , forwardMobsTo=1420240083, alliance = True))
except: print(4)
try:
    sam.start()
    loop.create_task(handlers.register(sam, attack=True, alliance = True))
except: print(5)
try: 
    mass.start()
    loop.create_task(handlers.register(mass, attack=True, quest=True, favQuest=[0], arenaTime='15:45'  , forwardMobsTo=1420240083, alliance = True))
except: print(6)
try:
    isma.start()
    loop.create_task(handlers.register(isma, attack=True ,quest=False, hunt=True, arenaTime='14:00', favQuest=[1,2], forwardMobsTo=745224074, traderId='08', alliance = True))
except: print(8)
try:
    bilbo.start()
    loop.create_task(handlers.register(bilbo, attack=True, quest=True, favQuest=[0,2],arenaTime='13:00'  , forwardMobsTo=1420240083, alliance = True))
    japz.start()
    loop.create_task(handlers.register(japz, attack=True, quest=True, favQuest=[0,2],arenaTime='13:00'  , forwardMobsTo=1420240083, alliance = True))
except: print(9)
try:
    noris.start()
    loop.create_task(handlers.register(noris, rngrAtk=True, hunt=True, alliance = True))
except: print(10)
try: 
    noris2.start()
    loop.create_task(handlers.register(noris2, attack=True, quest=True, favQuest=[0], arenaTime='06:00', forwardMobsTo=1420240083, alliance = True))
except: print(10.1)
try:
    electro.start()
    loop.create_task(handlers.register(electro, hunt=True, arenaTime='04:30', rngrAtk=True))
except: print(11)
try: 
    caro.start()
    loop.create_task(handlers.register(caro, attack=True ,quest=True, favQuest=[0], arenaTime='05:00'  , forwardMobsTo=1420240083, alliance = True))
except: print(12)
# try: 
#     nadie.start()
#     loop.create_task(handlers.register(nadie, quest=True, favQuest=[1]))
# except: print(13)
try: 
    shay.start()
    loop.create_task(handlers.register(shay, quest=True, favQuest=[0,1,2]  ))
except: print(14)
try:
    manu.start()
    loop.create_task(handlers.register(manu, hunt=True, quest=False, favQuest=[0,2],))
except: print(15)
try:
    muffin.start()
    loop.create_task(handlers.register(muffin, quest=False, hunt=True, arenaTime='05:00', favQuest=[1,2]  , forwardMobsTo=1420240083, rngrAtk=True, alliance = True))
except: print(16)
try: 
    manualt.start()
    loop.create_task(handlers.register(manualt, quest=True, favQuest=[0,1,2]))
except: print(17)
try: 
    nadieGF.start()
    loop.create_task(handlers.register(nadieGF, quest=True, favQuest=[0,1,2]))
except: print(18)
try: 
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
# try: 
#     carlos4.start()
#     loop.create_task(handlers.register(carlos4, quest=False, favQuest=[0], arenaTime='12:18'))
# except: print(25)
try: 
    carlos5.start()
    loop.create_task(handlers.register(carlos5,attack=False, quest=False, favQuest=[0,1,2], arenaTime='13:19'))
except: print(26)

try: 
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
try:
    yisus.start()
    loop.create_task(handlers.register(yisus, quest=False, hunt=True, arenaTime='06:00', favQuest=[0,1,2], traderId='08', rngrAtk=True, alliance = True))
except: print(30)
try:
    y_soyKlau.start()
    loop.create_task(handlers.register(y_soyKlau, quest=False, hunt=True, arenaTime='06:10', favQuest=[0,1,2], rngrAtk=True, alliance = True))
except: print(31)
try: 
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
try: 
    lachy.start()
    loop.create_task(handlers.register(lachy, quest=True, attack=True, favQuest=[0,1,2], arenaTime='11:13', alliance = True))
except: print(36)
try:
    andrea.start()
    loop.create_task(handlers.register(andrea, quest=True, attack=False, favQuest=[0,1,2], traderId='02', arenaTime='11:35'))
except:
    print(38)




loop.create_task(handlers.scheduleArenas())
loop.create_task(me(all_list))
a = lambda: loop.create_task(handlers.check_schedule())

a()

yo.run_until_disconnected()

print(time.asctime(), '-', 'Stopped!')