# Data-driven experiment planning strategies 

This repository offers data-driven experiment planning strategies following principles of Bayesian optimization in combination with Bayesian kernel density estimation to perform cost-effective global optimization on physical experiments and/or resource-intensive computations.

The mathematical formulation of this algorithms provided in this repository are based on Phoenics [1]. Among several functionalities, Phoenics targets data-driven experiment planning tasks particularly in the context of chemistry and materials science. It is possible to use Phoenics for the rapid identification of optimal continuous process parameters for physical experiments or computations. Phoenics natively supports sequential and batch-wise optimizations. 

![continuous_integration](https://github.com/chemos-inc-dev/phoenics/workflows/Continuous%20integration/badge.svg)
[![codecov](https://codecov.io/gh/chemos-inc-dev/phoenics/branch/dev/graph/badge.svg?token=anTJ0HXjI6)](https://codecov.io/gh/chemos-inc-dev/phoenics)
![github_license](https://img.shields.io/github/license/chemos-inc/phoenics)
![github_issues](https://img.shields.io/github/issues/chemos-inc/phoenics)
![pypi_version](https://img.shields.io/pypi/v/phoenics)

Check out our `examples` for a few highlights and use cases of Phoenics.

| Example | Link |
|:--------|:-----|
| Sequential optimization           |  [examples/optimization_sequential](https://github.com/chemos-inc/phoenics/tree/master/examples/optimization_sequential)  |



### Getting started

Phoenics is developed for Linux based systems. We also support MacOS and Windows, but support for these platforms is experimental at the moment. Although we hope that you will not encounter any issues we would appreciate if you contacted us should you run into any of them.

###### Option 1 (recommended)
Phoenics can be installed for all three platforms via pip
```
pip install phoenics 
```

###### Option 2
For Linux systems, Phoenics is also available through anaconda
```
conda install -c chemos phoenics
```

###### Option 3
If you would like to install `Phoenics` from source you can clone this repository and execute the following steps

```
git clone https://github.com/chemos-inc/phoenics.git
cd phoenics
python -m pip install -U pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

The partial installation of `Phoenics` with a particular backend is possible via 
```
pip install -e .[<backend>]
```
or
```
pip install -e .\[<backend>\]
```
when using a Z shell, where `<backend>` indicates the selected backend (`edward` or `tfprob`).

**Note**: We recommend to install Phoenics in a separate environment which could be create with [`venv`](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) or [`anaconda`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 


##### Dependencies 

Phoenics is developed for Python >= 3.6 and supported on plaforms based on Unix and Windows 10. It relies on the following Python packages (summarized in `requirements.txt`):

- `numpy` 
- `pyyaml` >= 5.1
- `sqlalchemy` >= 1.3
- `watchdog` >= 0.9
- `wheel` >= 0.33

For an installation on a Windows platform, we additionally require the `Microsoft C++ Build Tools` ([download link](https://visualstudio.microsoft.com/visual-cpp-build-tools/)).

The inference steps of the algorithm are implemented in two different backends. The latest version runs on 

- `tensorflow` == 1.15
- `tensorflow-probability` == 0.8
- `python` >= 3.7

but we also support the older versions 

- `tensorflow` == 1.4.1
- `edward` == 1.3.5
- `python` <= 3.6


### Running Phoenics

Phoenics identifies optimal parameter choices in a closed-loop approach. Given a set of prior observations, consisting of evaluated parameters and associated measurements, it can recommend several parameter choices for future evaluation. 

```python
from phoenics import Phoenics

# create an instance from a configuration file
config_file = 'config.json'
phoenics    = Phoenics(config_file)

# request new parameters from a set of observations
params = phoenics.recommend(observations=observations)
```
Detailed examples for specific applications are presented in the [examples](https://github.com/chemos-inc/phoenics/tree/master/examples) folder.

### Disclaimer

Note: This repository is under construction! We hope to add further details on the method, instructions and more examples in the near future.

### Experiencing problems?

Please create a [new issue](https://github.com/chemos-inc/phoenics/issues/new/choose) and describe your problem in detail so we can fix it.

### References

[1] Häse, F., Roch, L. M., Kreisbeck, C., & Aspuru-Guzik, A. [Phoenics: A Bayesian Optimizer for Chemistry.](https://pubs.acs.org/doi/abs/10.1021/acscentsci.8b00307) *ACS Cent. Sci.* **4**.6 (2018): 1134-1145.
