# Phoenics


Phoenics is an open source optimization algorithm combining ideas from Bayesian optimization with Bayesian Kernel Density estimation [1]. It performs global optimization on expensive to evaluate objectives, such as physical experiments or demanding computations. Phoenics supports sequential and batch optimizations and allows for the simultaneous optimization of multiple objectives via the Chimera scalarizing function [2].

Check out the `examples` folder for detailed descriptions and code examples for:

| Example | Link | 
|:--------|:-----|
| Sequential optimization           |  [examples/optimization_sequential](https://github.com/chemos-inc/phoenics/tree/master/examples/optimization_sequential)  |



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

[2] Häse, F., Roch, L. M., & Aspuru-Guzik, A. [Chimera: enabling hierarchy based multi-objective optimization for self-driving laboratories.](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c8sc02239a) Chemical Science (2018).
