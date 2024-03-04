import json
import sys

from preparator import Preparator
from evaluator import Evaluator
from strategies.advanced import AdvancedStrategy
from src.strategies.ideal import IdealStrategy
from strategies.medium import MediumStrategy
from strategies.baseline import BaselineStrategy


if __name__ == "__main__":
    DATA_PATH = sys.argv[1]
    START_BALANCE = int(sys.argv[2])

    preparator = Preparator(DATA_PATH)
    evaluator = Evaluator(*preparator.get_data())
    strategy = IdealStrategy()
    profit = evaluator.calculate_profit(strategy, START_BALANCE)
    print("TOTAL STRATEGY PROFIT IS: ", round(profit, 8), "$", sep='')
