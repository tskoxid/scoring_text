from spellchecker import SpellChecker


class CheckSpells:

    def __init__(self):
        self.russian_checker = SpellChecker(distance=1, language='ru')

    def pipeline(self, orig_input: str):
        count_bred = 0
        orig_input = orig_input.split()
        misspelled = self.russian_checker.unknown(orig_input)
        if len(misspelled) == 0:
            return 5
        for word in misspelled:
            if isinstance(self.russian_checker.candidates(word), type(None)):
                continue
            if word == list(self.russian_checker.candidates(word))[0]:
                count_bred += 1
        return 5 * (1 - count_bred / len(orig_input))
