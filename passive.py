import spacy
nlp = spacy.load("en_core_web_sm")

def import_text(filename):
    file = open("texts/" + filename, "r")
    return file.read()


def is_sentence_passive(sentence):
    for token in sentence:
        if token.dep_ == "nsubjpass":
            return True
    return False

import_text("sample1")