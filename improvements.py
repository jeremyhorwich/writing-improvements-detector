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


def mark_improveable_sentences(document):
    passive = list()
    long = list()
    very_long = list()
    contains_adverbs = list()

    for sent in document.sents:
        if len(sent) > 20:
            very_long.append(sent.text)
        elif len(sent) > 14:
            long.append(sent.text)
        #passive
        #adverbs
        pass


text = import_text("sample1")
doc = nlp(text)