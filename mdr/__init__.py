import spacy
import docx

nlp = spacy.load("ru_core_news_lg")

# def extract_names(text):
#     doc = nlp(text)
#     return [ent.text for ent in doc.ents if ent.label_ == "PER"]

# class DataReader_module:
