from mdr import mdr

mdr_ = mdr()

mdr_.read_document('tests/BKP_АндреевДА_02.03.03_МОАИС_2023.docx')

print(mdr_.get_doc_name())