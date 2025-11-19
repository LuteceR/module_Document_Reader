from mdr import mdr
# from mdr import lookingup

mdr_ = mdr()

mdr_.read_document('tests/BKP_АндреевДА_02.03.03_МОАИС_2023.docx')

mdr_.extract_names()