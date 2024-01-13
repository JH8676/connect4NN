import numpy as np
import pandas as pd
import time

from src.enviroments.connect4_game import simulateGame
from src.train import loadData


def main():
  # startTime = time.time()
  # dataset = []

  # for i in range(10000):
  #   gameData = simulateGame()
  #   dataset.extend(gameData)
  
  # endTime = time.time()
  # elapsedTime = endTime - startTime

  # print(elapsedTime)

  # pd.DataFrame(dataset).to_csv('data/raw/training_data.csv', index=False)

  loadData('data/raw/training_data.csv')

if __name__ == '__main__':
  main()

