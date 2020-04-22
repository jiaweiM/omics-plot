import plotly.graph_objects as go
from plotly.subplots import make_subplots

from omicsplot.omics_excel import OmicsExcel


def get_fraction(file_name):
    """
    return the fraction number encoded in the file name
    :param file_name:  file name with format .*_fraction[.mgf]
    :return: fraction number
    """
    lid = file_name.rfind('_')
    assert lid != -1
    rid = file_name.rfind(".")
    if rid == -1:
        rid = len(file_name)
    return int(file_name[lid + 1: rid])


def get_f_fraction(file_name):
    lid = file_name.find('_F')
    rid = file_name.rfind(".")
    if rid == -1:
        rid = len(file_name)
    return int(file_name[lid + 2:rid])


def make_compare_plot(fractions, specific_normal_count, specific_tumor_count,
                      unspecific_normal_count, unspecific_tumor_count, title, yaxis_title):
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=("Normal", "Tumor"),
                        shared_yaxes=True)

    fig.add_trace(go.Bar(
        x=fractions,
        y=specific_normal_count,
        name="Kidney Normal Specific"
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        x=fractions,
        y=unspecific_normal_count,
        name="Kidney Normal Unspecific"
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        x=fractions,
        y=specific_tumor_count,
        name="Kidney Tumor Specific"
    ), row=1, col=2)

    fig.add_trace(go.Bar(
        x=fractions,
        y=unspecific_tumor_count,
        name="Kidney Tumor Unspecific"
    ), row=1, col=2)

    fig.update_xaxes(title_text="Fraction", row=1, col=1)
    fig.update_xaxes(title_text="Fraction", row=1, col=2)

    fig.update_layout(
        title=title,
        yaxis_title=yaxis_title,
        showlegend=False
    )
    return fig


in_file = r'C:\Users\Chen\IdeaProjects\semi\data\kidney_rerank.xlsx'
in_file2 = r"C:\Users\Chen\IdeaProjects\semi\data\kidney_unspecific_test.xlsx"
out_file = "images/kidney_psm.png"

excel1 = OmicsExcel(in_file)
excel2 = OmicsExcel(in_file2)

# specific normal PSM count
fractions, normal_specific_psm_count, specific_tumor_psm_count = excel1.get_psm_his2(
    "Normal", "Tumor", get_fraction_func=get_f_fraction)
# unspecific normal PSM count
_, unspecific_normal_psm_count, unspecific_tumor_psm_count = excel2.get_psm_his2(
    "Normal", "Tumor", get_fraction_func=get_f_fraction)

fig1 = make_compare_plot(fractions, normal_specific_psm_count, specific_tumor_psm_count,
                         unspecific_normal_psm_count, unspecific_tumor_psm_count, "Kidney PSM Distribution",
                         "# PSM")

fig1.show()

fractions, specific_normal_seq_count, specific_tumor_seq_count = excel1.get_seq_his2("Normal", "Tumor",
                                                                                     get_fraction_func=get_f_fraction)
_, unspecific_normal_seq_count, unspecific_tumor_seq_count = excel2.get_seq_his2("Normal", "Tumor",
                                                                                 get_fraction_func=get_f_fraction)

fig2 = make_compare_plot(fractions, specific_normal_seq_count, specific_tumor_seq_count,
                         unspecific_normal_seq_count, unspecific_tumor_seq_count, "Kidney Sequence Distribution",
                         "# Sequence")
fig2.show()
