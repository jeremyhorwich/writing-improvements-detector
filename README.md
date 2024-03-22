# Writing Improvements Detector

Small project designed for me to learn about the Spacy library. The goal was to approximate features of the Hemingway Editor: https://hemingwayapp.com/. Originally the project was meant to be lengthier and more involved but Spacy turned out to be powerful enough to make
the project quite simple.

Features included:
- Adverb detection
- Passive voice detection
- Wordy and very wordy sentence detection

Features not included:
- Setting a goal for number of adverbs / passive voice sentences to be under. I don't think this is a very useful feature (improvements should be decided on a case by case basis, not by some arbitrary threshold), but it could be easily recreated with only a few lines of code.
- Finding a phrase with a simpler alternative. I would need to import a database of synonyms, and that will blow the size of the data included in the project out of the water. But ultimately implementation would involve checking if a similar enough word (according to the database) was shorter than the current word used
- Scoring "readability" by grade level. I have absolutely no idea the heuristics for which the Hemingway Editor decides this number but it always felt to me to be arbitrary and often wrong.
