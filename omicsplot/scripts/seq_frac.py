import plotly.graph_objects as go
from plotly.subplots import make_subplots

from omicsplot.omics_excel import OmicsExcel


def get_f_fraction(file_name):
    lid = file_name.find('_F')
    rid = file_name.rfind(".")
    if rid == -1:
        rid = len(file_name)
    return int(file_name[lid + 2:rid])


in_file = r'C:\Users\Chen\IdeaProjects\semi\data\kidney_rerank.xlsx'
in_file2 = r"C:\Users\Chen\IdeaProjects\semi\data\kidney_unspecific_test.xlsx"
out_file = "images/kidney_seq.png"

excel1 = OmicsExcel(in_file)
excel2 = OmicsExcel(in_file2)

fractions, specific_normal_seq_count, specific_tumor_seq_count = excel1.get_seq_his2("Normal", "Tumor",
                                                                                     get_fraction_func=get_f_fraction)
_, unspecific_normal_seq_count, unspecific_tumor_seq_count = excel2.get_seq_his2("Normal", "Tumor",
                                                                                 get_fraction_func=get_f_fraction)
for frac, sn, st, un, ut in zip(fractions, specific_normal_seq_count, specific_tumor_seq_count,
                                unspecific_normal_seq_count, unspecific_tumor_seq_count):
    print(frac, sn, st, un, ut, sep='\t')

fig = make_subplots(rows=1, cols=2,
                    subplot_titles=("Normal", "Tumor"),
                    shared_yaxes=True)

fig.add_trace(go.Bar(
    x=fractions,
    y=specific_normal_seq_count,
    name="Kidney Normal Specific"
), row=1, col=1)

fig.add_trace(go.Bar(
    x=fractions,
    y=unspecific_normal_seq_count,
    name="Kidney Normal Unspecific"
), row=1, col=1)

fig.add_trace(go.Bar(
    x=fractions,
    y=specific_tumor_seq_count,
    name="Kidney Tumor Specific"
), row=1, col=2)

fig.add_trace(go.Bar(
    x=fractions,
    y=unspecific_tumor_seq_count,
    name="Kidney Tumor Unspecific"
), row=1, col=2)

fig.update_xaxes(title_text="Fraction", row=1, col=1)
fig.update_xaxes(title_text="Fraction", row=1, col=2)

fig.update_layout(
    title="Kidney Sequence Distribution",
    yaxis_title="# Sequence",
    showlegend=False
)
fig.show()
