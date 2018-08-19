#!/usr/bin/python

# Written by Pin-Chih Su 2017-08-17

# Tested in python 3.6.1.
#
# To reproduce the python environment,
#
# please copy the "environment.yml" into the path and run
#
# conda env create -f environment.yml
#
# Here is the instruction of how to install mini-conda (https://conda.io/docs/user-guide/install/linux.html)
#
# After the python environment is set up, please run
#
# python go_pin-chih.py
#
# to reproduce the results.
#
# Please contact Pin-Chih at "dr.pin.chih.su@gmail.com" if any question.  Thanks.

import re
import sys, getopt
print('Python version ' + sys.version)

print ('Welcome to the Go Game')




quit_variable = 1 # whether the game will be quit or not


## start over games. Make go_game a 2 dimension list. For example 4 X 4 like this

# [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]
# [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]

def beginning():

    go_game = []

    for x in range(0, sizeboard):

        go_game.append([])

        for y in range(0, sizeboard):

            go_game[x].append('-')

            # if sizeboard is 2, then the loop will construct a 2x2 dimension list
            # [['-']]
            # [['-', '-']]
            # [['-', '-'], ['-']]
            # [['-', '-'], ['-', '-']]

    return go_game # in 2 x2 example, this will generate [['-', '-'], ['-', '-']]


## GUI of the game board in ASCII
## Now we need to do some cosmetic changes to convert this 2X2 [['-', '-'], ['-', '-']] into
## - -
## - -

def printboard(go_game):

    global sizeboard

    for row in go_game:

        gameboard = ''

        for element in row:

            gameboard += element

            gameboard += ' ' # replace '-' with ' ', so that the game board looks pretty

        print(gameboard) # print the game board like the following (3X3 example)

        ## - - -
        ## - - -
        ## - - -


## the check state function reads the states of the go game board from the "go_game" list input like this

# in a 2 x2 example, the "go_game" list is [['o', '-'], ['-', '-']]

# it will be converted into a string "read_board"="o---"

def check_state(go_game):

    read_board = ''

    for row in go_game:

        for column in row:

            read_board += column

    return read_board


# check whether the move is legal or not by comparing the board game in a string in the nth step and the n-1 step.  If these 2 strings are not the same,

# then we check the "ko-rule" violoation or not.
#
    # If "ko-rule" violation : return 0.  If not, return 1.

# If the nth step and the n-1 step are the same, return 0 and show the error message.

def check_move():

    global go_1_dimension_string

    global go_2_dimension_list

    global go_gamep

    global go_game_general_list

    global go_game

    # check_state(go_game_general_list) is a string of the board in the n-1th step

    # go_1_dimension_string is a string of the board in the nth step

    if check_state(go_game_general_list) != go_1_dimension_string:

        go_gamep = []

        go_2_dimension_list = []

        ## this loop converts the 2D board game, such as
        ## - -
        ## - -

        # into a 2D list "go_game_general_list" [['o', '-'], ['-', '-']]

        for element in go_game_general_list:

            go_gamep.append(element)

            go_2_dimension_list.append(element)

        # convert "go_game_general_list" the 2D list into 1D string "go_1_dimension_string" such as "o---"

        go_1_dimension_string += check_state(go_game_general_list)

        ## check ko-rules:
        # In a 9X9 board, a ko rule in a string, which is converted from a 2D list is like this:

        # The original game board in a 2D list

        # - - - - - - - - -
        # - - - - - - - - -
        # - - - o x - - - -
        # - - o x o x - - -
        # - - - o x - - - -
        # - - - - - - - - -
        # - - - - - - - - -
        # - - - - - - - - -
        # - - - - - - - - -

        # converted into a string

        # xo------xoxo------xo

        # So we can do a regular expression check on the following

        # xo - -xxx - x - xo - -----xo  # no no => NOT ko rule violation
        # xo - -xxx - xoxo - -----xo  # yes => ko rule violation
        # xo - -xxx - xxxo - -----xo  # no => NOT ko rule violation
        # xo - -xxx - xxxo - xxx - -xo  # no => NOT ko rule violation
        # xo - -xxx - xoxo - xxx - -xo  # yes => ko rule violation

        # or the opposite

        # The original game board in a 2D list

        # - - - - - - - - -
        # - - - - - - - - -
        # - - - x o - - - -
        # - - x o x o - - -
        # - - - x o - - - -
        # - - - - - - - - -
        # - - - - - - - - -
        # - - - - - - - - -
        # - - - - - - - - -

        # converted into a string

        # ox------oxox------ox

        #ko_rule_check = "xo------xoxo------xo"


        ko_rule_search = re.search(r'xo......xoxo......xo', go_1_dimension_string)

        if str(ko_rule_search) == "None":

            print ("No ko rule violation.")

            return 1

        elif str(ko_rule_search) != "None":

            print ("Warning: there is a ko rule violation!! Try to move again!! ")

            return 0
    else:

        print('Invalid move! Players are not allowed to make a move that returns the game to the previous position. This rule, called the ko rule, prevents unending repetition.')

        return 0

