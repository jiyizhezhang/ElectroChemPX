"""
This is for running reaction simulator, we are providing two simulators here:
(1) A continuous variable reaction simulator, which has all continuous variables.
https://pubs.rsc.org/en/content/articlelanding/2017/re/c6re00109b

(2) A mixed variable reaction simulator, which has both continuous and categorical variables.
https://pubs.rsc.org/en/content/articlelanding/2024/re/d3re00502j

The code structure follows the original repository of PDBO, we thank the authors for sharing their code.
[1] https://github.com/Alaleh/PDBO
"""


import os
os.environ['OMP_NUM_THREADS'] = '1'  # speed up
from helper import *
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore", message="delta_grad == 0.0. Check if the approximated function is linear.")

from arguments import get_args
from baselines.vis_data_export import DataExport
from problems.common import build_problem
from mobo.algorithms import get_algorithm
from utils import save_args, setup_logger

############################################################################
# this is to run close-loop
# change mobo.py to "original code" to get X_next and Y_next
def main():
    args, framework_args = get_args()

    framework_args= {'surrogate': {'surrogate': 'gp', 'n_spectral_pts': 100, 'nu': 5, 'mean_sample': False},
                     'acquisition': {'acquisition': 'EI'},
                     'solver': {'solver': 'nsga2', 'pop_size': 100, 'n_gen': 10, 'pop_init_method': 'nds', 'n_process': 8, 'batch_size': 1},
                     'selection': {'selection': 'dpp', 'batch_size': 1}}

    args.algo = "PDBO"
    # args.problem = "zdt2"

    # This is a reaction simulator with all continuous variables
    args.problem = "Reaction_conti"
    args.n_var = 4  # number of var

    # This is a reaction simulator with all mixed variables
    # args.problem = "Reaction_categ"
    # args.n_var = 8  # number of var

    args.n_obj = 2  # number of obj
    args.n_process = 1  # number of evalation parallel processes
    args.n_iter = 40  # number of iterations
    args.n_init_sample = 10  # initial samples
    args.ref_point = None  # ref points
    args.batch_size = 1  # batch size
    args.n_seed = 10  # random seeds (how many times to run algo)

    np.random.seed(5)
    problem, true_pfront, X_init, Y_init = build_problem(args.problem, args.n_var, args.n_obj, args.n_init_sample, args.n_process)
    args.n_var, args.n_obj = problem.n_var, problem.n_obj


    # # This is for generating initial dataset, the generated dataset is saved in "result" folder
    # import pandas as pd
    # X_df = pd.DataFrame(X_init.copy())
    # Y_df = pd.DataFrame(Y_init.copy())
    # Y_df.iloc[:,0] = -Y_df.iloc[:,0]
    # data = pd.concat([X_df, Y_df], axis=1)
    # data_names = ['var1', 'var2', 'var3', 'var4', 'obj1', 'obj2']
    # data.columns = data_names
    # data.to_csv("result/InitialSet_conti.csv", index=False, header=True)


    print("X_init", X_init)
    print("Y_init",Y_init)
    plt.scatter(-Y_init[:,0], Y_init[:,1])
    plt.show()

    optimizer = get_algorithm(args.algo)(problem, args.n_iter, args.ref_point, framework_args)

    save_args(args, framework_args)
    logger = setup_logger(args)
    print(problem, optimizer, sep='\n')

    exporter = DataExport(optimizer, X_init, Y_init, args)
    solution = optimizer.solve(X_init, Y_init)

    # The results are saved in csv files in "result" folder
    for _ in range(args.n_iter):
        X_next, Y_next = next(solution)
        exporter.update(X_next, Y_next)
        exporter.write_csvs()

    if logger is not None:
        logger.close()


if __name__ == '__main__':
    main()



