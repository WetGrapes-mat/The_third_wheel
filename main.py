from server_wot import*
s = Server()

b1 = BattlePlayer(Bot(s))
b2 = BattlePlayer(Bot(s))
b3 = BattlePlayer(Bot(s))
b4 = BattlePlayer(Bot(s))


t1 = [b1, b2]
t2 = [b3, b4]
battle = Battle(t1, t2, 'qwerty')
a, b = battle.simulate_battle()