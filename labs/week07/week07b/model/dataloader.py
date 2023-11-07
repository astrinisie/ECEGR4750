import torch
import math

class CustomDataloader():
    """
    Wraps a dataset and enables fetching of one batch at a time
    """
    def __init__(self, x: torch.Tensor, y: torch.Tensor, batch_size: int = 1, randomize: bool = False):
        self.x = x
        self.y = y
        self.batch_size = batch_size
        self.randomize = randomize
        self.iter = None
        self.num_batches_per_epoch = math.ceil(self.get_length() / self.batch_size)

    def get_length(self):
        return self.x.shape[0]

    def randomize_dataset(self):
        """
        This function randomizes the dataset, while maintaining the relationship between 
        x and y tensors
        """


    def generate_iter(self):
        """
        This function converts the dataset into a sequence of batches, and wraps it in
        an iterable that can be called to efficiently fetch one batch at a time
        """

    
    def fetch_batch(self):
        """
        This function calls next on the batch iterator, and also detects when the final batch
        has been run, so that the iterator can be re-generated for the next epoch
        """
