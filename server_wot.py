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

    def get_winrate(self):
        return self.__win_rate

    def get_nickname(self):
        return self.__nickname

    def get_tank(self):
        return self.__tank


class Server:
    __player_list = []
    __tank_list = []

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
