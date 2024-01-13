import numpy as np
import random

class Connect4Game:
  def __init__(self):
      self.availableMoves = list((y, x) for y in range(6) for x in range(7))

  def connect4game(self):
    trainingData = []

    board = np.zeros((6, 7),dtype=int)
    random.shuffle(self.availableMoves)

    while len(self.availableMoves) != 0:
      while True:
        moveIndex = np.random.randint(len(self.availableMoves))
        move = self.availableMoves[moveIndex]
        if self.isLegalMove(board, move):
          self.updatePossibleMoves(move)
          board = self.makeMove(board, move, 'yellow')

          turnData = {
            'board_state': board,
            'move': move
          }

          trainingData.append(turnData)
          break
    
      if self.checkWin(board, 'yellow'):
        break
    
      while True:
        moveIndex = np.random.randint(len(self.availableMoves))
        move = self.availableMoves[moveIndex]
        if self.isLegalMove(board, move):
          self.updatePossibleMoves(move)
          board = self.makeMove(board, move, 'red')

          turnData = {
            'board_state': board,
            'move': move
          }

          trainingData.append(turnData)
          break

      if self.checkWin(board, 'red'):
        break

    return trainingData
      

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
        return True
      
    for col in currentBoard.T:
          if any(np.all(col[i:i+4] == symbol) for i in range(len(col) - 3)):
              return True
          
    for i in range(len(currentBoard) - 3):
          for j in range(3, len(currentBoard[0])):
              if all(currentBoard[i+k][j-k] == symbol for k in range(4)):
                  return True
    
    return False

  def updatePossibleMoves(self, move):
    self.availableMoves.remove(move)
  
def simulateGame():
  game = Connect4Game()
  return game.connect4game()