## Tech Task

### Strategies
I have implemented four strategies - from baseline to more complicated ones.

All strategies one can find in **src/strategies/** folder.

There are results for these three stategies:

| Strategy | Profit ($) |
| :---: | :---: | 
| BaselineStrategy | 0.084984 |
| MeduimStrategy | 0.501937 |
| AdvancedStrategy | 0.531554 |
| IdealStrategy | 0.5832 |

The **IdealStrategy** is stricly the best strategy in task's requirements conditions.


### How to run
1. Install all packages from requirements.txt
```commandline
pip install -r requirements.txt
```
2. Run main script
```commandline
PYTHONPATH=. python src/main.py data/raw.chartblock.json 1 
```

P.S. By default script runs **IdealStrategy**, which has the best score.
