class statsPlayer:
    def __init__(self,client, atk=None, doQuest=None, hunt=None, hp = 0, stam= 0, lvl= 0, maxHp= 0, arenaTime= None, favQuest = None, forwardMobsTo = None, traderId=None, rangerAtkTime=None, alliance = False):
        self.client = client
        self.atk = atk
        self.doQuest = doQuest
        self.hunt = hunt
        self.hp = hp
        self.stam = stam
        self.lvl = lvl
        self.maxHp = maxHp
        self.arenaTime = arenaTime
        self.favQuest = favQuest
        self.forwardMobsTo = forwardMobsTo
        self.traderId = traderId
        self.arenaDeamon = None
        self.rangerAtkTime = rangerAtkTime
        self.alliance = alliance

    def __str__(self) -> str:
        return 'Ataca:%s\nQuest=%s\nCaza=%s\nArenaTime=%s\nFav Quest=%s\nFoward mobs to=%s\nTrader id:%s\nHp=%s/%s\nStam:%s\nLevel:%s\nRangerAtkTime=%s\nArenaJob=%s' %( self.atk,  self.doQuest, self.hunt, self.arenaTime, self.favQuest,  self.forwardMobsTo, self.traderId, self.hp, self.maxHp, self.stam, self.lvl, self.rangerAtkTime, self.arenaDeamon)

