import json
from server_wot import*


def parser():
    all_tanks = []
    all_player = []
    with open('tank_list.json', 'r') as file_tank:
        tank_list = json.load(file_tank)
        for tank in tank_list['tanks']:
            all_tanks.append(Tank(
                name=tank['tank_name'],
                id=tank['tank_id'],
                price=tank['tank_price'],
                hp=tank['tank_hp'],
                force=tank['tank_force']
            ))

    with open('player_list.json', 'r') as file_player:
        temp_tank = []
        player_list = json.load(file_player)
        for player in player_list['player']:
            for id_tank in all_tanks:
                if id_tank.get_id() in player['tanks']:
                    temp_tank.append(id_tank)
            all_player.append(Player(
                nickname=player['nickname'],
                won_battels=player['won_battels'],
                battels=player['battels'],
                credits=player['credits'],
                tank=temp_tank.copy()
            ))
            temp_tank.clear()
        return all_player, all_tanks


def encoder(all_player_list):
    class MyEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Player):
                temp = []
                for i in o.get_tanks():
                    temp.append(i.get_id())
                return {
                    "nickname": o.get_nickmane(),
                    "won_battels": o.get_won_battel(),
                    "battels": o.get_battel(),
                    "credit": o.get_credits(),
                    "tanks": temp
                }
            return o

    with open('player_list.json', 'r') as file:
        player_list = json.load(file)
        for i_item in player_list['player']:
            json.dumps(i_item, cls=MyEncoder)
        with open('player_list.json', 'w') as w:
            json.dump(player_list, w, indent=2)
