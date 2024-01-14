import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class SimpleNN(nn.Module):
  def __init__(self):
    super(SimpleNN, self).__init__()
    self.fc1 = nn.Linear(42, 128)
    self.tanh = nn.Tanh()
    self.fc2 = nn.Linear(128, 7)
    self.softmax = nn.Softmax(dim=1)

  def forward(self, x):
    x = x.view(-1, 42)
    x = self.fc1(x)
    x = self.tanh(x)
    x = self.fc2(x)
    x = self.softmax(x)
    return x