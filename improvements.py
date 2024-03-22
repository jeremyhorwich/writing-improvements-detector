from collections import defaultdict

import spacy
nlp = spacy.load("en_core_web_sm")

def import_text(filename):
    file = open("texts/" + filename + ".txt", "r")
    return file.read()


def mark_improveable_sentences(document):
    TOO_LONG = 20
    VERY_TOO_LONG = 27

    long = set()
    very_long = set()
    passive = set()
    adverbs = defaultdict(list)
    for sent in document.sents:
        if len(sent) > VERY_TOO_LONG:
            very_long.add(sent)
        elif len(sent) > TOO_LONG:
            long.add(sent)
        for token in sent:
            if token.dep_ == "nsubjpass":
                passive.add(sent)
            if token.pos_ == "ADV":
                adverbs[sent].append(token)
    return (long, very_long, passive, adverbs)


def display_improvable_sentences(document, problems):
    long,very_long,passive,adverbs = problems
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


if __name__ == "__main__":
    text = import_text("sample1")
    doc = nlp(text)
    problems = mark_improveable_sentences(doc)
    display_improvable_sentences(doc,problems)
