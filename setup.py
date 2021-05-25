''' Phoenics

'''

import numpy as np

from setuptools import setup
from distutils.extension import Extension

#===============================================================================

def readme():
    with open('README.md', encoding="utf-8") as content:
        return content.read()

#===============================================================================

try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass    = {}
ext_modules = []

if use_cython:
    ext_modules += [
        Extension('phoenics.BayesianNetwork.kernel_evaluations', ['src/phoenics/BayesianNetwork/kernel_evaluations.pyx']),
    ]
    cmdclass.update({'build_ext': build_ext})
else:
    ext_modules += [
        Extension('phoenics.BayesianNetwork.kernel_evaluations', ['src/phoenics/BayesianNetwork/kernel_evaluations.c']),
    ]

#===============================================================================

setup(
    name             = 'phoenics',
    version          = '0.1.2',
    description      = 'Phoenics: A deep Bayesian optimizer',
    long_description = readme(),
	long_description_content_type = 'text/markdown',
    classifiers      = [
        'Intended Audience :: Science/Research',
		'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
    url              = 'https://github.com/Atinary-technologies/phoenics',
    author           = 'Atinary Technologies Inc. & Atinary Technologies Sarl',
    license          = 'Apache license, version 2',
    packages         = [
		'phoenics',
		'phoenics/Acquisition',
		'phoenics/Acquisition/NumpyOptimizers',
		'phoenics/BayesianNetwork',
		'phoenics/BayesianNetwork/EdwardInterface',
		'phoenics/BayesianNetwork/TfprobInterface',
        'phoenics/DatabaseHandler',
        'phoenics/DatabaseHandler/JsonWriters',
        'phoenics/DatabaseHandler/PandasWriters',
        'phoenics/DatabaseHandler/PickleWriters',
        'phoenics/DatabaseHandler/SqliteInterface',
		'phoenics/ObservationProcessor',
		'phoenics/RandomSampler',
		'phoenics/SampleSelector',
		'phoenics/utilities',
	],
    package_dir      = {'': 'src'},
    cmdclass         = cmdclass,
    ext_modules      = ext_modules,
    include_dirs     = np.get_include(),
    zip_safe         = False,
    tests_require    = ['pytest'],
    install_requires = [
        "Cython==0.29.22",
        "edward2 @ git+https://github.com/google/edward2.git@a06c3abd8ec9aa4928aad6ae336e7c0324edcbc7",
        "matplotlib==3.4.1",
        "numpy==1.19.2",
        "pandas==1.2.3",
        "seaborn==0.11.1",
        "SQLAlchemy==1.4.6",
        "tensorflow==2.4.0",
        "tensorflow-probability==0.11.0"
    ],
    python_requires  = '>=3.6',
)
