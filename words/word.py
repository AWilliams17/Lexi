from typing import Dict, List, Any

from nltk.corpus import wordnet
from pronouncing import rhymes


class Word:
    def __init__(self, word):
        self.word = word
        self._synsets = wordnet.synsets(self.word)
        self.definitions = self._get_definitions()  # dictionary with format: { 'noun': [], 'verb': [] }
        self.meanings = self._get_meanings()  # dictionary with format: { 'antonyms': [], 'synonyms': [] }
        self.examples = self._get_examples()  # list of examples
        self.rhymes = None

    def __repr__(self):
        pass

    def _get_definitions(self):
        definitions = {"noun": [], "verb": []}
        for synset in self._synsets:
            if self.word in synset.name():
                if 'n' in synset.name().split(self.word)[1]:
                    definitions["noun"].append(synset.definition())
                else:
                    definitions["verb"].append(synset.definition())
        return definitions

    def _get_meanings(self):
        meanings = {"antonyms": [], "synonyms": []}
        for synset in self._synsets:
            syn_lemmas = synset.lemmas()
            for lem in syn_lemmas:
                synonym = lem.name().replace('_', ' ')
                if lem.antonyms():
                    antonym = lem.antonyms()[0].name().replace('_', ' ')
                    if antonym not in meanings['antonyms']:
                        meanings['antonyms'].append(antonym)
                if synonym not in meanings['synonyms']:
                    meanings['synonyms'].append(synonym)

        return meanings

    def _get_examples(self):
        examples = []

        return examples

    def _get_rhymes(self):
        pass
