from server_wot import Server

s = Server()

player = s.get_player_list()[0]

player.lets_battle(s)


# player.change_nickname()
# player.buy_tank(s)


s.set_players_in_file(s.get_player_list())


