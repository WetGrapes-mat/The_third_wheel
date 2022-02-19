import random
import json


class Player:

    def __init__(self, nickname, won_battles, battles, credits, tank):
        self.__nickname = nickname
        self.__won_battles = won_battles
        self.__battles = battles
        self.__credits = credits
        self.__tanks = tank
        self.__win_rate = (self.__won_battles / self.__battles) * 100

    def get_nickname(self):
        return self.__nickname

    def get_won_battles(self):
        return self.__won_battles

    def get_battle(self):
        return self.__battles

    def get_credits(self):
        return self.__credits

    def get_tanks(self):
        return self.__tanks

    def lets_battle(self, server):
        print('Choose the tank:')
        tanks = self.__tanks
        for i in range(len(tanks)):
            print(f'{i} - {tanks[i].get_name()}')
        print(f'{len(tanks)} - exit')
        choice = int(input())
        if choice == len(tanks):
            return
        elif 0 <= choice < len(tanks):
            my_tank = tanks[choice]
            earned_credits, battle_won = server.start_battle(my_tank, self)
            self.__credits += earned_credits
            print(f'Earned {earned_credits} credits per battle')
            self.__won_battles += battle_won
            self.__battles += 1
            self.__win_rate = (self.__won_battles / self.__battles) * 100
        else:
            print('WRONG INPUT!')
            self.lets_battle(server)
        # save to Server!

    def buy_tank(self, server):
        tanks = server.get_tank_list()
        available_to_purchase = []
        for c in tanks:
            if c not in self.__tanks:
                available_to_purchase.append(c)
            else:
                continue
        print('Available to purchase tanks:')
        for i in range(len(tanks)):
            print(f'{i} - {available_to_purchase[i].get_name()} - {available_to_purchase[i].get_price()}')
        print(f'{len(tanks)} - exit')
        choice = int(input())
        if choice == len(tanks):
            return
        elif 0 <= choice < len(tanks):
            new_tank = tanks[choice]
            if self.__credits >= new_tank.get_price():
                self.__credits -= new_tank.get_price()
                self.__tanks.append(new_tank)
            else:
                print('Not enough credits :(')
                self.buy_tank(server)
        else:
            print('WRONG INPUT!')
            self.buy_tank(server)
        # save to Server!

    def change_nickname(self):
        new_nickname = input('Enter new nickname: ')
        print('Are you sure? Changing your nickname costs 50_000 credits')
        print('0 - YES\n1 - NO')
        choice = int(input())
        if choice == 0:
            self.__nickname = new_nickname
            self.__credits -= 50_000
        elif choice == 1:
            return
        else:
            print('WRONG INPUT!')
            self.change_nickname()


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

    def __init__(self, server):
        self.generate_nickname()
        self.generate_tank(server)
        self.generate_win_rate()

    def get_win_rate(self):
        return self.__win_rate

    def get_nickname(self):
        return self.__nickname

    def get_tank(self):
        return self.__tank

    def generate_win_rate(self):
        choice = random.randint(0, 100)
        if 0 <= choice < 10:
            i = random.randint(0, 1)
            if i == 0:
                self.__win_rate = random.randint(30, 40)
            elif i == 1:
                self.__win_rate = random.randint(60, 70)
        elif 10 <= choice < 30:
            i = random.randint(0, 1)
            if i == 0:
                self.__win_rate = random.randint(40, 43)
            elif i == 1:
                self.__win_rate = random.randint(57, 60)
        elif 30 <= choice < 55:
            i = random.randint(0, 1)
            if i == 0:
                self.__win_rate = random.randint(43, 47)
            elif i == 1:
                self.__win_rate = random.randint(53, 57)
        elif 55 <= choice <= 100:
            self.__win_rate = random.randint(47, 53)

    def generate_nickname(self):
        with open('nickname.txt', 'r') as file_nickname:
            self.__nickname = random.choice(file_nickname.readlines())

    def generate_tank(self, server):
        self.__tank = random.choice(server.get_tank_list())


class Server:
    __player_list = []
    __tank_list = []

    def __init__(self):
        self.get_players_from_file()
        self.get_tanks_from_file()

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

    def start_battle(self, tank, player):
        earned_credits, battle_won = 0, 0    # temporary value, need to be changed later
        return earned_credits, battle_won


class Battle:
    __team_one = []
    __team_two = []
    __team_one_frags = []
    __team_two_frags = []
    __team_one_damage = []
    __team_two_damage = []
    __map_name = ''
