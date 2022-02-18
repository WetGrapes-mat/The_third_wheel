class Player:
    __nickname = ''
    __tanks = []
    __win_rate = 0    # float
    __battles = 0
    __won_battles = 0
    __credits = 0
    __exp = 0
    # __tanks_exp = 0
    __investigated_tanks = []

    def get_credits(self):
        return self.__credits

    def get_exp_for_tank_invest(self):
        return self.__exp


class Tank:
    __name = ''
    __id = 0
    __price = 0
    __investigation_price = 0
    __level = 0
    __heal_points = 0
    __force = 0    # int?
    __tanks_exp = []

    def get_heal_points(self):
        return self.__heal_points

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_lvl(self):
        return self.__level

    def get_force(self):
        return self.__force

    def get_price(self):
        return self.__price

    def get_investigation_price(self):
        return self.__investigation_price

    def get_investigation_list(self):
        return self.__tanks_exp


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
