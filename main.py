from obscent_filter import ObscentFilter
from score_bred import CheckSpells
from csv import reader

PATH_CORPUS: str = r"../scoring_text2/data/profane_corpus.csv"
corpus_list: list = []
with open(PATH_CORPUS, 'r', encoding='utf8') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        corpus_list.append(row[0])
corpus_set: set = set(corpus_list)


if __name__ == "__main__":
    text_list = ['Я, БЛЯТЬ, РАЗОЧАРОВАНА, ИДИ НАХУЙ', 'ВСЕ БУДЕТ ТАК, КАК Я ХОЧУ', 'УеБоК ,НахУй',
                 'ятутпишу буссвезнуюхрень имненестыдно', 'вфиваф фваршцузгардфылвои!@ыва фвыоислфысилофывси',
                 'Здарова почаны, чо по митингу, у нас залупа, нужно решить пару тасок']

    obscent_filter = ObscentFilter(corpus_set, return_string=True)
    russian = CheckSpells()

    for sentence in text_list:
        score_bred = russian.pipeline(obscent_filter.preprocessing_text(sentence))
        filtered_text = obscent_filter.obscene_filter(sentence)
        score_obscent = obscent_filter.obscent_score(sentence)

        print(f"\nScore нормальности текста: {score_bred}")
        print(f"Score мата: {score_obscent}")
        print(f"Общий score: {score_bred+score_obscent}")
        print('Отфильтрованный текст: ', filtered_text)
        if score_obscent + score_bred < 7:
            print("Пожалуйста проверь что ты написал. \n")
