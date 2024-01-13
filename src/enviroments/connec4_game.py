import numpy as np

class Connect4Game:
  def connect4game(self):
    board = np.zeros((6, 7),dtype=int)

    for i in range(42):
      print("Yellows's go")
      while True:
        move = self.convertCoords((np.random.randint(0,7),np.random.randint(0,6)))
        if self.isLegalMove(board, move):
          board = self.makeMove(board, move, 'yellow')
          break
    
      print(board)
      if self.checkWin(board, 'yellow'):
        break
    
      print("Red's go")
      while True:
        move = self.convertCoords((np.random.randint(0,7),np.random.randint(0,6)))
        if self.isLegalMove(board, move):
          board = self.makeMove(board, move, 'red')
          break

      print(board)
      if self.checkWin(board, 'red'):
        break
      

  def makeMove(self, currentBoard, position, colour):
    if colour == 'yellow':
      currentBoard[position] = 1
    else:
      currentBoard[position] = 2

    return currentBoard
  
  def isLegalMove(self, currentBoard, position):
    if (currentBoard[position] == 0 and ((position[0] == 5) or (currentBoard[position[0]+1, position[1]] != 0))):
      return True
    else:
      return False

  def convertCoords(self, coords):
    newCoords = (5 - coords[1], coords[0])
    return newCoords

  def checkWin(self, currentBoard, colour):
    if colour == 'yellow':
      symbol = 1
    else:
      symbol = 2

    for row in currentBoard:
      if any(np.all(row[i:i+4] == symbol) for i in range (len(row) - 3)):
        print(symbol, " horizontal")
        return True
      
    for col in currentBoard.T:
          if any(np.all(col[i:i+4] == symbol) for i in range(len(col) - 3)):
              print(symbol, " vertical")
              return True
          
    for i in range(len(currentBoard) - 3):
          for j in range(3, len(currentBoard[0])):
              if all(currentBoard[i+k][j-k] == symbol for k in range(4)):
                  print(symbol, " diagonal")
                  return True
    
    return False
  
def simulateGame():
  game = Connect4Game()
  game.connect4game()