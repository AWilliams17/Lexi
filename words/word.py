from nltk.corpus import wordnet


class Word:
    def __init__(self, word):
        self.word = word
        self.definitions = {
            "noun": [],
            "verb": []
        }
        self._get_definitions()

    def _get_definitions(self):
        synsets = wordnet.synsets(self.word)
        for synset in synsets:
            if self.word in synset.name():
                if 'n' in synset.name().split(self.word)[1]:
                    self.definitions["noun"].append(synset.definition())
                else:
                    self.definitions["verb"].append(synset.definition())
