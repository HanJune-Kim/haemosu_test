import skbio.diversity.alpha as alpha
import pandas as pd
import plotly.express as px

class BetaDiversity:
    def __init__(self, *args):
        self.arguments = args[0]
        self.tablepath = self.arguments[0]
        self.outputpath = self.arguments[1]
        self.metatablepath = self.arguments[2]
        self.class1 = self.arguments[3]
        self.sclass1 = self.arguments[4]

    def CalculateBetaDiversity(self):
        self.table = pd.read_csv(self.tablepath, sep="\t", index_col=0).T
        self.metatable = pd.read_csv(self.metatablepath, sep="\t", index_col=0)
        self.table["Class1_{}".format(self.class1)] = self.metatable.loc[self.table.index][self.class1]
        self.tablecalssname = "Class1_{}".format(self.class1)
        self.classlist = list(set(self.table["Class1_{}".format(self.class1)]))
        self.ootu_list = []
        self.shannon_list = []
        self.simpson_list = []
