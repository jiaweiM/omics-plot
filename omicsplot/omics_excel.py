from collections import defaultdict

import numpy as np
import pandas as pd

_sheet_parameter = "Parameter"
_sheet_psm = "PSM"
_sheet_peptide = 'Peptide'
_tag_ms_file = "MS Files"
_tag_fixed_modifications = "Fixed Modifications"


class OmicsExcel:
    def __init__(self, file):
        self.excel_file = pd.ExcelFile(file)

    def read_pm(self):
        """
            read the MS files
            :param omics_excel: pandas DataFrame of the omics-excel file's parameter sheet
            :return: dict of the ms files, ms file title -> (name, location)
            """
        df_pm = pd.read_excel(self.excel_file, _sheet_parameter, header=None)
        row_it = df_pm.itertuples()
        id_name_map = {}
        for row in row_it:
            if row[1] == _tag_ms_file:
                next(row_it)
                while True:
                    cur_row = next(row_it)
                    title = cur_row[1]
                    if title == np.nan or title == _tag_fixed_modifications:
                        break
                    name = cur_row[2]
                    location = cur_row[3]
                    id_name_map[title] = (name, location)
                break
        return id_name_map

    def get_psm_distribution(self):
        """
        return the # PSM in different fraction
        :return:  Series of psm distribution
        """
        df_psm = pd.read_excel(self.excel_file, _sheet_psm)
        file_col = df_psm.loc[:, "MS File"]
        return file_col.value_counts()

    def get_seq_distribution(self):
        """
        Return peptide sequence distribution in different fraction
        :return:  `defaultdict` file->sequence set
        """
        df_psm = pd.read_excel(self.excel_file, _sheet_psm)
        d = defaultdict(set)
        for file, seq in zip(df_psm.loc[:, "MS File"], df_psm.loc[:, "Sequence"]):
            d[file].add(seq)
        return d

    def get_psm_his1(self, get_fraction_func):
        dis = self.get_psm_distribution()
        his = {}
        for id in dis.index.values:
            his[get_fraction_func(id)] = dis.loc[id]
        return his

    def get_psm_his2(self, his1_key, his2_key, get_fraction_func):
        """
        get # PSM distribution
        :param file: file to parse
        :param get_fraction_func: function to get fraction number from file name
        :param his1_key: key for the first histogram
        :param his2_key: key for the second histogram
        :return: two dict fraction -> # PSM
        """
        dis = self.get_psm_distribution()
        his1_dict = {}
        his2_dict = {}
        for id in dis.index.values:
            fraction = get_fraction_func(id)
            if his1_key in id:
                his1_dict[fraction] = dis.loc[id]
            if his2_key in id:
                his2_dict[fraction] = dis.loc[id]
        fractions = list(his1_dict)
        fractions.sort()
        his1_count = []
        his2_count = []
        for frac in fractions:
            his1_count.append(his1_dict[frac])
            his2_count.append(his2_dict[frac])

        return fractions, his1_count, his2_count

    def get_seq_set(self):
        """
        Return unique sequences
        :return: ndarray of unique sequence
        """
        df = pd.read_excel(self.excel_file, _sheet_peptide)
        return set(df.loc[:, "Sequence"].unique())

    def get_seq_delta_set(self):
        """
        Return (sequence,delta) set
        :return: set of (sequence,delta)
        """
        df = pd.read_excel(self.excel_file, _sheet_psm)
        seq_delta_set = set()
        for seq, delta in zip(df.loc[:, "Sequence"], df.loc[:, "Delta Name"]):
            seq_delta_set.add((seq, delta))
        return seq_delta_set

    def get_pep_delta_set(self):
        """
        Return (peptide,delta) set
        :return: set of (sequence,delta)
        """
        df = pd.read_excel(self.excel_file, _sheet_psm)
        seq_delta_set = set()
        for seq, delta in zip(df.loc[:, "Modified Sequence"], df.loc[:, "Delta Name"]):
            seq_delta_set.add((seq, delta))
        return seq_delta_set

    def get_seq_his2(self, his1_key, his2_key, get_fraction_func):
        """
        get # PSM distribution
        :param file: file to parse
        :param get_fraction_func: function to get fraction number from file name
        :param his1_key: key for the first histogram
        :param his2_key: key for the second histogram
        :return: two dict fraction -> # PSM
        """
        df_psm = pd.read_excel(self.excel_file, _sheet_psm)
        d = defaultdict(set)
        for file, seq in zip(df_psm.loc[:, "MS File"], df_psm.loc[:, "Sequence"]):
            d[file].add(seq)
        his1_dict = {}
        his2_dict = {}
        for file, seq_set in d.items():
            fraction = get_fraction_func(file)

            if his1_key in file:
                his1_dict[fraction] = len(seq_set)
            if his2_key in file:
                his2_dict[fraction] = len(seq_set)
        fractions = list(his1_dict)
        fractions.sort()
        his1_count = []
        his2_count = []
        for frac in fractions:
            his1_count.append(his1_dict[frac])
            his2_count.append(his2_dict[frac])

        return fractions, his1_count, his2_count
