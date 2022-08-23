import sys

board = ['0','1','2','3','4','5','6','7','8','9']
p1 = 'player1'
player1 = 'wrong'
player2 = 'wrong'

def check_fullboard(board):
        ''' This function is used to check wheather board is full or not'''
        
        cnt = 0
        for i in range(1,10):
                if board[i] == 'X' or board[i] == 'O':
                        cnt +=1
                       
        if cnt == 9:
                return True
        else:
                return False
                        
def check_position(board,pos):
        ''' This function check if selected position index is already selected or not
                if it is already selected then it returns True else return False'''
        
        if board[pos] == 'X' or board[pos] == 'O':
                return True
        else:
                return False

def check_win(board):
        
        if board[1]==board[2] and board[2] == board[3] and board[1] != '1':
                return True
        elif board[4]==board[5] and board[5] == board[6] and board[4] != '4':
                return True
        elif board[7]==board[8] and board[8] == board[9] and board[8] != '8':
                return True
        elif board[4]==board[1] and board[1] == board[7] and board[4] != '4':
                return True
        elif board[5]==board[2] and board[2] == board[8] and board[5] != '5':
                return True
        elif board[3]==board[6] and board[6] == board[9] and board[9] != '9':
                return True
        elif board[1]==board[5] and board[1] == board[9] and board[1] != '1':
                return True
        elif board[5]==board[7] and board[7] == board[3] and board[5] != '5':
                return True

def display_board(board,flag):
        print('\n'*27)
        print(board[7],'|',board[8],'|',board[9])
        print ('--|---|---')
        print(board[4],'|',board[5],'|',board[6])
        print ('--|---|---')
        print(board[1],'|',board[2],'|',board[3])
        if flag:
                position_choice()

def player_choice():
    choice = 'wrong'
    print('welcome to Tic Tac Toe game')
    while choice not in (['x','o']):
        choice = input('Enter your choice (X / O)')
        if choice.isalpha():
            choice = choice.lower()
            if choice in (['x','o']):
                if choice == 'x':
                    global player1
                    global player2
                    player1 = 'X'
                    player2 = 'O'
                else:
                    player1 = 'O'
                    player2 = 'X'
            else:
                print('Enter valid choice!')
        else:
            print('Enter valid choice!')
            
    display_board(board,True)


            
    
def position_choice():
    pos = 0
    pos_range = range(1,10)
    if check_fullboard(board):
            print("Game Tie")
    else:
            while pos not in pos_range:
                pos = input(f'Enter {p1} position index (1 - 9): ')
                if pos.isdigit():
                        pos = int(pos)
                        if check_position(board,pos):
                                print("Already Selected, Please select other index")
                                pos = 0
                        else:
                                if pos not in pos_range:
                                        print("Enter Valid Index!")
                                
                else:
                    '''print('Enter valid index!')'''
                    exit()
                
            reposition_block(pos,board)
            


def reposition_block(pos,board):
    global p1
    if p1 in 'player1':
        board[pos] = player1
        if check_win(board):
                display_board(board,False)
                
                sys.exit(f'{p1} win')
        p1 = 'player2'
        display_board(board,True)
    else:
        board[pos] = player2
        if check_win(board):
                display_board(board,False)
                sys.exit(f'{p1} win')
        p1 = 'player1'
        display_board(board,True)


player_choice()



