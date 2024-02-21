import random

def getboard(a,b):
  print("-----------------")
#top row
  for i in range(7,4,-1):
    if(i==a):
     print("A",end="\t")
    elif(i==b):
      print("B",end="\t")
    else:
      print(i,end ="\t")
  print()
  #mid row
  if(a==0):
    print("A",end = "\t")
  elif(b==0):
    print("B", end = "\t")
  else:
    print("S", end = "\t")
  if(a==8):
    print("A",end = "\t")
  elif(b==8):
    print("B", end = "\t")
  else:
    print("X", end = "\t")
  if(a==4):
    print("A",end = "\t")
  elif(b==4):
    print("B", end = "\t")
  else:
    print("4", end = "\t")
  print()
  #bottom
  for i in range(1,4):
    if(i==a):
      print("A",end="\t")
    elif(i==b):
      print("B",end="\t")
    else:
      print(i,end ="\t")
  print()
  print("-----------------")
gamewon = False
#safe spot 0, winning spot is 8
playera = 0
playerb = 0
turn = 0
winner = ""
print("Both players start on space 0 and must race to reach 8 with rolls of 1-3 to win!!")
input("Press Enter To START")
print("******************** Game start: *********************")
while (not gamewon):
#safe spot at 0
#if either reaches 8 they win
#if they land on the same spot the first player goes back to 0
#if they land 'above' 8 then their turn is skipped and dice =2/3
#they land on a spot like normal
  if (turn%2 == 0):
    print("******************************************************")
    print("Player A's Turn")
    input("Press Enter key to roll a number from 1-3:")
    roll = roll = random.randint(1,3)
    print("Player A rolled ",roll)
    if(playera+roll == 8):
      gamewon = True
      winner = "Player A"
    elif(playerb == (playera +roll) and playerb!=0):
      playerb = 0
      playera = playera +roll
      print("OH NO!! player B has gone back to the safespace (0)")
      print("Player A has moved to spot:", playera)
    elif(playera+roll > 8):
      print("Player A remains at spot: ", playera)
    else:
      playera = playera + roll
      print("Player A has moved to spot: ", playera)
    getboard(playera,playerb)
  else:
    print("******************************************************")
    print("Player B's Turn")
    input("Press enter key to roll a number from 1-3:")
    roll = roll = random.randint(1,3)
    #player b's turn
    print("Player B rolled ",roll)
    if(playerb + roll ==  8):
      gamewon = True
      winner = "Player B"
      playerb = playerb + roll
    elif(playera == (playerb +roll) and playera!=0):
      playera =0
      playerb = playerb +roll
      print("OH NO!! player A has gone back to the safespace (0)")
      print("Player B has moved to spot:", playerb)
    elif(playerb+roll>8):
      print("Player B remains at spot ", playerb)
    else:
      playerb = playerb + roll
      print("Player B has moved to spot:", playerb)
    getboard(playera,playerb)
  turn = turn + 1
print("The Winner is: ", winner, "!!!!")



#pseudocode
//store the variables needed for the game
player <- 0
otherplayer <- 0
gameWon <-false
winner <- ""
turn = 0
...
while gamewon == false
 //check who's turn it is
 if turnn%2 == 0:
  then 'player 1's turn'
 //initiate turn and dice roll after player clicks enter
 if(player + roll == 8):
  winner <- "player"
  gameWon <- True
 else if(player + roll == otherplayer and otherplayer !=0):
  'player eats the other player and other player goes back to Start'
   otherplayer <-- 0
   player <--  player + roll
 else if (player + roll > 8)
  'player remains in their spot and skips a turn'
 else:
  player <-- player + roll
  'player moves amount of spaces on dice'
 //print the current board state to the user after their turn
 getboard(a,b)
 else:
  'player 2's turn'
  ...
  'same checks are used'
	
 //turn is incrememted at the end of each turn
 turn += 1
//outside of loop
print "Winnner ..."
function getboard(a,b):
'prints the game board from 7 to 1 in descending order'
//with: goal,starting,Player1 and Player2 positions all shown