## Take the user input coordinate x=1 & y=2 and save into a list such as [1, 2]

def user_input(white_chess):

    global temp

    global go_game_general_list

    temp = 1

    while temp == 1 and play_or_test == "p":

        user_input = input('Press y for Place, n for Quit  (y/n)? ')

        if user_input == 'n':

            print ('Quit')

            quit_variable == 0

            break

        elif user_input == 'y':

            error = 0

            try:

                x = int(input('x: '))

            except ValueError:

                error = 1

                print("The input value for x is not an integer!")

            try:

                y = int(input('y: '))

            except ValueError:

                error = 1

                print("The input value for y is not an integer!")

            if error == 1:

                print('Invalid input. The input value for coordinates is not an integer! Please Press y for Place again, n for Pass ')
        else:

            print('invalid')

    ## Ensures that the user_input is within the board boundary

        if (x > sizeboard) | (x < 0) | (y > sizeboard) | (y < 0):

            print('Invalid coordinate.  The coordinate has to be x >=0, y >=0')

        elif go_2_dimension_list[y][x] != '-':

            print('Invalid coordinate.  This coordinate has been occupied.')

        else:

            temp = 0

    if play_or_test == "p":  # play_or_test="p" actual play

        if white_chess == 'o':

            go_game_general_list[y][x] = 'o' # if it is the turn of "o", replace the board game's user input coordinate with "o"

        else:

            go_game_general_list[y][x] = 'x' # if it is the turn of "x", replace the board game's user input coordinate with "x"

    elif play_or_test == "u": # play_or_test="u"  => unit test

        if white_chess == 'o':

            y=int(0)
            x=int(0)

            go_game_general_list[y][x] = 'o'  # if it is the turn of "o", replace the board game's user input coordinate with "o"

        else:

            y=int(0)
            x=int(0)

            go_game_general_list[y][x] = 'x'

    return [x, y]



def turn():

    global white_chess

    global black_chess

    temp = 1

    while temp == 1:

        print("There are still " +str(sum([row.count('-') for row in go_2_dimension_list])) + ' empty positions left.') # go_2_dimension_list is a 2D list, [row.count('-') for row in go_2_dimension_list] will sum the 2nd dimension

        print("The o occupied "+str(sum([row.count('o') for row in go_2_dimension_list])) + ' positions')

        print("The x occupied "+str(sum([row.count('x') for row in go_2_dimension_list])) + ' positions')

        print()

        print('place for ' + white_chess)  # to show whose turn it is

        xy = user_input(white_chess) ## xy is a user input coordinate where the data type is list

        if check_move() == 1:

            temp = 0



## This is the main function to start the game, which call a bunch of functions above

def main():

    global sizeboard

    sizeboard = int(input(
        'Please select how big the N X N square game board you would like to have. Please enter N as an integer.  If no value is provided, the default value is 9 X 9 ') or "9")

    try:

        val = int(sizeboard)

    except ValueError:

        print("The input value " + sizeboard + " is not an integer!")

    sizeboard = int(sizeboard)  # the size of the board

    o_list = []

    x_list = []


    global go_2_dimension_list

    global go_game_general_list

    global go_1_dimension_string

    global white_chess

    global black_chess

    ## re-set the values to start the game

    go_2_dimension_list = beginning()

    go_game_general_list = beginning()

    go_1_dimension_string = ''

    white_points = 0  # set the points of white into 0

    black_points = 0  # set the points of black into 0

