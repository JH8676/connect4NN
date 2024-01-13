import pandas as pd
import numpy as np
import ast
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def loadData(file):
  df = pd.read_csv(file)

  print(df.head())

  df['board_state'] = df['board_state'].apply(lambda x: ast.literal_eval(x.replace(" ", ",")))
  boardStatesArray = np.array(df['board_state'].values.tolist())
  moves = df['move'].apply(ast.literal_eval).tolist()

  moves = np.array(moves).reshape(-1, 2)
  encoder = OneHotEncoder(sparse=False)
  encodedMoves = encoder.fit_transform(moves)

  print("Game States:", boardStatesArray[:5])
  print("Encoded Moves:", encodedMoves[:5])  
