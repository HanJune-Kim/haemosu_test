import os

class ArgumentGenerator:
    def __init__(self, metapara_dict, tablecol_dict, project_dict, dict_idx, sample_list, process):

        #########MetaParameters##########
        self.SType = "paired" if metapara_dict["M_Paired"] == True else "single"
        self.SOrigin  = "human" if metapara_dict["M_Human"] == True else "mouse"
        self.SPlatform = "illumina" if metapara_dict["M_Illumina"] == True else "others"
        self.MThreads = metapara_dict["M_Threads"]

        ###########Meta Table parameters############
        self.SampleTitleCol = tablecol_dict["SampleTitle"]
        self.Class1 = tablecol_dict["Class1"]
        self.SClass1 = tablecol_dict["SClass1"]
        self.MetaTablePath = tablecol_dict["MetaTablePath"]

        ############Project Dir paramters###############
        self.SampleDir = project_dict["SampleDir"]
        #self.SampleTitles = project_dict["SampleTitles"]
        self.SampleIdx1 = project_dict["SampleIdx1"]
        self.SampleIdx2 = project_dict["SampleIdx2"]
        self.HuMMUSDir = project_dict["HuMMUSDir"]
        self.ProjectDir = "/".join([project_dict["ProjectDir"], project_dict["ProjectTitle"]])
        self.PipelineTitle = project_dict["PipelineTitle"]
        self.sample_list = sample_list
        self.Process = [process] if type(process) != list else process
        self.ProcessType = "Main" if type(process) != list else "Sub"
        self.AvailableMem = project_dict["AvailableMemory"]

        self.dict_idx = dict_idx
        self.DirectoryManagement()

    def GenerateArguments(self):
        ProcessArguments = []
        Executor_name = ["HuMMUS_Argument_Execute.py"]

        for process in self.Process:
            self.tool_name = process
            if self.ProcessType == "Main":
                self.tool_dict = self.dict_idx[process]

                print(process)
                print(self.tool_dict)

            if process == "Trimmomatic":

                for sample in self.sample_list:
                    if self.SType == "paired":
                        self.SampleTitle = sample[0][self.SampleIdx1:self.SampleIdx2]
                        self.SampleFileName = sample
                    else:
                        self.SampleTitle = sample[self.SampleIdx1:self.SampleIdx2]
                        self.SampleFileName = sample

                    ProcessArguments.append(Executor_name + self.TrimmomaticArguments())

            elif process == "Trimmomatic Summary":
                ProcessArguments.append(Executor_name + self.TrimmomaticSubArguments(process))

            elif process == "Bowtie2":

                if self.SType == "paired":
                    validationpath = self.trimmomatic_psurvival_path
                else:
                    validationpath = self.trimmomatic_single_output_path

                if not os.path.isdir(validationpath):
                    self.bowtie_sample_list = self.sample_list
                    self.bowtie_sample_path = self.SampleDir
                    for sample in self.bowtie_sample_list:
                        if self.SType == "paired":
                            self.SampleTitle = sample[0][self.SampleIdx1:self.SampleIdx2]
                            self.SampleFileName = sample
                        else:
                            self.SampleTitle = sample[self.SampleIdx1:self.SampleIdx2]
                            self.SampleFileName = sample


                        ProcessArguments.append(Executor_name + self.Bowtie2Arguments(self.bowtie_sample_path))

                elif os.path.isdir(validationpath):
                    self.bowtie_sample_path, self.bowtie_sample_list = self.get_valid_samplelist(validationpath)
                    for sample in self.bowtie_sample_list:
                        print(sample)
                        if self.SType == "paired":
                            self.SampleTitle = sample[0].split("ps_")[1][self.SampleIdx1:self.SampleIdx2]
                            self.SampleFileName = sample
                        else:
                            self.SampleTitle = sample.split("single_")[1][self.SampleIdx1:self.SampleIdx2]
                            self.SampleFileName = sample

                        ProcessArguments.append(Executor_name + self.Bowtie2Arguments(self.bowtie_sample_path))

            elif process == "Bowtie2 Summary":
                self.tool_dict = self.dict_idx["Bowtie2"]
                ProcessArguments.append(Executor_name + self.Bowtie2SubArguments(process))

            elif process == "Kraken2":
                if self.SType == "paired":
                    validationpath = self.trimmomatic_psurvival_path
                else:
                    validationpath = self.trimmomatic_single_output_path

                if not os.path.isdir(self.bowtie2_filtered_path):
                    if not os.path.isdir(validationpath):
                        self.kraken2_sample_list = self.sample_list
                        self.kraken2_sample_path = self.SampleDir

                        for sample in self.kraken2_sample_list:
                            if self.SType == "paired":
                                self.SampleTitle = sample[0][self.SampleIdx1:self.SampleIdx2]
                                self.SampleFileName = sample
                            else:
                                self.SampleTitle = sample[self.SampleIdx1:self.SampleIdx2]
                                self.SampleFileName = sample

                            ProcessArguments.append(Executor_name + self.Kraken2Arguments(self.kraken2_sample_path))

                    elif os.path.isdir(validationpath):
                        self.kraken2_sample_path, self.kraken2_sample_list = self.get_valid_samplelist(self.trimmomatic_psurvival_path)
                        for sample in self.kraken2_sample_list:
                            if self.SType == "paired":
                                self.SampleTitle = sample[0].split("ps_")[1][self.SampleIdx1:self.SampleIdx2]
                                self.SampleFileName = sample
                            else:
                                self.SampleTitle = sample.split("single_")[self.SampleIdx1:self.SampleIdx2]
                                self.SampleFileName = sample

                            ProcessArguments.append(Executor_name + self.Kraken2Arguments(self.kraken2_sample_path))

                elif os.path.isdir(self.bowtie2_filtered_path):
                    bowtie_exclusion_path = "/".join([self.bowtie2_path, "Bowtie2Excluded.txt"])
                    excluded_list =[]
                    if os.path.isfile(bowtie_exclusion_path):
                        excluded_list = [i.strip() for i in open(bowtie_exclusion_path, "r")]
                    self.kraken2_sample_path, self.kraken2_sample_list = self.get_valid_samplelist(self.bowtie2_filtered_path, excluded_list)

                    for sample in self.kraken2_sample_list:
                        if self.SType == "paired":
                            self.SampleTitle = sample[0].split("unconc_")[1].split(".")[0]
                            self.SampleFileName = sample
                        else:
                            self.SampleTitle = sample.split("un_")[1]
                            self.SampleFileName = sample

                        ProcessArguments.append(Executor_name + self.Kraken2Arguments(self.kraken2_sample_path))

            elif process == "Kraken2 Taxonomic Table":
                ProcessArguments.append(Executor_name + self.Kraken2SubArguments(process))

            elif process == "Taxonomic_Alpha":
                ProcessArguments.append(Executor_name + self.Kraken2SubArguments(process))
            elif process == "Diamond":
                if self.SType == "paired":
                    validationpath = self.trimmomatic_psurvival_path
                else:
                    validationpath = self.trimmomatic_single_output_path

                if not os.path.isdir(self.bowtie2_filtered_path):
                    if not os.path.isdir(validationpath):
                        self.diamond_sample_list = self.sample_list
                        self.diamond_sample_path = self.SampleDir

                        for sample in self.diamond_sample_list:
                            if self.SType == "paired":
                                self.SampleTitle = sample[0][self.SampleIdx1:self.SampleIdx2]
                                self.SampleFileName = sample
                            else:
                                self.SampleTitle = sample[self.SampleIdx1:self.SampleIdx2]
                                self.SampleFileName = sample

                            ProcessArguments.append(Executor_name + self.DiamondArguments(self.diamond_sample_path))

                    elif os.path.isdir(validationpath):
                        self.diamond_sample_path, self.diamond_sample_list = self.get_valid_samplelist(self.trimmomatic_psurvival_path)

                        for sample in self.diamond_sample_list:
                            if self.SType == "paired":
                                self.SampleTitle = sample[0].split("ps_")[1][self.SampleIdx1:self.SampleIdx2]
                                self.SampleFileName = sample
                            else:
                                self.SampleTitle = sample.split("single_")[self.SampleIdx1:self.SampleIdx2]
                                self.SampleFileName = sample

                            ProcessArguments.append(Executor_name + self.DiamondArguments(self.diamond_sample_path))

                elif os.path.isdir(self.bowtie2_filtered_path):
                    bowtie_exclusion_path = "/".join([self.bowtie2_path, "Bowtie2Excluded.txt"])
                    excluded_list =[]
                    if os.path.isfile(bowtie_exclusion_path):
                        excluded_list = [i.strip() for i in open(bowtie_exclusion_path, "r")]
                    self.diamond_sample_path, self.diamond_sample_list = self.get_valid_samplelist(self.bowtie2_filtered_path, excluded_list)

                    for sample in self.diamond_sample_list:
                        if self.SType == "paired":
                            self.SampleTitle = sample[0].split("unconc_")[1].split(".")[0]
                            self.SampleFileName = sample
                        else:
                            self.SampleTitle = sample.split("un_")[1]
                            self.SampleFileName = sample

                        ProcessArguments.append(Executor_name + self.DiamondArguments(self.diamond_sample_path))

            elif process == "Random Forest":

                for sample in self.sample_list:
                    if self.SType == "paired":
                        self.SampleTitle = sample[0][self.SampleIdx1:self.SampleIdx2]
                        self.SampleFileName = sample
                    else:
                        self.SampleTitle = sample[self.SampleIdx1:self.SampleIdx2]
                        self.SampleFileName = sample
                    ProcessArguments.append(Executor_name + self.RandomForestArguments())

        '''with open(self.project_tmp_Main_path, "w") as f:
            for line in MainProcessArgumentList:
                f.write(";".join(line)+"\n")

            f.close()
        with open(self.project_tmp_Sub_path, "w") as f:
            for k, v in SubProcessArgumentDict.items():
                f.write("|".join([k, ";".join(v[0])])+"\n")
            f.close()'''

        return ProcessArguments

    def DirectoryManagement(self):
        self.trimmomatic_path = "/".join([self.ProjectDir, "Preprocessing", "Trimmomatic", self.PipelineTitle])
        self.trimmomatic_logs_path = "/".join([self.trimmomatic_path, "Logs"])
        self.trimmomatic_summary_path = "/".join([self.trimmomatic_path, "Summary"])
        self.trimmomatic_psurvival_path = "/".join([self.trimmomatic_path, "p_Survival"])
        self.trimmomatic_ssurvival_path = "/".join([self.trimmomatic_path, "s_Survival"])
        self.trimmomatic_single_output_path = "/".join([self.trimmomatic_path, "Single_Output"])
        self.trimmomatic_ref_adaptor_path = "/".join([self.HuMMUSDir, "HuMMUS_DB", "Preprocessing", "Trimmomatic"])
        self.trimmomatic_output_analysis_path = "/".join([self.trimmomatic_path, "Output_Analysis", "FastQC"])
        self.trimmomatic_output_fastqc_raw_path = "/".join([self.trimmomatic_output_analysis_path, "Raw_Samples"])
        self.trimmomatic_output_fastqc_trim_path = "/".join([self.trimmomatic_output_analysis_path, "Trimmed_Samples"])

        self.bowtie2_path = "/".join([self.ProjectDir, "Preprocessing", "Bowtie2", self.PipelineTitle])
        self.bowtie2_contaminant_path = "/".join([self.bowtie2_path, "Contaminant"])
        self.bowtie2_filtered_path = "/".join([self.bowtie2_path, "Filtered"])
        self.bowtie2_aligned_sam_path = "/".join([self.bowtie2_path, "Human-aligned_SAM"])
        self.bowtie2_output_analysis_path = "/".join([self.bowtie2_path, "Output_Analysis"])
        self.bowtie2_ref_index_path = "/".join([self.HuMMUSDir, "HuMMUS_DB", "Preprocessing", "Bowtie2"])

        self.kraken2_path = "/".join([self.ProjectDir, "Classification", "Kraken2", self.PipelineTitle])
        self.kraken2_output_kraken_path = "/".join([self.kraken2_path, "Output_Kraken"])
        self.kraken2_output_report_path = "/".join([self.kraken2_path, "Output_Report"])
        self.kraken2_outout_classified = "/".join([self.kraken2_path, "Output_Classified_Seq."])
        self.kraken2_output_unclassified= "/".join([self.kraken2_path, "Output_Unclassified_Seq."])
        self.Kraken2_bracken_path = "/".join([self.kraken2_path, "Output Bracken"])
        self.Kraken2_output_table_path = "/".join([self.kraken2_path, "Output_Tables"])
        self.Kraken2_ref_db_path = "/".join([self.HuMMUSDir, "HuMMUS_DB", "Classification", "Kraken2"])

        self.diamond_path = "/".join([self.ProjectDir, "Classification", "Diamond", self.PipelineTitle])
        self.diamond_output_path = "/".join([self.diamond_path, "Output_Diamond"])
        self.diamond_output_aligned = "/".join([self.diamond_path, "Output_Aligned_Seq."])
        self.diamond_output_unaligned = "/".join([self.diamond_path, "Output_Unaligned_Seq."])
        self.diamond_output_table_path = "/".join([self.diamond_path, "Output_Tables"])
        self.diamond_ref_db_path = "/".join([self.HuMMUSDir, "HuMMUS_DB", "Classification", "Diamond"])
        self.diamond_concat_sample_path = "/".join([self.diamond_path, "Concatenate_Samples"])

        self.alpha_path = "/".join([self.ProjectDir, "Statistical_Analysis", "Alpha", self.PipelineTitle])
        self.alpha_taxonomic_path = "/".join([self.alpha_path, "Taxonomy"])
        self.alpha_genefamily_path = "/".join([self.alpha_path, "GeneFamily"])
        self.alpha_pathway_path = "/".join([self.alpha_path, "Pathway"])

        self.beta_path = "/".join([self.ProjectDir, "Statistical_Analysis", "Beta", self.PipelineTitle])
        self.beta_taxonomic_path = "/".join([self.beta_path, "Taxonomy"])
        self.beta_genefamily_path = "/".join([self.beta_path, "GeneFamily"])
        self.beta_pathway_path = "/".join([self.beta_path, "Pathway"])

        self.mwut_path = "/".join([self.ProjectDir, "Statistical_Analysis", "Mann-Whitney_U_Test", self.PipelineTitle])
        self.mwut_output_path = "/".join([self.mwut_path, "Output_MWUT"])

        self.lefse_path = "/".join([self.ProjectDir, "Statistical_Analysis", "LEfSe", self.PipelineTitle])
        self.lefse_output_path = "/".join([self.lefse_path, "Output_LEfSe"])

        self.ancombc_path = "/".join([self.ProjectDir, "Statistical_Analysis", "ANCOMBC", self.PipelineTitle])
        self.ancombc_output_path = "/".join([self.ancombc_path, "Output_ANCOMBC"])

        self.songbird_path = "/".join([self.ProjectDir, "Statistical_Analysis", "SongBird", self.PipelineTitle])
        self.songbird_output_path = "/".join([self.songbird_path, "Output_SongBird"])

        self.randomforest_path = "/".join([self.ProjectDir, "Modeling", "Random_Forest", self.PipelineTitle])
        self.randomforest_output_path = "/".join([self.randomforest_path, "Output_Random_Forest"])

        self.project_tmp_file_path = "/".join([self.ProjectDir, ".pipeline_tmp", self.PipelineTitle])
        self.project_tmp_Main_path = "/".join([self.project_tmp_file_path, "".join([".", "Main_{}".format(self.PipelineTitle)])])
        self.project_tmp_Sub_path = "/".join([self.project_tmp_file_path, "".join([".", "Sub_{}".format(self.PipelineTitle)])])

        os.makedirs(self.project_tmp_file_path, exist_ok=True)
    def TrimmomaticArguments(self):

        ################setting parameters#################
        trim_threads = self.tool_dict["Trim_Threads"] if self.MThreads != self.tool_dict["Trim_Threads"] else self.MThreads
        trim_phred = self.tool_dict["Trim_Phred"].lower()
        trim_summary = self.tool_dict["Trim_Summary"]
        trim_leading = self.tool_dict["Trim_Leading"]
        trim_trailing = self.tool_dict["Trim_Trailing"]
        trim_minlen = self.tool_dict["Trim_Minlen"]
        trim_wsliding = self.tool_dict["Trim_Sliding"]


        ################create directory#################
        os.makedirs(self.trimmomatic_logs_path, exist_ok=True)
        os.makedirs(self.trimmomatic_summary_path, exist_ok=True) if trim_summary else None
        if self.SType == "paired":
            os.makedirs(self.trimmomatic_psurvival_path, exist_ok=True)
            os.makedirs(self.trimmomatic_ssurvival_path, exist_ok=True)
        else:
            os.makedirs(self.trimmomatic_single_output_path, exist_ok=True)

        ################setting argument#################
        if self.SType == "paired":
            trimmomatic_refadaptor = "/".join([self.trimmomatic_ref_adaptor_path, "PE_Trimmomatic_seq.fa"])
        else:
            trimmomatic_refadaptor = "/".join([self.trimmomatic_ref_adaptor_path, "SE_Trimmomatic_seq.fa"])


        argument_1 = "PE" if self.SType == "paired" else "SE"
        argument_2 = " ".join(["-threads", str(trim_threads)])
        argument_3 = "-".join(["", trim_phred])
        argument_4 = " ".join(["-trimlog", "/".join([self.trimmomatic_logs_path, "log_{}".format(self.SampleTitle)])])
        argument_5 = ":".join(["ILLUMINACLIP", trimmomatic_refadaptor, "2:30:7"])
        argument_6 = ":".join(["LEADING", str(trim_leading)])
        argument_7 = ":".join(["TRAILING", str(trim_trailing)])
        argument_8 = ":".join(["SLIDINGWINDOW", str(trim_wsliding)])
        argument_9 = ":".join(["MINLEN", str(trim_minlen)])


        if self.SType == "paired":
            argument_10 = "/".join([self.SampleDir, self.SampleFileName[0]])
            argument_11 = "/".join([self.SampleDir, self.SampleFileName[1]])
            argument_12 = "/".join([self.trimmomatic_psurvival_path, "ps_{}".format(self.SampleFileName[0])])
            argument_13 = "/".join([self.trimmomatic_ssurvival_path, "ss_{}".format(self.SampleFileName[0])])
            argument_14 = "/".join([self.trimmomatic_psurvival_path, "ps_{}".format(self.SampleFileName[1])])
            argument_15 = "/".join([self.trimmomatic_ssurvival_path, "ss_{}".format(self.SampleFileName[1])])
            argument_sampletitle = ", ".join(self.SampleFileName)
            arguments_list = [self.tool_name, argument_sampletitle, argument_1, argument_2, argument_3, argument_10, argument_11,
                              argument_12, argument_13, argument_14, argument_15,
                              argument_5, argument_6, argument_7, argument_8, argument_9,
                              argument_4]
            if trim_summary:
                argument_16 = " ".join(["-summary", "/".join([self.trimmomatic_summary_path, "summary_{}".format(self.SampleTitle)])])
                arguments_list.append(argument_16)


        else:
            argument_10 = "/".join([self.SampleDir, self.SampleFileName])
            argument_11 = "/".join([self.trimmomatic_single_output_path, "single_{}".format(self.SampleFileName)])
            arguments_list = [self.tool_name, self.SampleFileName, argument_1, argument_2, argument_3, argument_10, argument_11,
                              argument_5, argument_6, argument_7, argument_8,
                              argument_9, argument_4]
            if trim_summary:
                argument_13 = " ".join(["-summary", "/".join([self.trimmomatic_summary_path, "summary_{}".format(self.SampleTitle)])])
                arguments_list.append(argument_13)

        return arguments_list

    def Bowtie2Arguments(self, bowtiesamplepath):

        ################setting parameters#################
        bowthreads = self.tool_dict["Bow_Threads"] if self.tool_dict["Bow_Threads"] != self.MThreads else self.MThreads
        bowphred = self.tool_dict["Bow_Phred"].lower()
        bowsensitivity = "".join(["--", "-".join(self.tool_dict["Bow_Sensi"].lower().split(" "))])
        bowsamreorder = self.tool_dict["Bow_ROSAM"]
        bowtiesamplepath = bowtiesamplepath

        ################create directory#################
        os.makedirs(self.bowtie2_path, exist_ok=True)
        os.makedirs(self.bowtie2_contaminant_path, exist_ok=True)
        os.makedirs(self.bowtie2_filtered_path, exist_ok=True)
        os.makedirs(self.bowtie2_aligned_sam_path, exist_ok=True)
        os.makedirs(self.bowtie2_output_analysis_path, exist_ok=True)

        ################setting argument#################
        if self.SOrigin == "human":
            bowtierefdb = "/".join([self.bowtie2_ref_index_path, "Human", "grch38_1kgmaj"])
        else:
            bowtierefdb = "/".join([self.bowtie2_ref_index_path, "Mouse", "grch38_1kgmaj"])


        argument1 = " ".join(["-p", str(bowthreads)])
        argument2 = bowsensitivity
        argument5 = " ".join(["-x", bowtierefdb])
        argument6 = "".join(["--", bowphred])


        if self.SType == "paired":
            argument3 = " ".join(["--un-conc", "/".join([self.bowtie2_filtered_path, "unconc_{}".format(self.SampleTitle)])])
            argument4 = " ".join(["--al-conc", "/".join([self.bowtie2_contaminant_path, "alconc_{}".format(self.SampleTitle)])])
            argument7= " ".join(["-1", "/".join([bowtiesamplepath, self.SampleFileName[0]])])
            argument8 = " ".join(["-2", "/".join([bowtiesamplepath, self.SampleFileName[1]])])
            arguments = [argument1, argument2, argument3, argument4, argument5, argument6, argument7, argument8]
            argument9 = " ".join(["-S", "/".join([self.bowtie2_aligned_sam_path, "SAM_{}".format(self.SampleTitle)])])
            arguments = arguments + [argument9]
            if bowsamreorder:
                argument10 = "--reorder"
                arguments = arguments + [argument10]
            argumentFileName = ", ".join(name for name in self.SampleFileName)
            arguments = [self.tool_name, self.SampleTitle] + arguments
            return arguments

        else:

            argument3 = " ".join(["--un", "/".join([self.bowtie2_filtered_path, "un_{}".format(self.SampleTitle)])])
            argument4 = " ".join(["--al", "/".join([self.bowtie2_contaminant_path, "al_{}".format(self.SampleTitle)])])
            argument7 = " ".join(["-U", "/".join([bowtiesamplepath, self.SampleFileName])])
            arguments = [argument1, argument2, argument3, argument4, argument5, argument6, argument7]
            argument8 = " ".join(["-S", "/".join([self.bowtie2_aligned_sam_path, "SAM_{}".format(self.SampleTitle)])])
            arguments = arguments + [argument8]
            if bowsamreorder:
                argument9 = "--reorder"
                arguments = arguments + [argument9]
            arguments = [self.tool_name, self.SampleTitle] + arguments

            return arguments



    def Kraken2Arguments(self, krakensamplepath):

        ################setting parameters#################
        krakensamplepath = krakensamplepath
        kraken_threads = str(self.tool_dict["Kra_Threads"])
        kraken_unclass = self.tool_dict["Kra_Uncla"]
        kraken_class = self.tool_dict["Kra_Cla"]
        kraken_confidence = str(self.tool_dict["Kra_Confi"])
        if self.SOrigin == "human":
            kraken_refdb = "/".join([self.Kraken2_ref_db_path, "Human"])
        else:
            kraken_refdb = "/".join([self.Kraken2_ref_db_path, "Mouse"])


        ################create directory###################

        os.makedirs(self.kraken2_path, exist_ok=True)
        os.makedirs(self.kraken2_output_kraken_path, exist_ok=True)
        os.makedirs(self.kraken2_output_report_path, exist_ok=True)
        if kraken_unclass:
            os.makedirs(self.kraken2_output_unclassified, exist_ok=True)
        if kraken_class:
            os.makedirs(self.kraken2_outout_classified, exist_ok=True)


        ################setting argument###################

        argument1 = " ".join(["--threads", kraken_threads])
        argument2 = "--use-names"
        argument3 = "--report-zero-counts"
        argument4 = " ".join(["--confidence", kraken_confidence])
        argument5 = " ".join(["--db", kraken_refdb])
        argument6 = " ".join(["--output", "/".join([self.kraken2_output_kraken_path, "kraken_{}".format(self.SampleTitle)])])
        argument7 = " ".join(["--report", "/".join([self.kraken2_output_report_path, "report_{}".format(self.SampleTitle)])])
        if self.SType == "paired":
            argument_sampletitle = ", ".join(self.SampleFileName)
            argument8 = " ".join(["--paired", "/".join([krakensamplepath, self.SampleFileName[0]]), "/".join([krakensamplepath, self.SampleFileName[1]])])
        else:
            argument_sampletitle = self.SampleFileName
            argument8 = "/".join([krakensamplepath, self.SampleFileName])

        arguments = [self.tool_name, argument_sampletitle, argument1, argument2, argument3, argument4, argument5,
                     argument6, argument7, argument8]

        return arguments

    def DiamondArguments(self, diamondsamplepath):

        ################setting parameters#################
        diamondsamplepath = diamondsamplepath
        dia_threads = str(self.tool_dict["Dia_Threads"])
        dia_sensitivity = "".join(["--",  "-".join(self.tool_dict["Dia_Sensi"].lower().split(" "))])
        dia_minidentity = str(self.tool_dict["Dia_MinId"])
        dia_querycover = str(self.tool_dict["Dia_QCover"])
        dia_evalue = self.tool_dict["Dia_Eval"]
        dia_verbose = self.tool_dict["Dia_Verbose"]
        dia_aligned = self.tool_dict["Dia_Aligned"]
        dia_unaligned = self.tool_dict["Dia_Unaligned"]

        if self.SOrigin == "human":
            dia_refdb = "/".join([self.diamond_ref_db_path, "Human", "HRGM50.dmnd"])
        else:
            dia_refdb = "/".join([self.diamond_ref_db_path, "Mouse", "MRGM50.dmnd"])

        ################create directory###################
        os.makedirs(self.diamond_path, exist_ok=True)
        os.makedirs(self.diamond_output_path, exist_ok=True)
        if dia_aligned:
            os.makedirs(self.diamond_output_aligned, exist_ok=True)
        if dia_unaligned:
            os.makedirs(self.diamond_output_unaligned, exist_ok=True)
        os.makedirs(self.diamond_concat_sample_path, exist_ok=True)


        ################setting argument###################

        argument1 = "blastx"
        argument2 = " ".join(["--threads", dia_threads])
        argument3 = " ".join(["--db", dia_refdb])
        argument4 = " ".join(["--out", "/".join([self.diamond_output_path, "diamond_{}".format(self.SampleTitle)])])
        argument5 = dia_sensitivity
        argument6 = " ".join(["--query-cover", dia_querycover])
        argument7 = " ".join(["--id", dia_minidentity])
        argument8 = " ".join(["--evalue", dia_evalue])
        argument_mem = " ".join(["--memory-limit", str(self.AvailableMem * 0.90)])


        if self.SType == "paired":
            argument_sampletitle = ", ".join(self.SampleFileName)
            argument9 = " ".join(["--query", "/".join([self.diamond_concat_sample_path, "Concat_{}".format(self.SampleTitle)])])
        else:
            argument_sampletitle = self.SampleFileName
            argument9 = " ".join(["--query", "/".join([diamondsamplepath, self.SampleFileName])])

        arguments = [self.tool_name, argument_sampletitle, diamondsamplepath, self.diamond_concat_sample_path,
                     self.SType, self.SampleTitle, self.bowtie2_path, argument1, argument2, argument3, argument4, argument5, argument6,
                     argument7, argument8, argument9, argument_mem]

        if dia_aligned:
            argument10 = " ".join(["--al", "/".join([self.diamond_output_aligned, "al_{}".format(self.SampleTitle)])])
            arguments.append(argument10)
        if dia_unaligned:
            argument11 = " ".join(["--un", "/".join([self.diamond_output_unaligned, "unal_{}".format(self.SampleTitle)])])
            arguments.append(argument11)
        if dia_verbose:
            argument12 = "--verbose"
            arguments.append(argument12)

        if self.tool_dict["Dia_Sensi"] in ["Fast", "Sensitive"] and self.tool_dict["Dia_MemControl"] == True:
            argument_blocksize = " ".join(["--block-size", str(round((self.AvailableMem * 0.9) / 6))])

            arguments.append(argument_blocksize)

        return arguments



    def RandomForestArguments(self):
        pass

    #############################Sub Process#############################

    def TrimmomaticSubArguments(self, subprocess):
        if subprocess == "Trimmomatic Summary":
            os.makedirs(self.trimmomatic_output_fastqc_raw_path, exist_ok=True)
            os.makedirs(self.trimmomatic_output_fastqc_trim_path, exist_ok=True)
            argument1 = "Trimmomatic Summary"
            if self.SType == "paired":
                argument2 = self.trimmomatic_psurvival_path
            else:
                argument2 = self.trimmomatic_single_output_path
            argument3 = self.SType
            argument4 = self.SampleDir
            argument5 = self.trimmomatic_output_fastqc_trim_path
            argument6 = self.trimmomatic_output_fastqc_raw_path

            arguments = [argument1, argument2, argument3, argument4, argument5, argument6]
            return arguments

    def Bowtie2SubArguments(self, subprocesslist):
        subprocess = subprocesslist

        if subprocess == "Bowtie2 Summary":
            argument1 = self.SType
            argument2 = "/".join([self.ProjectDir, "Preprocessing", "Bowtie2", self.PipelineTitle, "Bowtie2_Log"])
            argument3 = str(self.tool_dict["Bow_Exclusion"])
            arguments = [subprocess, argument1, argument2, argument3]
            print(arguments)
            return arguments

    def Kraken2SubArguments(self, subprocesslist):
        subprocess = subprocesslist
        if subprocess == "Kraken2 Taxonomic Table":
            os.makedirs(self.Kraken2_output_table_path, exist_ok=True)
            argument1 = subprocess
            argument2 = self.kraken2_output_report_path
            argument3 = self.Kraken2_output_table_path
            argument4 = self.MetaTablePath


            arguments = [argument1, argument2, argument3, argument4]

            return arguments

        elif subprocess == "Taxonomic_Alpha":
            os.makedirs(self.alpha_path, exist_ok=True)
            os.makedirs(self.alpha_taxonomic_path, exist_ok=True)
            argument1 = subprocess
            argument2 = "/".join([self.Kraken2_output_table_path, "TaxonomyNormalizedCountTable.tsv"])
            argument3 = self.alpha_taxonomic_path
            argument4 = self.MetaTablePath
            argument5 = self.Class1
            argument6 = self.SClass1
            arguments = [argument1, argument2, argument3, argument4, argument5, argument6]
            return arguments

        elif subprocess == "Taxonomic_Beta":
            pass
        elif subprocess == "Taxonomic_Mann-Whitney U Test":
            pass
        elif subprocess == "Taxonomic_LEfSe":
            pass
        elif subprocess == "Taxonomic_ANCOMBC":
            pass
        elif subprocess == "Taxonomic_SongBird":
            pass





    def DiamondSubArguments(self, subprocesslist):
        pass
    def RandomForestSubArguments(self, subprocesslist):
        pass

    def get_valid_samplelist(self, validationpath, excluded_list = None):
        Excluded_sample = []
        if excluded_list != None:
            Excluded_sample = excluded_list
        print("Excluded list {}".format(Excluded_sample))
        validationpath = validationpath
        validorderedlist = []

        if self.SType == "paired":
            validsamplelist = os.listdir(validationpath)
            print(validsamplelist)
            if len(validsamplelist) % 2 != 0:
                idx2 = 0
                for sample1 in validsamplelist:
                    sort_list = []
                    if sample1 == validsamplelist[0]:
                        pass
                    else:
                        if len(sample1) == len(validsamplelist[0]):
                            for ln in range(len(sample1)):
                                if sample1[ln] == validsamplelist[0][ln]:
                                    sort_list.append(ln)
                                else:
                                    break
                            if max(sort_list) >= idx2:
                                idx2 = max(sort_list)
                for sample1 in validsamplelist:
                    sorter = []
                    for sample2 in validsamplelist:
                        if sample1 != sample2 and sample1[:idx2] == sample2[:idx2]:
                            if sample1 not in sorter and sample2 not in sorter and sample1 not in Excluded_sample and sample2 not in Excluded_sample:
                                sorter.append(sample1)
                                sorter.append(sample2)
                                sorter.sort()
                                validsample = [sorter[0], sorter[1]]
                                if validsample not in validorderedlist:
                                    validorderedlist.append(validsample)
            elif len(validsamplelist) % 2 == 0:
                validsamplelist.sort()

                for forward, reverse in zip(validsamplelist[::2], validsamplelist[1::2]):
                    sorter = []
                    if forward not in Excluded_sample and reverse not in Excluded_sample:
                        sorter.append(forward)
                        sorter.append(reverse)
                        sorter.sort()
                        if sorter not in validorderedlist:
                            validorderedlist.append(sorter)

            print(validorderedlist)
            return validationpath, validorderedlist

        elif self.SType == "single":
            validsamplelist = os.listdir(validationpath)
            validsamplelist.sort()
            for sample in validsamplelist:
                if sample not in Excluded_sample:
                    validorderedlist.append(sample)

            return validationpath, validorderedlist