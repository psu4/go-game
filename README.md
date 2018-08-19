go-game

Written by Pin-Chih Su 2017-08-17

Tested in python 3.6.1.

To reproduce the python environment,

please copy the "environment.yml" into the path and run

conda env create -f environment.yml

Here is the instruction of how to install mini-conda (https://conda.io/docs/user-guide/install/linux.html)

After the python environment is set up, please run

python go_pin-chih.py

to reproduce the results.

Please contact Pin-Chih at "dr.pin.chih.su@gmail.com" if any question.  Thanks.


1. How to run this code?

1.a: python go_pin-chih.py

1.b: Press p for Play. Press u for Unit tests:

1.c: if press "p", the game will be in the play mode.  if press "u", the code will run unit tests on its functions.

1.d: Please select how big the N X N square game board you would like to have. Please enter N as an integer.  If no value is provided, the default value is 9 X 9

1.e: the following is the default 9X9 output:

- - - - - - - - -
- - - - - - - - -
- - - - - - - - -
- - - - - - - - -
- - - - - - - - -
- - - - - - - - -
- - - - - - - - -
- - - - - - - - -
- - - - - - - - -
There are still 81 empty positions left.
The o occupied 0 positions
The x occupied 0 positions

place for o
Press y for Place, n for Quit  (y/n)?

1.f: the turn of the player "o". If press "y", then users can input x & y coordinates to place the move.  For a 9X9 game board, the coordinates from the upper left to lower right are (0,0) and (8,8) correspondingly.

1.g: the turn of the player "x". If press "y", then users can input x & y coordinates to place the move.  For a 9X9 game board, the coordinates from the upper left to lower right are (0,0) and (8,8) correspondingly.

1.h: if any user presses "n", then the game will be ended.

1.i: the game will continue until the whole game board is filled or any user presses "n"

1.j: the game state is constantly evaluated and shown during every move:

There are still 80 empty positions left.
The o occupied 1 positions
The x occupied 0 positions

1.k: the following moves are not allowed:

(1) the move is on the same location as any previous move.  If violated, the error message is "Invalid coordinate.  This coordinate has been occupied."

(2) the ko rule violation (only works in 9X9 game board size):

         In a 9X9 board,

         - - - - - - - - -
         - - - - - - - - -
         - - - o x - - - -
         - - o x - x - - -
         - - - o x - - - -
         - - - - - - - - -
         - - - - - - - - -
         - - - - - - - - -
         - - - - - - - - -

         the o player is not allowed to move into the following

         - - - - - - - - -
         - - - - - - - - -
         - - - o x - - - -
         - - o x o x - - -
         - - - o x - - - -
         - - - - - - - - -
         - - - - - - - - -
         - - - - - - - - -
         - - - - - - - - -

If violated, the warning message is "Warning: there is a ko rule violation!! Try to move again!!".


2. Unit tests

Unit test 1: beginning function

Unit test 2: checkstate function

Unit test 3-1: checkstate part 1 move violation: the same being occupied more than once

Unit test 3-2: checkstate part 2 function

Unit test 3-3 on the checkstate() function's ko-rule violation test, please see the pseudo codes

Unit test 4: user_input function

Unit test 5 & 6 on the turn() and main() function, please see the pseudo codes

3. Design decisions:

there are several functions such as beghinning, checkstate, user_input to allow user inputs to control the board size, move coordinates, and move validation etc.

If players input "p" when asked "Press p for Play. Press u for Unit tests:", the code is in the game mode.

Then the main() function call and combine all the previous functions together to make the game run.

If players input "n" when asked "Press p for Play. Press u for Unit tests:", the code runs several unit tests to test its functions.

More details are available in the comments inside the code


4. Trade offs & extensibility:

4.a: there is no life and death scenario considered.  This can be done by potentially adding a few more functions which can be called by the main() function.

4.b: the ko rule violation checks only works for the 9X9 game board. We can extend the regular expression checks in the check_move() function to make the ko rule check works for different sizes of the game board.

4.c: the unit tests can be improved with coverages on mocking user inputs, and testing more extensively in different user options.

4.d: the go game should only be ended if both users quit instead of the current state, where just an user quitting ends the game.

4.e: More command line options should be provided such as player names.  Training game board images with convolutional neural networks potentially can build an AI opponent again a human player.


