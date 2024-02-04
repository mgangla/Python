import random
import time
import sys


# functions
#got snake n got ladder tohelp get_position
#dice_roll
#snake_n_ladder
#play

maxval = 100
dice_face = 6
delay  = 1 #a delay of 1 sec between actions

#define the data dictionary to store the data for snake n ladder position

# snake takes you down from 'key' to 'value' keyis the head of snake
snake_position= {
    17: 7,
    62: 19,
    64: 60,
    54: 34,
    87: 36,
    95: 75,
    93: 73,
    98: 79,
    
}

# ladder takes you up from 'key' to 'value' key is the begining of the ladder
ladders_position = {

    1: 38,    
    4: 14,
    9: 31,  
    21: 42,
    28: 84,
    51: 67,
    72: 91,
    80: 99
    
}

#function for dice roll
def get_roll():
    time.sleep(delay)
    dice_roll = random.randint(1, dice_face)

    #if die rollis 6 the person has to takeanother turn and maz of 3 turns
    
    print("Its a " + str(dice_roll))

    return dice_roll

#function define for taking input (Name of player) from user
def get_player_names():
    p1_name = None
    while not p1_name:
        p1_name = input("Name of first player: ").strip()

    p2_name = None
    while not p2_name:
        p2_name = input("Name of second player: ").strip()

#p3_name = None
    #while not p3_name:
    #    p3_name = input("Name of third player: ").strip()

   # p4_name = None
   # while not p4_name:
     #   p4_name = input("Name of fourth player: ").strip()
      #  """""""""


    print("\n'" + p1_name+ "' and '" +p2_name + " You will play against each other'\n")
    print(p1_name, p2_name)
    return p1_name, p2_name 
    

#function define for snake 
def got_snake(old_value, current_value, player_name):
    print("\n" + " ~~~~~~~~>")
    print("\n"" " + player_name + " got a bite from snake. Going down from " + str(old_value) + " to " + str(current_value))



#function define for ladder
def got_ladder(old_value, current_value, player_name):
    print("\n" + " ########")
    print("\n" + player_name + " is climbing the ladder from " + str(old_value) + " to " + str(current_value))

#function define for snake and ladder
def snake_ladder(player_name, current_value, dice_value):
    time.sleep(delay)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > maxval:
        print("You need " + str(maxval - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snake_position:
        final_value = snake_position.get(current_value)
        got_snake(current_value, final_value, player_name)

    elif current_value in ladders_position:
        final_value = ladders_position.get(current_value)
        got_ladder(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

#function define for checking the winner
def check_win(player_name, position):
    time.sleep(delay)
    if maxval == position:
        print("\n" + player_name + "has  won the game.")
        print("Congratulations " + player_name +"You are the winner")
        sys.exit (1)


#function to play
        
def play ():
    time.sleep(delay)
    p1_name, p2_name = get_player_names()
    time.sleep(delay)

    p1_current_position = 0
    p2_current_position = 0

    while True:
        time.sleep(delay)
        input_1 = input("\n" + p1_name + " Press enter for rolling the dice: ")
        print("\n d\Dice is being rolled...")
        dice_value = get_roll()
        time.sleep(delay)
        print(p1_name + " moving....")
        p1_current_position = snake_ladder(p1_name, p1_current_position, dice_value)

        check_win(p1_name, p1_current_position)

        input_2 = input("\n" + p2_name + " Press enter for rolling the dice: ")
        print("\n Dice is being rolled...")
        dice_value = get_roll()
        time.sleep(delay)
        print(p2_name + " moving....")
        p2_current_position = snake_ladder(p2_name, p2_current_position, dice_value)

        check_win(p2_name, p2_current_position)


if __name__ == "__main__":
    play()




#call the functions
#get_player_names()
#get_roll()

