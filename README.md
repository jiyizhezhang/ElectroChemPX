
This is the repository for applying PDBO for reaction optimization problems.

The code in this repository is modified based on PDBO - Pareto Front-Diverse Batch Multi-Objective Bayesian Optimization (10.1609/aaai.v38i10.28951) and follows the original structure. We thank the authors for sharing the code!

## To run the code ##

Please note this code is based on `python 3.8` and the dependencies are listed in `requirements.txt`.

To run the code, use main.py. Examples of reaction simulators can be found in `problems` folder and use main.py to start optimization. The optimization results can be found in `result` folder. 

You could also set up your own problem, simply follow the template in `problems` folder and add information in `common.py` and `problem.py`.

If you want to run the code manually with your experiments, see `run_exp.ipynb` as an example.

## To query the data ##

A lightweight ontology for data management is applied in the study. To query the data, go to the `ontology` folder, run query examples in `query.py`