import skbio.diversity.alpha as alpha
import pandas as pd
import plotly.express as px

class AlphaDiversity:
    def __init__(self, *args):
        self.arguments = args[0]
        self.tablepath = self.arguments[0]
        self.outputpath = self.arguments[1]
        self.metatablepath = self.arguments[2]
        self.class1 = self.arguments[3]
        self.sclass1 = self.arguments[4]


    def CalculateAlpha(self):
        self.table = pd.read_csv(self.tablepath, sep="\t", index_col=0).T
        self.metatable = pd.read_csv(self.metatablepath, sep="\t", index_col=0)
        self.table["Class1_{}".format(self.class1)] = self.metatable.loc[self.table.index][self.class1]
        self.tablecalssname = "Class1_{}".format(self.class1)
        self.classlist = list(set(self.table["Class1_{}".format(self.class1)]))
        self.ootu_list = []
        self.shannon_list = []
        self.simpson_list =[]

        for i in self.table.index:
            self.ootu_list.append(alpha.observed_otus(self.table.loc[i][:-1]))
            self.shannon_list.append(alpha.shannon(self.table.loc[i][:-1]))
            self.simpson_list.append(alpha.simpson(self.table.loc[i][:-1]))
        self.table["ObservedOTUs"] = self.ootu_list
        self.table["ShannonIndex"]  = self.shannon_list
        self.table["SimpsonIndex"] = self.simpson_list
        OOTUs_fig = px.box(self.table, x=self.tablecalssname, y = "ObservedOTUs", notched=True, points= "all", color=self.tablecalssname)
        Shannon_fig = px.box(self.table, x=self.tablecalssname, y = "ShannonIndex", notched=True, points="all", color=self.tablecalssname)
        Simpson_fig = px.box(self.table, x=self.tablecalssname, y = "SimpsonIndex", notched=True, points="all", color=self.tablecalssname)

        OOTUs_fig.write_html("/".join([self.outputpath, "ObservedOTUs_{}".format(self.tablecalssname)]))
        Shannon_fig.write_html("/".join([self.outputpath, "ShannonIndex_{}".format(self.tablecalssname)]))
        Simpson_fig.write_html("/".join([self.outputpath, "SimpsonIndex_{}".format(self.tablecalssname)]))

        if self.sclass1 != "None":
            self.ootu_list_sub = []
            self.shannon_list_sub =[]
            self.simpson_list_sub =[]

            self.table["SubClass"] = self.metatable.loc[self.table.index][self.sclass1]
            OOTUs_fig_sub = px.box(self.table, x=self.sclass1, y="ObservedOTUs", notched=True, points="all", color=self.sclass1)
            Shannon_fig_sub = px.box(self.table, x=self.sclass1, y="ShannonIndex", notched=True, points="all", color=self.sclass1)
            Simpson_fig_sub = px.box(self.table, x=self.sclass1, y="SimpsonIndex", notched=True, points="all", color=self.sclass1)

            OOTUs_fig_sub.write_html("/".join([self.outputpath, "ObservedOTUs_{}".format(self.sclass1)]))
            Shannon_fig_sub.write_html("/".join([self.outputpath, "ShannonIndex_{}".format(self.sclass1)]))
            Simpson_fig_sub.write_html("/".join([self.outputpath, "SimpsonIndex_{}".format(self.sclass1)]))

















