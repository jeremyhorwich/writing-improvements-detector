from collections import defaultdict

import spacy
nlp = spacy.load("en_core_web_sm")

def import_text(filename):
    file = open("texts/" + filename, "r")
    return file.read()


def mark_improveable_sentences(document):
    long = set()
    very_long = set()
    passive = set()
    adverbs = defaultdict(list)
    for sent in document.sents:
        if len(sent) > 20:
            very_long.add(sent.text)
        elif len(sent) > 14:
            long.add(sent.text)
        for token in sent:
            if passive[-1] != sent and token.dep_ == "nsubjpass":
                passive.add(sent)
            if token.pos_ == "ADV":
                adverbs[sent].append(token)
    return long, very_long, passive, adverbs


def display_improvable_sentences(document,long,very_long,passive,adverbs):
    print("Sentences with problems found: ")
    for sent in document.sents:
        sentence_printed = False
        if sent in long:
            print(sent, " -- this sentence is too long")
            sentence_printed = True
        if sent in very_long:
            print(sent," -- this sentence is much too long")
            sentence_printed = True
        if sent in passive:
            if not sentence_printed:
                print(sent, " -- this sentence is passive")
                sentence_printed = True
            else:
                print("The sentence is also passive")
        if sent in adverbs:
            if not sentence_printed:
                print(sent)
                sentence_printed = True
            print("The following adverbs were found: ", adverbs[sent])
        if sentence_printed:
            print()



text = import_text("sample1")
doc = nlp(text)