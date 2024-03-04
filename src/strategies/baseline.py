import numpy as np
import typing as tp

from src.strategies.strategy import Strategy


class BaselineStrategy(Strategy):
    
    def trade(self, data_generator: tp.Iterator[tuple[int, float, float]], data_size: int, start_balance: float) -> tp.Tuple[float, np.array]:
        last_i, last_bid, last_ask = next(data_generator)
        balance = start_balance
        transactions = []
        skip = False
        
        while last_i != data_size - 1:
            i, bid, ask = next(data_generator)
            if not skip and bid - last_ask > 0:
                balance += int(balance / last_ask) * (bid - last_ask)
                transactions.append([last_i, i])
                skip = True
            elif skip == True:
                skip = False
            last_i, last_bid, last_ask = i, bid, ask

        return balance, np.array(transactions)
