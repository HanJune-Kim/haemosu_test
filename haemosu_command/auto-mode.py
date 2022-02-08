#!/usr/bin/env python3

from proj_manager import proj_manager
from modules import modules


def run_automode(args):
	p_manager = proj_manager(args)
	_module_to_run = p_manager
	_detours = args['detour']
	
	_out_path = (lambda x : x if x.endswith('/') else x+'/')(args['output'])
	os.system('mkdir '+_out_path+args['name'])




		

os.system('mkdir '+args

os.system('hummus trimming



