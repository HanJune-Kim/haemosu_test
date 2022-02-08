#!/usr/bin/env python3

class preprocssing:

#initiate variable
	def __init__(self, args, path):
		self._args = args
		self._path = path
	def echo_process(self):
		class1 = 'preprocessing'
		class2 = 'trimming'
		return class1, class2
	
	def cal_depth(self):
		if len(self._path.split(';')) == 1:
			file1 = self.path.split(';')[0]
			file2 = self.path.split(';')[1]
		
					


		
	def trimming(self):
		os.system('trimmomatic ')

	def decontamination(self):
		os.system('bowtie2 ')
	




