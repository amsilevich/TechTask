import numpy as np
import typing as tp

from src.strategies.strategy import Strategy


class MediumStrategy(Strategy):
    
    def trade(self, data_generator: tp.Iterator[tuple[int, float, float]], data_size: int, start_balance: float) -> tp.Tuple[float, np.array]:
        last_i, last_bid, last_ask = next(data_generator)
        min_ask = (last_ask, last_i)
        balance = start_balance
        transactions = []

        while last_i != data_size - 1:
            i, bid, ask = next(data_generator)
            min_ask = min_ask if min_ask[0] < last_ask else (last_ask, last_i)
            
            if bid > min_ask[0]:
                i_to_sell, bid_to_sell = i, bid
                cnt = 0
                while i != data_size - 1:
                    i, bid, ask = next(data_generator)
                    if bid >= bid_to_sell:
                        i_to_sell, bid_to_sell = i, bid 
                        continue
                    transactions.append((min_ask[1], i_to_sell))
                    balance += (bid_to_sell - min_ask[0]) * int(balance / min_ask[0])
                    min_ask = (ask, i)
                    break
                
            last_i, last_bid, last_ask = i, bid, ask 

        return balance, np.array(transactions)



