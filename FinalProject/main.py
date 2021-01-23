import random, time, copy
from termcolor import cprint
from os import system, name

#Clears terminal
def clear():

	# for Windows
	if name == 'nt':
		_ = system('cls')
		
	# for Mac and Linux (here, os.name is
	else:
		_ = system('clear')

clear()

#Introduction
print()
cprint('Welcome to MineSweeper v.3.0!', 'cyan')
cprint('=============================', 'cyan')
print()
cprint('Excited to declare version 3.0 of MineSweeper as almost fully functional!', 'cyan')


#Sets up the game.
def reset():
	print('''
MAIN MENU
=========

-> For instructions on how to play, type 'I'
-> To play immediately, type 'P'
''')

	choice = input('Type here: ').upper()

	if choice == 'I': #If player typed "I", clears terminal, prints the instructions.txt
		clear()
		
		#Prints instructions
		print(open('instructions.txt', 'r').read())
		
		input('Press [enter] when ready to play. ')
		
	elif choice != 'P':
		clear()
		reset()
		
	#The solution grid. A list of lists, each index of b is a row and each index of a row is a column
	b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


	#The two for loops go through each square in the grid, by cycling through the x and y coordinates, r and c. 
	
	for n in range (0, 10):
		placeBomb(b)
		
	for r in range (0, 9):
		for c in range (0, 9):
			value = l(r, c, b)
			if value == '*':
				updateValues(r, c, b)
				
	#Sets the variable k to a grid of blank spaces, because nothing is yet known about the grid.
	k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]			

	printBoard(k)
	
	#start the timer
	startTime = time.time()
		
	#the game begins!
	play(b, k, startTime)

#Places a bomb in a random location.
def placeBomb(b):
	r = random.randint(0, 8)	#row
	c = random.randint(0, 8)	#column
	
	#Checks if there's a bomb in the randomly generated loactaion. If not, it puts one
	currentRow = b[r]	#gets the row, one of the lists in b
	if not currentRow[c] == '*':	#if theres no bomb, put a sucka in there
		currentRow[c] = '*'
	else:
		placeBomb(b)		#if there is a bomb, then bruh you gotta just roll again ;-;
	
	
#Adds 1 to all of the squares around a bomb.
def updateValues(rn, c, b):

    #Row above.
    if rn-1 > -1:
        r = b[rn-1]
        
        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

    #Same row.    
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 9 > c+1:
        if not r[c+1] == '*':
            r[c+1] += 1

    #Row below.
    if 9 > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1
           

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1
                
                			
#Gets the value of a coordinate on the grid.
#l stands for location
def l(r, c, b):
    return b[r][c]


#prints the given board
def printBoard(b):
	clear()
	print('    A   B   C   D   E   F   G   H   I')
	print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
	
	for r in range (0, 9):
		print(r,'║',l(r,0,b),'║',l(r,1,b),'║',l(r,2,b),'║',l(r,3,b),'║',l(r,4,b),'║',l(r,5,b),'║',l(r,6,b),'║',l(r,7,b),'║',l(r,8,b),'║')
		if not r == 8:
			print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
	print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')
	
#the above for loop runs 9 times, changing r (the row number) each time


def play(b, k, startTime):
	#player chooses square
	c, r = choose(b, k, startTime)
	
	#gets the value at that location
	v = l(r, c, b)
	
	if v == '*':
		printBoard(b)
		cprint('aha ha- ur ded, loser', 'red')
		
		#print timer result
		print('Time: ' + str(round(time.time() - startTime)) + 's')
		
		#offer to play again
		playAgain = input('Rematch to prove your worth???? (Y/N): ').lower()
		if playAgain == 'y':
			clear()
			reset()
			
		else:
			quit()
			
	#Puts that value into the known grid (k)
	k[r][c] = v
	
	#runs checkZeros() if that value is a 0
	if v == 0:
		checkZeros(k, b, r, c)
	printBoard(k)
	
	squaresLeft = 0
	for x in range (0, 9):
		row = k[x]
		squaresLeft += row.count(' ')
		squaresLeft += row.count('⚐')
		
	if squaresLeft == 10:
		printBoard(b)
		cprint('WINNER WINNER CHICKEN DINNER', 'cyan')
		
		#print timer
		print('Time: ' + str(round(time.time() - startTime)) + 's')
		
		#offer to play again
		playAgain = input('U wanna rematch??? Prove ur worth???, BET! (Y/N): ')
		playAgain = playAgain.lower()
		if playAgain == 'y':
			clear()
			reset()
		else:
			quit()
			
	play(b, k, startTime)

#the player chooses a location
def choose(b, k, startTime):
#variables
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	
	#loop in case of invalid entry
	while True:
		chosen = input('Choose a square (eg. E4) or place a marker (eg. mE4): ').lower()
		
		#checks for valid square
		if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
			c, r = (ord(chosen[1]))-97, int(chosen[2])
			marker(r, c, k)
			play(b, k, startTime)
			break
			
		elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers:
			return (ord(chosen[0]))-97, int(chosen[1])
			
		else:
			choose(b, k, startTime)
#python function 'ord()' stands for ordinal, and returns the ASCII value of whatever character you give it, and from it we can get the numerical equivalent of a letter without the need for an alphabet variable.


#places a marker in the given location
def marker(r, c, k):
	k[r][c] = '⚐'
	printBoard(k)


#checks known grid for 0s
def checkZeros(k, b, r, c):
	oldGrid = copy.deepcopy(k) #makes a copy of the known grid
	zeroProcedure(r, c, k, b)
	if oldGrid == k:
		return
	while True:
		oldGrid = copy.deepcopy(k)
		for x in range (9):
			for y in range (9):
				if l(x, y, k) == 0:
					zeroProcedure(x, y, k, b) #opens the squares
		if oldGrid == k:
			return

def zeroProcedure(r, c, k, b):
	#row above
	if (r-1 > -1):
		row = k[r-1]
		if (c-1 > -1):
			row[c-1] = l(r-1, c-1, b)
		row[c] = l(r-1, c, b)
		if (9 > c+1):
			row[c+1] = l(r-1, c+1, b)
			
	#same row
	row = k[r]
	if (c-1 > -1):
		row[c-1] = l(r, c-1, b)
	if (9 > c+1):
		row[c+1] = l(r, c+1, b)
		
	#row below
	if (9 > r+1):
		row = k[r+1]
		if (c-1 > -1):
			row[c-1] = l(r+1, c-1, b)
		row[c] = l(r+1, c, b)
		if (9 > c+1):
			row[c+1] = l(r+1, c+1, b)



reset()

# ═ ║ ╔ ╦ ╗ ╠ ╬ ╣ ╚ ╩ ╝














