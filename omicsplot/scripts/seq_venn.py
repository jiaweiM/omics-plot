import matplotlib.pyplot as plt
from matplotlib_venn import venn3_unweighted

from omicsplot.omics_excel import OmicsExcel
from omicsplot.set_tools import venn_set

in_file1 = r'C:\Users\Chen\IdeaProjects\semi\data\kidney_rerank.xlsx'
in_file2 = r"C:\Users\Chen\IdeaProjects\semi\data\kidney_unspecific_test.xlsx"
in_file3 = r"C:\Users\Chen\IdeaProjects\semi\data\kidney_sequest.xlsx"

excel1 = OmicsExcel(in_file1)
excel2 = OmicsExcel(in_file2)
excel3 = OmicsExcel(in_file3)

venn_region = venn_set(excel1.get_seq_set(), excel2.get_seq_set(), excel3.get_seq_set())
seq_v = venn3_unweighted(subsets=venn_region, set_labels=("Specific", "Unspecific", "Sequest"))
plt.title("Sequence Overlap")
plt.show()

# venn_delta_region = venn_set(excel1.get_pep_delta_set(), excel2.get_pep_delta_set(), excel3.get_pep_delta_set())
# seq_delta_v = venn3_unweighted(subsets=venn_delta_region, set_labels=("Specific", "Unspecific", "Sequest"))
#
# plt.title("Glycopeptide Overlap")
# plt.show()
