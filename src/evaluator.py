import numpy as np
import typing as tp

from src.strategies.strategy import Strategy


class Evaluator:
    def __init__(self, bids: np.array, asks: np.array, data_generator: tp.Iterator[tuple[int, float, float]]):
        assert bids.size == asks.size
        
        self.n = bids.size
        self.bids: np.array = bids
        self.asks: np.array = asks
        self.data_generator: tp.Iterator[tuple[int, float, float]] = data_generator

    def check_valid(self, transactions) -> bool:
        flatten_transactions = transactions.reshape(-1)
        flatten_transactions_sorted = np.sort(flatten_transactions)
        assert np.array_equal(flatten_transactions, flatten_transactions_sorted)
        
        flatten_transactions_unique = set(flatten_transactions)
        assert flatten_transactions.size == len(flatten_transactions_unique)
        
        for buy, sell in transactions:     
            assert self.asks[buy] < self.bids[sell]   
            assert self.asks[buy:sell+1].min() == self.asks[buy]
            assert self.bids[buy:sell+1].max() == self.bids[buy:sell+1][-1]
        
    def calculate_profit(self, strategy: Strategy, start_balance: float) -> float:
        final_balance, transactions =  strategy.trade(self.data_generator, self.n, start_balance)
        self.check_valid(transactions)
        
        profits = []
        check_balance = start_balance
        for (buy, sell) in transactions:
            count: int = int(check_balance / self.asks[buy])
            check_balance += (self.bids[sell] - self.asks[buy]) * count
            profits.append((self.bids[sell] - self.asks[buy]) * count)
        
        assert final_balance == check_balance
        return final_balance - start_balance