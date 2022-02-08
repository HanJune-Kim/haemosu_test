#!/usr/bin/env python3
import sys
import pandas as pd
from proj_manager import proj_manager
class modules:
	def __init__(self, args):
		self.args = args
		self.manifest = pd.read_csv(self.args['input'], sep ='\t')
#Trimming modules
	
	def trimming(self, path):
		_p_manager = proj_manager(self.args)
		_manifest_val = _p_manager.validate_input(self.manifest)
		_path = (lambda x : x if x.endswith('/') else x+'/')(path)
		os.system('mkdir '+_path+'HuMMUS_trimming/')
		print('trimmomatic '
			+self.args['read-type']
	
	+' '+_path+'HuMMUS_trimming/p')

#Decontamination module
	
	def decontamination(self):
		print('bowtie '
			)

#Taxonomic classification modules
	
	def kraken2(self):
		print('kraken2 '
			)
	def bracken(self):
		print('bracken '
			)
#genefamily, protein ortholog classification module
	
	def diamond2(self):
		print('kraken2 '
			)

#Bias correction module

	def corr_bias(self):
		print('bias correction '
			)


#print help message with no argument
	

class structure_modules:
	
	def print_help(parser, argv_len, argv_pos, argv_loc, argv_val):
		if len(sys.argv) == argv_len and sys.argv[argv_pos].split('/')[argv_loc] == argv_val:
			parser.print_help()
		
