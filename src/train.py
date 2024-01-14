import pandas as pd
import numpy as np
import ast
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from src.models.SimpleNN import SimpleNN

def loadData(file):
  df = pd.read_csv(file)

  print(df.head())

  df['board_state'] = df['board_state'].apply(lambda x: ast.literal_eval(x.replace(" ", ",")))
  boardStatesArray = np.array(df['board_state'].values.tolist())
  moves = df['move'].apply(ast.literal_eval).tolist()

  #moves = np.array(moves).reshape(-1, 2)
  moves = np.array(moves)
  columns = moves[:, 1]
  print(columns)
  #encoder = OneHotEncoder(sparse=False)
  numColumns = 7
  encodedMoves = np.eye(numColumns)[columns]

  trainInputs, valInputs, trainOutputs, valOutputs = train_test_split(boardStatesArray, encodedMoves, test_size=0.2, random_state=42)
  trainInputs, valInputs = torch.tensor(trainInputs, dtype=torch.float32), torch.tensor(valInputs, dtype=torch.float32)
  trainOutputs, valOutputs = torch.tensor(trainOutputs, dtype=torch.float32), torch.tensor(valOutputs, dtype=torch.float32)

  return trainInputs, valInputs, trainOutputs, valOutputs

def train(trainInputs, valInputs, trainOutputs, valOutputs, numEpochs):
  model = SimpleNN()

  criterion = nn.BCEWithLogitsLoss()
  optimizer = optim.Adam(model.parameters(), lr=0.001)

  for epoch in range(numEpochs):
    trainOutputsPred = model(trainInputs)
    loss = criterion(trainOutputsPred, trainOutputs)

    loss.backward()
    optimizer.step()

    model.eval()

    valOutputsPred = model(valInputs)

    valLoss = criterion(valOutputsPred, valOutputs)

    print(f'Epoch {epoch + 1}/{numEpochs}, Training Loss: {loss.item()}, Validation Loss: {valLoss.item()}')


