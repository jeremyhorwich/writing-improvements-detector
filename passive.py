import spacy
nlp = spacy.load("en_core_web_sm")

text = "I ate fish"
parsed_text = nlp(text)

def is_sentence_passive(sentence):
    for token in sentence:
        if token.dep_ == "nsubjpass":
            return True
    return False

print(is_sentence_passive(parsed_text))