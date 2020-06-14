from typing import Dict, List, Any

from nltk.corpus import wordnet


class Word:
    def __init__(self, word):
        self.word = word
        self.definitions = self._get_definitions()  # dictionary with format: { 'noun': [], 'verb': [] }
        self.meanings = self._get_meanings()  # dictionary with format: { 'antonyms': [], 'synonyms': [] }
        self.examples = self._get_examples()  # list of examples

    def _get_definitions(self):
        definitions = {"noun": [], "verb": []}
        synsets = wordnet.synsets(self.word)
        for synset in synsets:
            if self.word in synset.name():
                if 'n' in synset.name().split(self.word)[1]:
                    definitions["noun"].append(synset.definition())
                else:
                    definitions["verb"].append(synset.definition())
        return definitions

    def _get_meanings(self):
        meanings = {"antonyms": [], "synonyms": []}

        return meanings

    def _get_examples(self):
        examples = []

        return examples
