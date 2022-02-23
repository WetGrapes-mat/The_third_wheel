from server_wot import*


def menu():
    print('-' * 20)
    print('1 - choose an account')
    print('2 - start battle')
    print('3 - buy tank')
    print('4 - change nickname')
    print('0 - exit')
    print('-' * 20, '\n')


s = Server()


def choose_account(s: Server) -> Player:
    print('Choose an account: ')
    for i in range(len(s.get_player_list())):
        print('Number', i)
        print(s.get_player_list()[i].get_nickname())
        print(f'Won Battles: {s.get_player_list()[i].get_won_battles()}')
        print(f'Battles: {s.get_player_list()[i].get_battle()}')
        print(f'Credits: {s.get_player_list()[i].get_credits()}')
        print('Tanks')
        for tank in s.get_player_list()[i].get_tanks():
            print(tank.get_name())
        print('*'*20)
    choice: int = int(input())
    try:
        player = s.get_player_list()[choice]
    except IndexError:
        print('WRONG INPUT!')
        player = choose_account(s)
    return player


player = choose_account(s)
menu()
while True:
    choice = int(input())
    try:
        if choice == 1:
            player = choose_account(s)
            menu()
        elif choice == 2:
            player.lets_battle(s)
            menu()
        elif choice == 3:
            player.buy_tank(s)
            menu()
        elif choice == 4:
            player.change_nickname(s)
            menu()
        elif choice == 0:
            break
    except ValueError:
        print('WRONG INPUT!')
        menu()
