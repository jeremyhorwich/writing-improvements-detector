import spacy
nlp = spacy.load("en_core_web_sm")

text = "fish was eaten"
parsed_text = nlp(text)

for token in parsed_text:
    print(token.text,token.dep_)
