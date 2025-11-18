import spacy
import docx
import pathlib
# import typing

# nlp = spacy.load("ru_core_news_lg")

# def extract_names(text):
#     doc = nlp(text)
#     return [ent.text for ent in doc.ents if ent.label_ == "PER"]


class mdr:
    path = ""
    text_ = ""

    def __init__(self):
        self.path = ""

    def __call__(self):
        return self

    #   чтение документа
    def read_document(self, path_: str):

        # добавление названия файла
        if '/' not in path_:
            self.path = f"{pathlib.Path(__file__).parent.resolve()}{self.path}"
        #     print(f"{pathlib.Path(__file__).parent.resolve()}{self.path}")
        self.path = path_
        # print(f"{self.path}")

        try:
            doc = docx.Document(self.path)

            fullText = []

            for p in doc.paragraphs:
                fullText.append(p.text)

            self.text_ = '\n'.join(fullText)

        except:
            print("ERROR: Не удалось найти файл!")
    
    # получение названия файла
    def get_doc_name(self):
        return self.path.split('/')[-1]





# чтение документа
# def read_document(file_name_: str):
