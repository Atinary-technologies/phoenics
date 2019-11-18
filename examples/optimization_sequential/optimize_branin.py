#!/usr/bin/env python 

'''
Licensed to the Apache Software Foundation (ASF) under one or more 
contributor license agreements. See the NOTICE file distributed with this 
work for additional information regarding copyright ownership. The ASF 
licenses this file to you under the Apache License, Version 2.0 (the 
"License"); you may not use this file except in compliance with the 
License. You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
License for the specific language governing permissions and limitations 
under the License.

The code in this file was developed at Harvard University (2018) and 
modified at ChemOS Inc. (2019) as stated in the NOTICE file.
'''

__author__  = 'Florian Hase'

#=========================================================================

import sys 
sys.path.append('../../phoenics')
import pickle

from phoenics import Phoenics 
from branin   import branin as loss

#=========================================================================

class OptimizationManager(object):

	def __init__(self, config_file, loss_function):

		# creates instance of Phoenics optimizer
		self.phoenics      = Phoenics(config_file)
		self.loss_function = loss_function 


	def optimize(self, max_iter = 10):

		observations = []

		for num_iter in range(max_iter):

			# query for new parameters based on prior observations
			params = self.phoenics.recommend(observations = observations)

			# use parameters for evaluation ...
			# ... experimentally or computationally
			for param in params:
				observation = self.loss_function(param)
				observations.append(observation)

			# log observations in a pickle file for future analysis
			pickle.dump(observations, open('observations.pkl', 'wb'))

			# print observations to file 
			logfile = open('logfile.dat', 'a')
			for param in params:
				new_line = ''
				for param_name in sorted(self.phoenics.config.param_names):
					for param_value in param[param_name]:
						new_line += '%.5e\t' % (param[param_name])
				for obj_name in sorted(self.phoenics.config.obj_names):
					new_line += '%.5e\t' % (param[obj_name])
				logfile.write(new_line + '\n')
			logfile.close()

#=========================================================================

if __name__ == '__main__':

	logfile = open('logfile.dat', 'w')
	logfile.close()

	manager = OptimizationManager('config.json', loss)
	manager.optimize()
