import spacy
import docx
import pathlib
import mpire
# import typing

nlp = spacy.load("ru_core_news_lg")

# def extract_names(text):
#     doc = nlp(text)
#     return [ent.text for ent in doc.ents if ent.label_ == "PER"]


class mdr:
    def __init__(self):
        self.path = ""
        self.nlp = None
        self.names_ = [] 
        self.n = 10
        self.text_ = ""
        self.tables_ = []

        try:
            self.nlp = spacy.load("ru_core_news_lg")
            print("Успешная инициализация НЛП модели")

        except OSError:
            print("Error: spaCy model 'ru_core_news_lg' not found.")
            print("Please run: python -m spacy download ru_core_news_lg")

    def __call__(self):
        return self

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

            # чтение текста
            for p in doc.paragraphs:
                fullText.append(p.text)

            self.text_ = '\n'.join(fullText)
            
            # чтение таблиц
            # for table in doc.tables:
            #     for row in table.rows:
            #         row_ = []
            #         for cell in row.cells:
            #             for p in cell.paragraphs:
            #                 row_.append(p)
                    
            #         row_ = '\n'.join(row_)
            #         self.tables_.append(row_)
            
            # print(self.tables_)
                                                


        except:
            print("ERROR: Не удалось найти файл!")

        # чтение таблиц
        for table in doc.tables:
            table_ = []
            for row in table.rows:
                row_ = []
                for cell in row.cells:
                    for p in cell.paragraphs:
                        row_.append(p.text)
                
                row_ = ' '.join(row_)
                table_.append(row_)
            self.tables_.append(table_)
        
        print(self.tables_)

    def get_doc_name(self):
        """
        getter для имени файла
        """
        return self.path.split('/')[-1]
    
    def set_n(self, n):
        """
        n - количество найденных НЛП ФИО с начала документа и конца, которые берутся на дальнейшую обработку
        """

        self.n = n

    def extract_names(self):
        
        """
        Нахождение имен в при помощи NLP библиотеки spaCy
        """

        if not self.nlp or not self.text_:
            print("Не удалось найти имена: модель не была загружена или документ пустой")
            return []

        doc = self.nlp(self.text_)
        # names = [ent.text for ent in doc.ents if ent.label_ == "PER"]
        # self.names_ = names

        # берём только первые 10 найденных имён, дальше - мусор

        # проверка на то, чтобы n всегда было в range для doc.ents.count 
        # if self.n > doc.ents.__len__():
        #     self.n = doc.ents.__len__()
        #     print(f"doc.ents.__len__() = {doc.ents.__len__()}")

        # for i in range(self.n):
        #     if doc.ents[i].label_ == "PER":
        #         self.names_.append([doc.ents[i].text, [doc.ents[i].start_char, doc.ents[i].end_char]])
        #     if doc.ents[-i - 1].label == "PER":
        #         self.names_.append([doc.ents[-i - 1].text, [doc.ents[-i].start_char, doc.ents[-i].end_char]])
        #         # print(doc.ents[i].text, doc.ents[i].start_char, doc.ents[i].end_char)
        # print(f"Удалось обнаружить {self.names_.__len__()} предположительных имён")
        # print(self.names_)
        
        """
        Поиск преподавателей и студентов
        """

        # for el_ in self.names_:
            





# чтение документа
# def read_document(file_name_: str):
