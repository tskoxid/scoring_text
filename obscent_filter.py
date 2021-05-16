import typing


class ObscentFilter:

    def __init__(self, corpus: typing.Set[str], return_string: bool):
        self.corpus = corpus
        self.return_string = return_string

    @staticmethod
    def preprocessing_text(input_text: str):
        input_text = input_text.lower().replace('\n', ' ')
        input_text = input_text.split(' ')
        filtered_list = []
        for word in input_text:
            filtered_text = [character for character in word if character.isalnum()]
            filtered_list.append("".join(filtered_text))
        return " ".join(filtered_list)

    def obscene_filter(self, input_string: str):
        list_for_check = input_string.split()
        output_str = ''
        for word in list_for_check:
            if self.preprocessing_text(word) in self.corpus:
                output_str += word.replace(word, word[0] + (len(word) - 1) * '*') + " "
            else:
                output_str += word + ' '
        return output_str

    def obscent_score(self, input_string: str):
        list_for_check = input_string.split()
        for word in list_for_check:
            if self.preprocessing_text(word) in self.corpus:
                return 0
        return 5
