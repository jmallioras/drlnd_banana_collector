import torch
import torch.nn as nn
import torch.nn.functional as F

class QNet(nn.Module):
    def __init__(self, state_size, action_size, seed, h_sizes=[64, 128], activation_names = ["relu", "relu"]):
        super(QNet,self).__init__()
        self.seed = torch.manual_seed(seed)
        self.linears = nn.ModuleList([nn.Linear(state_size, h_sizes[0])])
        self.nlayers = len(h_sizes)
        for nlayer in range(self.nlayers-1):
            self.linears.append(nn.Linear(h_sizes[nlayer],h_sizes[nlayer+1]))
        self.linears.append(nn.Linear(h_sizes[-1],action_size))
        self.activation_functions = [getattr(F, name) for name in activation_names]
        print(f"DQN Structure created! \nLayers: {self.linears} \nActivation Functions:{self.activation_functions}")

    def forward(self, x):
        for layer in range(self.nlayers):
            x = self.activation_functions[layer](self.linears[layer](x))
        return self.linears[-1](x)

