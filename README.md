## Tech Task

### How to run
1. Install all packages from requirements.txt
```commandline
pip install -r requirements.txt
```
2. Run main script
```commandline
PYTHONPATH=. python src/main.py data/raw.chartblock.json 1 
```

### Strategies
I have implemented three strategies - from baseline to more complicated ones.

All strategies one can find in **src/strategies/** folder.

There are results for these three stategies:

| Strategy | Profit ($) |
| :---: | :---: | 
| BaselineStrategy | 0.08498399999999262 |
| MeduimStrategy | 0.5019369999999981 |
| AdvancedStrategy | 0.5315539999999974 |
