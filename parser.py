import json
from server_wot import*
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
temp_tank = []
with open('player_list.json', 'r') as file_player:
    # json.dump(data, file, indent=3)
    player_list = json.load(file_player)
    for player in player_list['player']:
        for id_tank in all_tanks:
            if id_tank.get_id() in player['tanks']:
                print(id_tank.get_id())
                temp_tank.append(id_tank)
        all_player.append(Player(
            nickname=player['nickname'],
            won_battels=player['won_battels'],
            battels=player['battels'],
            credits=player['credits'],
            tank=temp_tank
        ))
        temp_tank = []
# print(json.dumps(player_list, indent=2))
