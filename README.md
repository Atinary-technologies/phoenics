# Phoenics

[![Build Status](https://travis-ci.com/FlorianHase/phoenics.svg?token=rULvnKYmWdFF3JqQBVVW&branch=master)](https://travis-ci.com/FlorianHase/phoenics)

Phoenics is an open source optimization algorithm combining ideas from Bayesian optimization with Bayesian Kernel Density estimation [1]. It performs global optimization on expensive to evaluate objectives, such as physical experiments or demanding computations.

Check out the `examples` folder for detailed descriptions and code examples for:

| Example | Link |
|:--------|:-----|
| Sequential optimization           |  [examples/optimization_sequential](https://github.com/chemos-inc/phoenics/tree/master/examples/optimization_sequential)  |


# Installation

## Environment (Optional)

We suggest to create a new environment for the installation of Phoenics to avoid any compatibility issues with pre-existing python packages. This is optional, but recommended.

This can be done with Venv or Anaconda.

### Venv
```bash
python3.6 -m venv phoenics-env
source phoenics-env/bin/activate
```
A `venv` folder will be created in the current directory and the virtual enviroment will be activated.

### Anaconda
```bash
conda create --name phoenics-env python=3.6
conda activate phoenics-env
```

## Phoenics as pip module

Phoenics can be installed directly with pip.

```bash
apt-get install python-pip
pip install phoenics
```

## Phoenics from source

Phoenics can also be installed from source. This way allows anyone to make and test changes on the code.
```bash
git clone https://github.com/chemos-inc/phoenics.git
cd phoenics
python setup.py install
```

# Dependencies and requirements

This code has been tested with Python 3.6 and 3.7 on Unix platforms and requires the following packages
* numpy
* pyyaml >= 5.1
* sqlalchemy >= 1.3
* watchdog >= 0.9
* wheel >= 0.33

Phoenics requires additional modules for the backend of its Bayesian neural network. Two options are currently supported:
* `tfprob` backend:
  * tensorflow == 1.15
  * tensorflow-probability == 0.8.0
```bash
pip install tensorflow==1.15
pip install tensorflow-probability==0.8.0
```
* `edward` backend:
  * edward == 1.3.5
  * tensorflow == 1.4.1
```bash
pip install edward==1.3.5
pip install tensorflow==1.4.1
```

Note, that the `edward` backend requires Python 3.6 and will not work with Python 3.7.  While at the present time only unix operating system, we hope to provide Windows version of the code in the future.


# Using Phoenics

Phoenics is designed to suggest new parameter points based on prior observations. The suggested parameters can then be passed on to objective evaluations (experiments or involved computation). As soon as the objective values have been determined for a set of parameters, these new observations can again be passed on to Phoenics to request new, more informative parameters.

```python
from phoenics import Phoenics

# create an instance from a configuration file
config_file = 'config.json'
phoenics    = Phoenics(config_file)

# request new parameters from a set of observations
params      = phoenics.recommend(observations = observations)
```
Detailed examples for specific applications are presented in the `examples` folder.

### Disclaimer

Note: This repository is under construction! We hope to add further details on the method, instructions and more examples in the near future.

### Experiencing problems?

Please create a [new issue](https://github.com/chemos-inc/phoenics/issues/new/choose) and describe your problem in detail so we can fix it.

### References

[1] Häse, F., Roch, L. M., Kreisbeck, C., & Aspuru-Guzik, A. [Phoenics: A Bayesian Optimizer for Chemistry.](https://pubs.acs.org/doi/abs/10.1021/acscentsci.8b00307) ACS central science 4.6 (2018): 1134-1145.
