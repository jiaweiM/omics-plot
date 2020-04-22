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
