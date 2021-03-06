import os
os.system('cls' if os.name == 'nt' else 'clear')

#get the players choice of square
def take_turn(player, squares):
	turn_taken = False

	while turn_taken == False:
		players_choice = input(player + " what square would you like to take: ")
		if squares[players_choice] == "o" or squares[players_choice] == "x":
			print("This square has already been taken. Try again.")
		else:
			turn_taken = True

	return players_choice

#print all the squares
def print_grid(squares):
	print("\t", squares.get("A1"), "|", squares.get("A2"), "|", squares.get("A3"))
	print("\t", "----------")
	print("\t", squares.get("B1"), "|", squares.get("B2"), "|", squares.get("B3"))
	print("\t", "----------")
	print("\t", squares.get("C1"), "|", squares.get("C2"), "|", squares.get("C3"))


#check if all squares have been taken
def draw_check(squares):
	if (" " in squares.values()) == False:
		print("Cats game. No winners this time :(")
		print_grid(squares)
		return True
	elif (" " in squares.values()) == True:
		return False

squares = {"A1":" ", "A2":" ", "A3":" ", "B1":" ", "B2":" ", "B3":" ", "C1":" ", "C2":" ", "C3":" "}

player_one = input("Player one - please enter your name: ")
player_two = input("Player two - please enter your name: ")

print(player_one, " you are noughts (o)")
print(player_two, " you are crosses (x)")

game_over = False

print_grid(squares)

while game_over == False:

	print("\n")
	#player one takes a turn and then checks if they have won
	squares[take_turn(player_one, squares)] = "o"

	if (squares.get("A1") == "o" and squares.get("A2") == "o" and squares.get("A3") == "o") or (squares.get("B1") == "o" and squares.get("B2") == "o" and squares.get("B3") == "o") or (squares.get("C1") == "o" and squares.get("C2") == "o" and squares.get("C3") == "o") or (squares.get("A1") == "o" and squares.get("B1") == "o" and squares.get("C1") == "o") or (squares.get("A2") == "o" and squares.get("B2") == "o" and squares.get("C2") == "o") or (squares.get("A3") == "o" and squares.get("B3") == "o" and squares.get("C3") == "o") or (squares.get("A1") == "o" and squares.get("B2") == "o" and squares.get("C3") == "o") or (squares.get("C1") == "o" and squares.get("B2") == "o" and squares.get("A3") == "o"):
		game_over = True
		print(player_one, " has won!!!")
		print_grid(squares)
		continue

	if draw_check(squares) == True:
		game_over = True
		continue

	#player two takes a turn and then checks if they have won
	squares[take_turn(player_two, squares)] = "x"

	if (squares.get("A1") == "x" and squares.get("A2") == "x" and squares.get("A3") == "x") or (squares.get("B1") == "x" and squares.get("B2") == "x" and squares.get("B3") == "x") or (squares.get("C1") == "x" and squares.get("C2") == "x" and squares.get("C3") == "x") or (squares.get("A1") == "x" and squares.get("B1") == "x" and squares.get("C1") == "x") or (squares.get("A2") == "x" and squares.get("B2") == "x" and squares.get("C2") == "x") or (squares.get("A3") == "x" and squares.get("B3") == "x" and squares.get("C3") == "x") or (squares.get("A1") == "x" and squares.get("B2") == "x" and squares.get("C3") == "x") or (squares.get("C1") == "x" and squares.get("B2") == "x" and squares.get("A3") == "x"):
		game_over = True
		print(player_two, " has won!!!")
		print_grid(squares)
		continue

	if draw_check(squares) == True:
		game_over = True
		continue

	print_grid(squares)
