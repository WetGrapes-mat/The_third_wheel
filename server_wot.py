import random
import json


class Player:
    def __init__(self, nickname, won_battles, battles, credits, tank):
        self.__nickname = nickname
        self.__won_battles = won_battles
        self.__battles = battles
        self.__credits = credits
        self.__tanks = tank

    def get_nickname(self):
        return self.__nickname

    def get_won_battle(self):
        return self.__won_battles

    def get_battle(self):
        return self.__battles

    def get_credits(self):
        return self.__credits

    def get_tanks(self):
        return self.__tanks


class Tank:
    def __init__(self, name, id, price, hp, force):
        self.__name = name
        self.__id = id
        self.__price = price
        self.__heal_points = hp
        self.__force = force

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_price(self):
        return self.__price

    def get_heal_points(self):
        return self.__heal_points

    def get_force(self):
        return self.__force


class Bot:
    __nickname = ''
    __tank = None
    __win_rate = 0    # float

    def get_win_rate(self):
        return self.__win_rate

    def get_nickname(self):
        return self.__nickname

    def get_tank(self):
        return self.__tank

    def generate_nickname(self):
        with open('nickname.txt', 'r') as file_nickname:
            self.__nickname = random.choice(file_nickname.readlines())

    def generate_tank(self, server):
        self.__tank = random.choice(server.get_tank_list())


class Server:
    __player_list = []
    __tank_list = []

    def get_tanks_from_file(self):
        with open('tank_list.json', 'r') as file_tank:
            tank_list = json.load(file_tank)
            for tank in tank_list['tanks']:
                self.__tank_list.append(Tank(
                    name=tank['tank_name'],
                    id=tank['tank_id'],
                    price=tank['tank_price'],
                    hp=tank['tank_hp'],
                    force=tank['tank_force']
                ))

    def get_players_from_file(self):
        with open('player_list.json', 'r') as file_player:
            temp_tank = []
            player_list = json.load(file_player)
            for player in player_list['player']:
                for id_tank in self.__tank_list:
                    if id_tank.get_id() in player['tanks']:
                        temp_tank.append(id_tank)
                self.__player_list.append(Player(
                    nickname=player['nickname'],
                    won_battles=player['won_battles'],
                    battles=player['battles'],
                    credits=player['credits'],
                    tank=temp_tank.copy()
                ))
                temp_tank.clear()

    @staticmethod
    def set_players_in_file(list_all_players):
        with open('player_list.json', 'r') as file:
            counter = 0
            player_list = json.load(file)
            temp = []
            for i_item in player_list['player']:
                i_item['nickname'] = list_all_players[counter].get_nickname()
                i_item['won_battles'] = list_all_players[counter].get_won_battle()
                i_item['battles'] = list_all_players[counter].get_battle()
                i_item['credits'] = list_all_players[counter].get_credits()
                for i in list_all_players[counter].get_tanks():
                    temp.append(i.get_id())
                i_item['tanks'] = temp
                temp = []
                counter += 1
            with open('player_list.json', 'w') as w:
                json.dump(player_list, w, indent=2)

    def get_player_list(self):
        return self.__player_list

    def get_tank_list(self):
        return self.__tank_list


class Battle:
    __team_one = []
    __team_two = []
    __team_one_frags = []
    __team_two_frags = []
    __team_one_damage = []
    __team_two_damage = []
    __map_name = ''
