import numpy as np
import typing as tp

from abc import ABC, abstractmethod

class Strategy(ABC):
    
    @abstractmethod
    def trade(self, data_generator: tp.Iterator[tuple[int, float, float]], data_size: int, start_balance: float) -> tuple[float, np.array]:
        pass