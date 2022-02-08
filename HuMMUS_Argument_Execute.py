import os, sys
import time
import pandas as pd
import HuMMUS_SubModule.Kraken2.TaxnomicTable as KrakenTaxonomyTable
import HuMMUS_SubModule.Diversity.Alpha as AlphaDiversity
#MainProcess = [[argument.strip().split(";")[1], " ".join(argument.strip().split(";")[2:])] for argument in open(sys.argv[1], "r")]
#print(MainProcess)
#for process in MainProcess:


#Argument = process[1]
class ModuleManager:
    def __init__(self, sysarguments):
        self.sysarguments = sysarguments
        self.ToolName = self.sysarguments[1]
        self.MainPath = os.path.abspath(os.path.realpath(__file__))

    def RunModule(self):
        if self.ToolName == "Trimmomatic":
            SampleName = self.sysarguments[2]
            arguments = " ".join(self.sysarguments[3:])
            CLine = " ".join(["trimmomatic-0.39.jar", arguments])
            os.system(CLine)


        if self.ToolName == "Trimmomatic Summary":
            trimOutputDir = self.sysarguments[2]
            SType = self.sysarguments[3]
            rawSampleDir = self.sysarguments[4]
            fastqctrimOutputDir = self.sysarguments[5]
            fastqcrawOutputDir = self.sysarguments[6]
            trimOutputsamplelist = os.listdir(trimOutputDir)
            validrawSampleList = []
            for rawSample in os.listdir(rawSampleDir):
                if SType == "paired":
                    prefix = "ps_{}"
                else:
                    prefix = "single_{}"
                if prefix.format(rawSample) in trimOutputsamplelist:
                    validrawSampleList.append(rawSample)
            trimSamplePath = " ".join(["/".join([trimOutputDir, sample]) for sample in trimOutputsamplelist])
            rawSamplePath = " ".join(["/".join([rawSampleDir, sample]) for sample in validrawSampleList])

            CLine1 = " ".join(["/home/hjkim-g15-portable/Downloads/FastQC/fastqc", rawSamplePath, "-o", fastqcrawOutputDir, "-t 2"])
            CLine2 = " ".join(["/home/hjkim-g15-portable/Downloads/FastQC/fastqc", trimSamplePath, "-o", fastqctrimOutputDir, "-t 2"])

            os.system(CLine1)
            os.system(CLine2)

        if self.ToolName == "Bowtie2":
            SampleName = self.sysarguments[2]
            arguments = " ".join(self.sysarguments[3:])
            CLine = " ".join(["bowtie2", arguments])
            print("{}".format("".join(["#", SampleName, "#"])))
            os.system(CLine)

        if self.ToolName == "Bowtie2 Summary":
            SType = self.sysarguments[2]
            LogPath = self.sysarguments[3]
            ExclusionCutOff = float(self.sysarguments[4])
            ExcludedSample = []
            LogList = "".join("  ".join("".join([line for line in open(LogPath, "r")]).split("#")).split("\n"))
            print(LogList)
            full_line = ""
            LogDict = {}
            for i in LogList.split("  "):
                if i != " " and i != "    " and i != "":
                    if not i.startswith("-"):
                        full_line += i + "|"
            idx = 0

            log = full_line.split("|")[:-1]
            if SType == "paired":
                for _ in range(int(len(log)/13)):
                    sampletitle = log[idx] if float(log[idx+7][3:7]) < ExclusionCutOff else "{} (Excluded)".format(log[idx])
                    if sampletitle.endswith("(Excluded)"):
                        ExcludedSample.append(log[idx])

                    LogDict[sampletitle] = {"Total Reads" : log[idx+1].split(" ")[0], \
                                            "Total Aligned %" : log[idx+12].split("times")[1].rsplit(" ", 3)[0], \
                                            "Total Disconc.Aligned" : log[idx+7].rsplit(" ", 4)[0], \
                                            "Conc.Aligned 0" : log[idx+3].rsplit(" ", 4)[0], \
                                            "Conc.Aligned 1" : log[idx+4].rsplit(" ", 5)[0], \
                                            "Conc.Aligned >1" : log[idx+5].rsplit(" ", 4)[0], \
                                            "UnpairedAligned 0" : log[idx+10].rsplit(" ", 3)[0], \
                                            "UnpairedAligned 1" : log[idx+11].rsplit(" ", 4)[0], \
                                            "UnpairedAligned >1" : log[idx+12].split("%")[0].rsplit(" ", 3)[0]}
                    idx += 13
                if len(ExcludedSample) != 0:
                    with open("/".join([LogPath.rsplit("/", 1)[0], "Bowtie2Excluded.txt"]), "w") as f:
                        for samplename in ExcludedSample:
                            f.write("unconc_{}.1".format(samplename) + "\n")
                            f.wrtie("unconc_{}.2".format(samplename) + "\n")
                        f.close()
            elif SType == "single":
                for _ in range(int(len(log) / 6)):
                    sampletitle = log[idx] if float(log[idx + 5].split("times")[1].split("%")[0]) < ExclusionCutOff else "{} (Excluded)".format(log[idx])
                    if sampletitle.endswith("(Excluded)"):
                        ExcludedSample.append(log[idx])
                    LogDict[sampletitle] = {"Total Reads": log[idx + 1].split(" ")[0], \
                                            "Total Aligned %": log[idx + 5].split("times")[1].rsplit(" ", 3)[0], \
                                            "UnpairedAligned 0": log[idx + 3].rsplit(" ", 3)[0], \
                                            "UnpairedAligned 1": log[idx + 4].rsplit(" ", 4)[0], \
                                            "UnpairedAligned >1": log[idx + 5].split("%")[0].rsplit(" ", 3)[0]}
                    idx += 6

                if len(ExcludedSample) != 0:
                    with open("/".join([LogPath.rsplit("/", 1)[0], "Bowtie2Excluded.txt"]), "w") as f:
                        for samplename in ExcludedSample:
                            f.write("un_{}".format(samplename) + "\n")
                        f.close()

            print(LogDict)
            LogDF = pd.DataFrame.from_dict(LogDict, orient="index")
            LogDF.to_csv("/".join([LogPath.rsplit("/", 1)[0], "Bowtie2Summary.csv"]), sep="\t")

            os.system("echo {}".format("Bowtie2 Summary Complete"))


        if self.ToolName == "Kraken2":
            SampleName = self.sysarguments[2]
            arguments = " ".join(self.sysarguments[3:])
            CLine = " ".join(["kraken2", arguments])
            print(CLine)
            print(CLine)

        if self.ToolName == "Kraken2 Taxonomic Table":
            arguments = self.sysarguments[2:]
            print("haha", arguments)
            KrakenTaxonomyTable.main(arguments)

        if self.ToolName == "Taxonomic_Alpha":
            arguments = self.sysarguments[2:]
            alphadiversity = AlphaDiversity.AlphaDiversity(arguments)
            alphadiversity.CalculateAlpha()



        if self.ToolName == "Diamond":
            SampleName = self.sysarguments[2]
            concatsamplepath = self.sysarguments[4]
            SType = self.sysarguments[5]
            SampleTitle = self.sysarguments[6]
            excluded_list = []
            bowtie_exclusion_path = "/".join([self.sysarguments[7], "Bowtie2Excluded.txt"])
            if os.path.isfile(bowtie_exclusion_path):
                excluded_list = [i.strip() for i in open(bowtie_exclusion_path, "r")]
            if SType == "paired":
                validsamplepath, validsamplelist = self.get_valid_samplelist(self.sysarguments[3], SType, excluded_list)
                print("Paired Samples start to be concatenated")
                for paired in validsamplelist:
                    forward_path = "/".join([validsamplepath, paired[0]])
                    reverse_path = "/".join([validsamplepath, paired[1]])
                    os.system("cat {} {} > {}".format(
                        forward_path,
                        reverse_path,
                        "/".join([concatsamplepath, "Concat_{}".format(SampleTitle)])
                    ))
                print("ALl valid sample have been concatenated")
                arguments = " ".join(self.sysarguments[8:])
                CLine = " ".join(["diamond", arguments])

                os.system(CLine)
            else:
                arguments = " ".join(self.sysarguments[8:])
                CLine = " ".join(["diamond", arguments])
                os.system(CLine)

    def get_valid_samplelist(self, validationpath, stype, excluded_list=None):
        Excluded_sample = []
        if excluded_list != None:
            Excluded_sample = excluded_list
        print("Excluded list {}".format(Excluded_sample))
        validationpath = validationpath
        validorderedlist = []

        if stype == "paired":
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

        elif stype == "single":
            validsamplelist = os.listdir(validationpath)
            validsamplelist.sort()
            for sample in validsamplelist:
                if sample not in Excluded_sample:
                    validorderedlist.append(sample)

            return validationpath, validorderedlist




if __name__ == "__main__":
    modulemanager = ModuleManager(sys.argv)
    modulemanager.RunModule()