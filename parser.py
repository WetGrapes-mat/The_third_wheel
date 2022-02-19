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
    temp_tank = []

    with open('player_list.json', 'r') as file_player:
        # json.dump(data, file, indent=3)
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
                tank=temp_tank
            ))
            temp_tank = []
        return all_player, all_tanks,


def save_info(list_all_players):
    with open('player_list.json', 'r') as file:
        counter = 0
        player_list = json.load(file)
        temp = []
        for i_item in player_list['player']:
            i_item['won_battels'] = list_all_players[counter].get_won_battel()
            i_item['battels'] = list_all_players[counter].get_battel()
            i_item['credits'] = list_all_players[counter].get_credits()
            for i in list_all_players[counter].get_tanks():
                temp.append(i.get_id())
            i_item['tanks'] = temp
            temp = []
            counter += 1
        with open('player_list.json', 'w') as w:
            json.dump(player_list, w, indent=2)

