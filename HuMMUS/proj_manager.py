#!/usr/bin/env python3

import os, sys
import pandas as pd
#project manager for auto-mode
class proj_manager:
	def __init__(self, args):
		self.args = args	

	def list_modules(self):
		_list_modules = ['trimming', 'decontamination', 'kraken2', 'alpha', 'beta', 'mannwhitneyu', 'ancombc', 'songbird', 'log_regression', 'randomforest']
		return _list_modules

	def validate_input(self):
		_dict_to_return = {}
		_manifest = pd.read_csv(self.args['input'], sep ='\t')
		_class = list(filter(lambda x : (x.startswith('class')), _manifest.columns.tolist()))
		_single = list(filter(lambda x : (x.startswith('single')), _manifest.columns.tolist()))
		_forward = list(filter(lambda x : (x.startswith('forward')), _manifest.columns.tolist()))
		_reverse = list(filter(lambda x : (x.startswith('reverse')), _manifest.columns.tolist()))
		
		#check class prerequisite
		_list_class_validation = ['auto-mode', 'alpha', 'beta', 'mannwhitneyu', 'ancombc', 'songbird', 'log_regression', 'randomforest']
		if self.args['module'] in _list_class_validation:
			print('HuMMUS {} is running'.format(args['module']))
			print('chekcing for class prerequisite...')
			assert len(_class) > 0, 'At least one class must be submitted, detected None'
			print('{} class detected'.format(len(_class)))
			_class_validated = list(filter(lambda x : len(set(_manifest[x].tolist())) > 1, _class))
			_class_removed = list(filter(lambda x : len(set(_manifest[x].tolist())) <= 1, _class))
			assert len(_class_validated) > 0, 'Class must contain at leat two groups, detected one groups'
			print('{} class validated as containing at least two groups, will be used for further analysis'.format(_class_validated))
			_manifest_validated = _manifest.drop(columns = _class_removed)
		#check sample path prerequisite
		assert len(_single+_forward+_reverse) > 0, 'Sample path must be submitted, single or, forward and reverse'
		if len(_single) == 0:
			assert len(_forward+_reverse) == 2, 'both forward and reverse sample path must be submitted'
			assert len(_manifest[_forward[0]]) == len(_manifest[_reverse[0]]), 'number of path fo forward and reverse samples are not conincide'
			print('Paired read sample detected, path to both forward and reverse samples validated')
		elif len(_single) >=1 :
			assert len(_forward + _reverse) == 0, 'Only one type of reads must be submitted, both single and paired samples detected'
			print('Single read sample detected, path to the samples validated')
		return	_manifest_validated
		
	
	def write_syslog(self, list_agrs, out_path):
		_list_args = list_args
		_out_path = out_path
		
		
	

	def manage_folder(self):
		_out_path = (lambda x : x if x.endswith('/') else x+'/')(a)
		os.system('mkdir '+self.args['name'])
			
