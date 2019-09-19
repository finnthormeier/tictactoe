def play_tictactoe(p1=' ',p2=' ',p3=' ',p4=' ',p5=' ',p6=' ',p7=' ',p8=' ',p9=' '):
    
    def print_board(p1=' ',p2=' ',p3=' ',p4=' ',p5=' ',p6=' ',p7=' ',p8=' ',p9=' '):
    
        print(
            f'   |   |   \n {p7} | {p8} | {p9} \n   |   |   \n-----------\n\
   |   |   \n {p4} | {p5} | {p6} \n   |   |   \n-----------\n\
   |   |   \n {p1} | {p2} | {p3} \n   |   |   ')
    
    def check_win(p1,p2,p3,p4,p5,p6,p7,p8,p9):
        if p1 == players['Player 1'] and p2 == players['Player 1'] and p3 == players['Player 1'] \
        or p4 == players['Player 1'] and p5 == players['Player 1'] and p6 == players['Player 1'] \
        or p7 == players['Player 1'] and p8 == players['Player 1'] and p9 == players['Player 1'] \
        or p1 == players['Player 1'] and p4 == players['Player 1'] and p7 == players['Player 1'] \
        or p2 == players['Player 1'] and p5 == players['Player 1'] and p8 == players['Player 1'] \
        or p3 == players['Player 1'] and p6 == players['Player 1'] and p9 == players['Player 1'] \
        or p1 == players['Player 1'] and p5 == players['Player 1'] and p9 == players['Player 1'] \
        or p7 == players['Player 1'] and p5 == players['Player 1'] and p3 == players['Player 1']:
            print('Player 1 wins!!! Lets play again.')
            play_tictactoe()
        elif p1 == players['Player 2'] and p2 == players['Player 2'] and p3 == players['Player 2'] \
        or p4 == players['Player 2'] and p5 == players['Player 2'] and p6 == players['Player 2'] \
        or p7 == players['Player 2'] and p8 == players['Player 2'] and p9 == players['Player 2'] \
        or p1 == players['Player 2'] and p4 == players['Player 2'] and p7 == players['Player 2'] \
        or p2 == players['Player 2'] and p5 == players['Player 2'] and p8 == players['Player 2'] \
        or p3 == players['Player 2'] and p6 == players['Player 2'] and p9 == players['Player 2'] \
        or p1 == players['Player 2'] and p5 == players['Player 2'] and p9 == players['Player 2'] \
        or p7 == players['Player 2'] and p5 == players['Player 2'] and p3 == players['Player 2']:
            print('Player 2 wins!!! Lets play again.')
            play_tictactoe()
        else:
            pass

    def choose_player():
    
        XorO = input('Player 1, do you want to be "X" or "O"? ')
    
        if XorO == 'X' or XorO == 'x':
            player1 = 'X'
            player2 = 'O'
            print('\nPlayer 1 is ' + player1)
            print('Player 2 is ' + player2)
            return {'Player 1':player1,'Player 2':player2}
        elif XorO == 'O' or XorO == 'o':
            player1 = 'O'
            player2 = 'X'
            print('\nPlayer 1 is ' + player1)
            print('Player 2 is ' + player2)
            return {'Player 1':player1,'Player 2':player2}
        else:
            print('Wrong Input. Try again.')
            play_tictactoe()
            
    print('Lets play a game of Tic Tac Toe!!!')
        
    players = choose_player()
    
    print_board(1,2,3,4,5,6,7,8,9)
    
    move_counter = 1
    
    while move_counter <= 9:
        
        if move_counter%2 == 1:
    
            x = int(input('Player 1: Where do you want to place your stone? (1-9): '))

            if x == 1:
                if p1 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p1 = players['Player 1']
            elif x == 2:
                if p2 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p2 = players['Player 1']
            elif x == 3:
                if p3 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p3 = players['Player 1']
            elif x == 4:
                if p4 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p4 = players['Player 1']
            elif x == 5:
                if p5 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p5 = players['Player 1']
            elif x == 6:
                if p6 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p6 = players['Player 1']
            elif x == 7:
                if p7 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p7 = players['Player 1']
            elif x == 8:
                if p8 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p8 = players['Player 1']
            elif x == 9:
                if p9 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p9 = players['Player 1']
            else:
                print('Wrong input. Number needs to be between 1-9. Try again.')
                move_counter -= 1
                
        elif move_counter%2 == 0:
            
            x = int(input('Player 2: Where do you want to place your stone? (1-9): '))

            if x == 1:
                if p1 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p1 = players['Player 2']
            elif x == 2:
                if p2 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p2 = players['Player 2']
            elif x == 3:
                if p3 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p3 = players['Player 2']
            elif x == 4:
                if p4 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p4 = players['Player 2']
            elif x == 5:
                if p5 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p5 = players['Player 2']
            elif x == 6:
                if p6 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p6 = players['Player 2']
            elif x == 7:
                if p7 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p7 = players['Player 2']
            elif x == 8:
                if p8 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p8 = players['Player 2']
            elif x == 9:
                if p9 != ' ':
                    print('Cant place stone here. Try again.')
                    move_counter -= 1
                else:
                    p9 = players['Player 2']
            else:
                print('Wrong input. Number needs to be between 1-9. Try again.')
                move_counter -= 1

        positions = (p1,p2,p3,p4,p5,p6,p7,p8,p9)

        print_board(positions[0],positions[1],positions[2],positions[3],positions[4],positions[5],positions[6],positions[7],positions[8])
        
        check_win(positions[0],positions[1],positions[2],positions[3],positions[4],positions[5],positions[6],positions[7],positions[8])

        move_counter += 1
    
    print('This was a draw. Play again!!!')
    
    play_tictactoe()

play_tictactoe()