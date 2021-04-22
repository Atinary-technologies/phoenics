## Data-driven experiment planning strategies 

Phoenics [1] is a data-driven experiment planning strategy based on principles of Bayesian optimization in combination with Bayesian kernel density estimation to perform cost-effective global optimization on physical experiments and/or resource-intensive computations. Among several functionalities, Phoenics targets data-driven experiment planning tasks particularly in the context of chemistry and materials science. It is possible to use Phoenics for the rapid identification of optimal continuous process parameters for physical experiments or computations. Phoenics natively supports sequential and batch-wise optimizations. 

![continuous_integration](https://github.com/chemos-inc-dev/phoenics/workflows/Continuous%20integration/badge.svg)
[![codecov](https://codecov.io/gh/chemos-inc-dev/phoenics/branch/dev/graph/badge.svg?token=anTJ0HXjI6)](https://codecov.io/gh/chemos-inc-dev/phoenics)
![github_license](https://img.shields.io/github/license/chemos-inc/phoenics)
![github_issues](https://img.shields.io/github/issues/chemos-inc/experiment_planners)
![pypi_version](https://img.shields.io/pypi/v/phoenics)

Check out our `examples` for a few highlights and use cases of Phoenics.

| Example | Link |
|:--------|:-----|
| Sequential optimization           |  [examples/optimization_sequential](https://github.com/atinary-technologies/phoenics/tree/master/examples/optimization_sequential)  |



## Getting started

Phoenics is developed for Linux based systems. Although we hope that you will not encounter any issues we would appreciate if you contacted us should you run into any of them.

To install Phoenics from source you can clone this repository and execute the following steps.

#### From source
```
git clone https://github.com/atinary-technologies/phoenics.git
cd phoenics
pip install -r requirements.txt
pip install .
```

*NOTE:*: We recommend to install Phoenics in a separate environment which could be created with [`venv`](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) or [`anaconda`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 


## Running Phoenics

Phoenics identifies optimal parameter choices in a closed-loop approach. Given a set of prior observations, consisting of evaluated parameters and associated measurements, it can recommend several parameter choices for future evaluation. 

A basic skeleton of the code to run Phoenics in a single-objective optimization problem is as follows:
```
from phoenics import Phoenics

##  BUDGET (int): number of evaluations of the black-box function we want to optimize.
##  benchmark (function): 'black box' function that returns the merit (scalar) obtained for a certain parameter setup.

# create an instance from a configuration file
CONFIG_FILE = 'config.json'
phoenics = Phoenics(CONFIG_FILE)

observations = []
for _ in range(BUDGET):

    # phoenics recommends a number of parameter setups to evaluate based on previous observations
    samples  = phoenics.recommend(observations = observations)

    for sample in samples:
        # black-box function is queried with the recommended parameter setups
        measurement   = benchmark(sample)
        observations.append(measurement)
```

*NOTE:* measurement is expected to be a python dictionary with as many keys as objectives the optimation problem has. The merit for each objective is given by the value of the corresponding key.

## Configuration file

The config file (`config.json`) defines the optimization problem and the setup of Phoenics. It must contain the three following fields: `general`, `parameters` and `objectives`.

- `general`. It contains hyperparameter choices that will affect the performance of Phoenics. The whole list of hyperparameters and their default values are available at `src/phoenics/utilities/defaults.py`. An important hyperparameter (type) is:
    - `sampling_strategies` (int): Number of acquisition functions as per the Phoenics framework. By default, *n* sampling strategies are sampled evenly across the interval [-1, 1], i.e. `lambdas = np.linspace(-1, 1, n)`.

- `parameters`. It characterizes the parameters that are to be optimized. Phoenics only supports continuous parameters. For problems with categorical, discrete and/or categorical parameters we refer the user to the [Gryffin github](https://github.com/Atinary-technologies/gryffin) repositoryi [2]. Continuous parameters are characterized with a number of attributes.
    - `high` (float): The parameter is upper bounded by this value.
    - `low` (float): The parameter is lower bounded by this value.
    - `size` (int): It enables the possibility to define a number of parameters with the same characteristics (i.e., `high` and `low` hyperparameter values) at once.

- `objectives`. It enumerates the list of objectives to optimize. For the case where the user defines more than one objective, all objectives are aggregated into one single objective based on the Chimera framework [3]. In either case, each objective must always be characterized with:
    - `name` (str): Name of the property to be optimized.
    - `goal` (maximize/minimize).

    Moreover, for multi-objective optimization problems there are additional attributes that must be provided:
    - `hierarchy` (int): hierarchy importance for each individual objective. The lower the more relevant it becomes.
    - `tolerance` (float): relative tolerance value.

For a more detailed description of each hyperparameter, we refer the user to [1] and [3].

## Optimization of analytical functions

The goal of bayesian optimization is to find the parameter setup that maximizes/minimizes a black-box function. For benchmarking purposes, optimization techniques are often evaluated in functions whose analytical form is known. The `benchmark_functions.py` file contains examples of known functions such as Dejong, Camel or Ackley.


### References

[1] Häse, F., Roch, L. M., Kreisbeck, C., & Aspuru-Guzik, A. [Phoenics: A Bayesian Optimizer for Chemistry.](https://pubs.acs.org/doi/abs/10.1021/acscentsci.8b00307) *ACS Cent. Sci.* **4**.6 (2018): 1134-1145.

[2] Häse, F., Roch, L.M. and Aspuru-Guzik, A., 2020. Gryffin: An algorithm for Bayesian optimization for categorical variables informed by physical intuition with applications to chemistry. arXiv preprint arXiv:2003.12127.

[3] Häse, F., Roch, L. M. and  Aspuru-Guzik, A. Chimera: Enabling hierarchy based multi-objective optimization for self-driving laboratories. Chemical Science 2018, 9(39), 7642-7655.

