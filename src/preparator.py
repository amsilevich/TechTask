import numpy as np
import typing as tp
import json

class Preparator:
    def __init__(self, data_path: str):
        self.data_path = data_path
        
    def get_data(self) -> tuple[np.array, np.array, tp.Iterator[tuple[int, float, float]]]:
        data_file = open(self.data_path)
        data = json.load(data_file)
        bids, asks = np.array(data[0]['ticks'])[:, 1], np.array(data[1]['ticks'])[:, 1]
        
        def make_generator():
            for i, (bid, ask) in enumerate(zip(bids, asks)):
                yield i, bid, ask
        
        data_generator = make_generator()
        return bids, asks, data_generator