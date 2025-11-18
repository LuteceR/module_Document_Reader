import spacy
import docx
import pathlib
# import typing

nlp = spacy.load("ru_core_news_lg")

# def extract_names(text):
#     doc = nlp(text)
#     return [ent.text for ent in doc.ents if ent.label_ == "PER"]


class mdr:
    def __init__(self):
        self.path = ""
        self.nlp = None

        try:
            self.npl = spacy.load("ru_core_web_lg")
            print("Успешная инициализация НЛП модели")

        except OSError:
            print("Error: spaCy model 'ru_core_web_lg' not found.")
            print("Please run: python -m spacy download ru_core_web_lg")

    def __call__(self):
        return self

    #   чтение документа
    def read_document(self, path_: str):
        """
        добавление и считывания файла .docx формата
        """
        if '/' not in path_:
            self.path = f"{pathlib.Path(__file__).parent.resolve()}{self.path}"
        self.path = path_

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
        """
        getter для имени файла
        """
        return self.path.split('/')[-1]
    
    def extract_names(self):
        if not self.nlp or not self.text_:
            print("Cannot extract names: Model not loaded or document is empty.")
            return []

        doc = self.nlp(self.text_)
        names = [ent.text for ent in doc.ents if ent.label_ == "PER"]
        return names





# чтение документа
# def read_document(file_name_: str):
