import torch
import torch.nn as nn

# adapted from LearningModel from prior lab
class FullyConnectedNetwork(nn.Module): 
    def __init__(self, input_dim: int, hidden_dim: int):
        super(FullyConnectedNetwork, self).__init__()
        assert input_dim > 0, "Input dimension must be a positive integer"
        assert hidden_dim > 1, "Hidden dimensions must be an integer greater than 1"
        self.linear1 = nn.Linear(in_features = input_dim, out_features = hidden_dim)
        self.linear2 = nn.Linear(in_features = hidden_dim, out_features = round(hidden_dim//2))
        self.linear3 = nn.Linear(in_features = round(hidden_dim//2), out_features = 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.relu(x)
        x = self.linear3(x)       
        return x



# have students write this one themselves
class FCNClassifier(nn.Module): 
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super(FCNClassifier, self).__init__()
        assert input_dim > 0, "Input dimension must be a positive integer"
        assert hidden_dim > 1, "Hidden dimensions must be an integer greater than 1"
        assert output_dim > 0, "Output dimension must be a positive integer"
        self.linear1 = nn.Linear(in_features = input_dim, out_features = hidden_dim)
        self.linear2 = nn.Linear(in_features = hidden_dim, out_features = round(hidden_dim//2))
        self.linear3 = nn.Linear(in_features = round(hidden_dim//2), out_features = output_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.relu(x)
        x = self.linear3(x)     
        x = torch.sigmoid(x)  
        return x