## In the "turn" functions, if both players call "N" not to proceed, "quit variable" will become 0 to end the gaem

    while quit_variable == 1:

        ## Set it as white chess player's turn

        white_chess = 'o'

        black_chess = 'x'

        print()

        printboard(go_2_dimension_list)

        turn()

        if quit_variable == 0: ## if user quit, then exit

            exit

        ## Sets it as black chess player turn

        white_chess = 'x'

        black_chess = 'o'

        print()

        printboard(go_2_dimension_list)

        turn()

    ## Counts the score of both players

    print()
    print('final board:')
    print()

    printboard(go_2_dimension_list)

    print()

    print("There are still " + str(sum([row.count('-') for row in go_2_dimension_list])) + ' empty positions left.')  # go_2_dimension_list is a 2D list, [row.count('-') for row in go_2_dimension_list] will sum the 2nd dimension

    print("The o occupied " + str(sum([row.count('o') for row in go_2_dimension_list])) + ' positions')

    print("The x occupied " + str(sum([row.count('x') for row in go_2_dimension_list])) + ' positions')

    white_points=sum([row.count('o') for row in go_2_dimension_list])

    black_points=sum([row.count('x') for row in go_2_dimension_list])

    ## Determines the winner

    if white_points > black_points:

        print('o wins')

    elif black_points > white_points:

        print('x wins')

    else:

        print('tie')

## call the main function to run the game.  The game will only stop if the users choose to exit by input "n", which makes quit_variable == 0

## if the user inputs "p" here, the game will start.  If "u" here, the unit tests will start.

play_or_test= input('Press p for Play. Press u for Unit tests: ' or 'p')

if play_or_test == 'p':

    if quit_variable == 1:

        main()

        temp = 1

    elif quit_variable == 0:

        exit()

elif play_or_test == 'u':

#### definte the unit test functions #####

    def unit_test(input,output,function_name):

        if input != output:

            print (str(function_name)+" function unit test failed")

        elif input == output:

            print (str(function_name)+" function unit test passed")

    ## unit test 1 on the beginning function

    sizeboard = int(2)

    beginning_output = beginning()

    expected_beginning_output = [['-', '-'], ['-', '-']]

    unit_test(beginning_output,expected_beginning_output,"Unit test 1: beginning")

    ## unit test 2 on the check_state function

    check_state_output = check_state([['-', '-'], ['-', '-']])

    expected_check_state_output = "----"

    unit_test(check_state_output, expected_check_state_output, "Unit test 2: checkstate")

    ## unit test 3 on the check_move() function-1: check move

    go_1_dimension_string = 'o---'

    go_game_general_list = [['o', '-'], ['-', '-']]

    expected_output = int(0)

    unit_test(check_move(), expected_output, "Unit test 3-1: checkstate part 1 move violation: the same being occupied more than once ")

    ## unit test 4 on the check_move() function-2: check move

    go_1_dimension_string = 'o----'

    go_game_general_list = [['o', '-'], ['-', '-']]

    expected_output = int(1)

    unit_test(check_move(), expected_output, "Unit test 3-2: checkstate part 2")

    print ("Unit test 3-3 on the checkstate() function's ko-rule violation test, please see the pseudo codes ")

    ## unit test 5 on the check_move() function-3: check ko-rule {pseduoe code}

    # go_1_dimension_string = 'xo------x-xo------xo'
    #
    # go_game_general_list = "[[ we need to put the ko rule violation example in a 2-D list here for this unit test case. I don't have time to generate it for now]]"
    #
    # expected_output = int(1)
    #
    # unit_test(check_move(), expected_output, "Unit test 3-3: checkstate part 2 no violation ")

    ## unit test 6

    temp = 0

    white_chess = 'o'

    go_game_general_list=[['o', '-'], ['-', '-']]

    # go_game_general_list[y][x] = 'o'

    x=(user_input(white_chess))

    expected_output=[0, 0]

    unit_test(x, expected_output, "Unit test 4: user_input")

    ## unit test 7 on the turn() function {pseudo code}

    ## we can add the "play_or_test" variable in the turn function to make the unit test simpler

    ## in turn()

    ## if temp == 1 and play_or_test == p:

    ##  do whatever the current turn() does

    ## elif temp == 1 and play_or_test == u:

    ##  set all the necessary variables and coordinates for a validate move, and to see if the check_move will return 1 (meaning a valid move)

    ## return a string "valid move"

    ## call the unit test function to test

    ## unit_test(turn(), "valid move", "Unit test 7: turn function ")

    ## unit test 8 on the main() function {pseudo code}

    ## we can do the very similar steps for unit test 7 for the main() unit test

    print ("Unit test 5 & 6 on the turn() and main() function, please see the pseudo codes ")


