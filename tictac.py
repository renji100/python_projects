import random


tic_list =['N','N','N','N','N','N','N','N','N'] #tic tac board

winning_comb =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #possible winning combinations

open_positions = [0,1,2,3,4,5,6,7,8] #initial open positions in the board

def display_tic():
    '''
        this function displays the current status of the tic tac board

    '''
    print('displaying current position')
    k= tic_list
    
    print(k[0]," ",k[1]," ",k[2])
    print(k[3]," ",k[4]," ",k[5])
    print(k[6]," ",k[7]," ",k[8])
       

def update_tic_tac_list():
    '''
        remove the positions from open position list that are already selected by Computer or Player1
    '''
    
    for i,v in enumerate(tic_list,0):
       
        if v =='N':
            pass #print(k,v,end =" ")
        else :
            if i in open_positions:
                open_positions.remove(i)
            pass
    

def display_empty_positions():
    '''
        display the open positions,i starts from 0, incrementing with 1 for readability
    '''
    print('open positions : ',[i +1 for i in open_positions])
    

def player1_play():
    '''
        player1 picks his position
    '''
    inp_num = input('pick one position: ')
    tic_list[int(inp_num)-1]='x'

def computer_play():
    #print('computer playing')
    intelligence = 0 #if player1 is going to win, computer has to make a counter move
    computer_pick = 0
    for k in winning_comb:#go through the winning combination
        
        if tic_list[k[0] ]== '0'  and tic_list[k[1]] =='0' and tic_list[k[2]]=='N':
            computer_pick=k[2]+1
            tic_list[k[2]]='0'
            intelligence =1
            break
        elif tic_list[k[0] ]== '0'  and tic_list[k[1]] =='N' and tic_list[k[2]]=='0':
            computer_pick=k[1]+1
            tic_list[k[1]]='0'
            intelligence =1
            break
        
        elif tic_list[k[0] ]== 'N'  and tic_list[k[1]] =='0' and tic_list[k[2]]=='0':
            computer_pick=k[0]+1
            tic_list[k[0]]='0'
            intelligence =1
            break

        elif tic_list[k[0] ]== 'x'  and tic_list[k[1]] =='x' and tic_list[k[2]]=='N':
            computer_pick=k[2]+1
            tic_list[k[2]]='0'
            intelligence =1
            break
        elif  tic_list[k[0] ]== 'x'  and tic_list[k[1]] =='N' and tic_list[k[2]]=='x':
            computer_pick=k[1]+1
            tic_list[k[1]]='0'
            intelligence =1
            break
        elif  tic_list[k[0] ]== 'N'  and tic_list[k[1]] =='x' and tic_list[k[2]]=='x':
            computer_pick=k[0]+1
            tic_list[k[0]]='0'
            intelligence =1
            break
    
    if intelligence == 0:#if there is no threat to computer, computer will randomly pick his position
        computer_pick = random.choice([i +1 for i in open_positions])
        print('computer picked : ',computer_pick)
        tic_list[computer_pick-1]='0'


def check_win():

    '''
       check if there is any winner using the winning combination list 
    '''
    for k in winning_comb:
        
        if tic_list[k[0] ]== 'x'  and tic_list[k[1]] =='x' and tic_list[k[2]]=='x':
            
            return True
        elif tic_list[k[0]] == '0'  and tic_list[k[1]] =='0' and tic_list[k[2]]=='0':
            
            return True
        else:
            pass
    
    return False


def play_game():
    '''
    Game controller: player1 plays first and then computer plays. After each step, 
    tic tac board is updated and checked if there is any winner
    '''
   
    winner = ''          
    player1 = input('enter player1 name : ')
    while(len(open_positions)>0): #play as long as open tic tac positions are available
        
        
        display_tic() # display the tic tac board
        display_empty_positions() #display the available position
        player1_play() #player1 picks his position
        update_tic_tac_list() #update the tictac list
        if check_win(): # check if the player1 is a winner
            winner = player1
            break 
        if len(open_positions)==0: #if no more open positions end the game
            break
        computer_play() # computer makes the move

        update_tic_tac_list() #update tictac board
        if check_win(): #check if computer is winner
            winner = 'computer'
            break
       
    
    display_tic() # display the final board
    if winner == '':
        print( ' No one won')
    else :
        print('Winner is {}'.format(winner))

play_game() # call the game controller