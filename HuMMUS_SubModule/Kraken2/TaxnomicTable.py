import pandas as pd
import os, sys
import numpy as np

def Normalization(node, report, taxonomylength, pc_dict):
    NormalizedTable = report
    lca_count = float(NormalizedTable.loc[node, "LCACount"])
    length = float(taxonomylength.loc[node, "Length"])
    child_nodes = pc_dict[node]
    norm_counts = 0
    norm_child_counts = 0
    if child_nodes == ["leaf"]:
        norm_counts = (lca_count / length)
        NormalizedTable.loc[node, "NormalizedCount"] = norm_counts
    else:
        for c_node in child_nodes:
            norm_child_counts += Normalization(c_node, NormalizedTable, taxonomylength, pc_dict)[0]
        norm_counts += (lca_count / length) + norm_child_counts
        NormalizedTable.loc[node, "NormalizedCount"] = norm_counts
    return norm_counts, NormalizedTable

def ReestimateRatioWithRA(report, sample_name):
    krakentable = report
    total_counts = krakentable[:2]["Coverage"].sum()
    root_counts = krakentable[1:2]["Coverage"].sum()
    ratio = float(root_counts/total_counts)

    krakentable["NormalizedCount"] = krakentable["NormalizedCount"] * ratio

    krakentable["NormalizedRelativeCount"] = krakentable["NormalizedCount"] /float(krakentable.loc["root", "NormalizedCount"])
    nc_table = pd.DataFrame(krakentable["NormalizedCount"]).rename(columns={"NormalizedCount" : sample_name})
    ra_table = pd.DataFrame(krakentable["NormalizedRelativeCount"]).rename(columns={"NormalizedRelativeCount" : sample_name})
    return nc_table, ra_table


def MergingTable(krakenoutputpath, krakenoutputtablepath, taxonomylength, pc_dict):
    nc_inte_table = " "
    ra_inte_table = " "
    KrakenReportList = os.listdir(krakenoutputpath)
    print(KrakenReportList)
    for report in KrakenReportList:
        reportPath = "/".join([krakenoutputpath, report])

        reportTitle = report.split("report_")[1]
        print("{} in process.".format(reportTitle))
        KrakenReport = pd.read_csv(reportPath, sep = "\t", header = None,
                                   names = ["ClassifiedRatio", "Coverage", "LCACount", "Level", "0", "Taxa"],
                                   index_col = "Taxa",
                                   usecols = ["ClassifiedRatio", "Coverage", "LCACount", "Taxa"])
        KrakenReport.index = [i.split("  ")[-1] for i in KrakenReport.index]
        KrakenReport["NormalizedCount"] = np.zeros(KrakenReport.shape[0])
        NormalizedTable = Normalization("root", KrakenReport[1:], taxonomylength, pc_dict)[1]
        NormalizedTable = pd.concat([KrakenReport[:1], NormalizedTable])

        nc_table, ra_table = ReestimateRatioWithRA(NormalizedTable, reportTitle)


        if type(nc_inte_table) == str:
            nc_inte_table = nc_table
            ra_inte_table = ra_table
        else:
            nc_inte_table = nc_inte_table.join(nc_table)
            ra_inte_table = ra_inte_table.join(ra_table)
    nc_merged_table = nc_inte_table.fillna(0)
    ra_merged_table = ra_inte_table.fillna(0)
    nc_merged_table[2:].to_csv("/".join([krakenoutputtablepath, "TaxonomyNormalizedCountTable.tsv"]), sep="\t")
    ra_merged_table[2:].to_csv("/".join([krakenoutputtablepath, "TaxonomyRelativeAbundanceTable.tsv"]), sep="\t")
    print("Kraken2 Taxonomic Normalized Count Table has been created.")
    print("Kraken2 Taxonomic Normalized Relative Abundance Table has ben created")


def main(*args):
    MainPath = os.path.abspath(os.path.realpath(__file__)).rsplit("/", 1)[0]
    ParentChild = {i.strip().split("|")[0]: i.strip().split("|")[1].split(';') for i in open("/".join([MainPath, "HRGM_parent_child"]), "r")}
    TaxonomyLength = pd.read_csv("/".join([MainPath, "taxonomy_length.tsv"]), sep="\t", index_col=0)
    TaxonomyLength = TaxonomyLength * 1e-6
    arguments = args[0]
    print(arguments)
    MergingTable(arguments[0], arguments[1], TaxonomyLength, ParentChild)

if __name__ == "__main__":
    main()
