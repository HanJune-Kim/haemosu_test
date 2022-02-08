#!/usr/bin/env python3

class descriptions:
	
	def base():
		return '''




             _   _   ___   _____ ___  ___ _____  _____  _   _ 
            | | | | / _ \ |  ___||  \/  ||  _  |/  ___|| | | |
            | |_| |/ /_\ \| |__  | .  . || | | |\ `--. | | | |
            |  _  ||  _  ||  __| | |\/| || | | | `--. \| | | |
            | | | || | | || |___ | |  | |\ \_/ //\__/ /| |_| |
            \_| |_/\_| |_/\____/ \_|  |_/ \___/ \____/  \___/ 
                                                                                            

     ===================================================================
	        Human Animal Enhanced Microbiome Open Source Utility

  	  HAEMOSU 1.0.0 provided by Bioinformatics Lab. in Yonsei University 	

	  HAEMOSU 1.0.0 supports 2 modes following,
	

	  》auto-mode 
		
	  	Usage : ~$ hummus auto-mode -h or --help

	  》manual-mode 
		
		Usage : ~$ hummus manual-mode -h or --help
 	  
	  	

	  if users want to see all the modules of HuMMUS, check
			~$ hummus -r or -README


			'''

	def auto_mode():
		return '''

			================================

		  	     HAEMOSU auto-mode 1.0.0

			================================

	HAEMOSU auto-mode 1.0.0 enables users to run general pipelines of MWAS, 
	from prep. to differential analyses, possible with a single command line. 
	Only you need to do is to input manifest file.	
	
			'''

	def manual_mode():
		return '''

			=================================

			    HuMMUS manual-mode 1.0.0

			=================================
	
	HuMMUS manual-mode 1.0.0 provides all the separate moduels to run auto-mode.
	Thus, users can analyse data step by step or use a specific module.
	HuMMUS manual-mode 1.0.0 supports separate modules following,		

	Preprocessing 

		trimming		Usage : ~$ hummus trimming -h or --help
		decontamination		Usage : ~$ hummus decontamination -h or --help


	Classification

		kraken2			Usage : ~$ hummus kraken2 -h or --help
		kraken-uniq		Usage : ~$ hummus kraken-uniq -h or --help
		bracken			Usage : ~$ hummus bracken -h or --help
		diamond2		Usage : ~$ hummus diamond2 -h or --help

	Diversity
	
		alpha			Usage : ~$ hummus alpha -h or --help
		beta			Usage : ~$ hummus beta -h or --help
	
	Analyses
		
		mannwhitney U test	Usage : ~$ hummus mannwhitneyu -h or --help
		LefSe			usage : ~$ hummus lefse -h or --help
		ancom-bc		Usage : ~$ hummus ancombc -h or --help
		songbird		Usage : ~$ hummus songbird -h or --help


	Modeling

		Logistic regression	Usage : ~$ huumus log_regression -h or --help
		Random froest		Usage : ~$ hummus randomforest -h or --help
		ANN			Usage : ~$ hummus ann -h or --help
		Deep Learning		Usage : ~$ hummus DL -h or --help

			'''

	
	def trimming():
		return '''

			===================================

			  HuMMUS preprocessing - trimming 

			===================================
	
	This is usage lines for trimming in 
	manual_mode 
	Please fill in the usage lines


			'''

	def decontamination():
		return '''

			========================================

	 		 HuMMUS preprocessing - decontamination 

			========================================
	
	
	This is usage lines for trimming in
	manual_mode
	Please fill in the usage lines

			'''

	def kraken2():
		return '''

			======================================

	 		    HuMMUS classification - kraken2

			======================================
	

	This is usage lines for kraken2 in
	manual_mode
	Please fill in the usage lines

			'''

	def diamond2 ():
		return '''
	
			======================================

	 		   HuMMUS classification - diamond2

			======================================
	
	
	This is usage lines for kraken2 in
	manual_mode
	Please fill in the usage lines

			'''

	def diversities():
		return '''
	
			=====================================

	 		   HuMMUS diversity - diversities

			=====================================
	
	This is usage lines for diversities in
	manual_mode
	Please fill in the usage lines

			'''

	def alpha():
		return '''
	
			=================================

	 		    HuMMUS diversity - alpha

			=================================
	
		

	This is usage lines for alpha in
	manual_mode
	Please fill in the usage lines

			'''

	def beta():
		return '''	
		
			=================================

	 		    HuMMUS diversity - beta

			=================================
		
	This is usage lines for beta in 
	manual-mode
	Please fill in the usage lines
		
			'''

	def mannwhitneyu():
		return '''
	
			===================================

 	 		   HuMMUS analyses - mannwhitneyu

			===================================

	This is usage lines for mannwhitneyu in
	manual-mode
	Please fill in the usage lines	
	
			'''

	def ancombc():
		return '''
	
			================================

 	 		   HuMMUS analyses - ancombc

			================================

	This is usage lines for ancombc in
	manual-mode
	Please fill in the usage lines

			'''

	def songbird():
		return '''
	
			================================

 	 		   HuMMUS analyses - songbird

			================================
	
	This is usage lines for songbird in
	manual-mode
	Please fill in the usage lines

			'''


		
