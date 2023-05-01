from flask import Flask, request, jsonify, render_template
from obscent_filter import ObscentFilter
from score_bred import CheckSpells
from csv import reader


app = Flask(__name__)


PATH_CORPUS: str = r"./data/profane_corpus.csv"
corpus_list: list = []
with open(PATH_CORPUS, 'r', encoding='utf8') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        corpus_list.append(row[0])
corpus_set: set = set(corpus_list)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        sentence = to_predict_list['Sentence']
        score_bred = russian.pipeline(obscent_filter.preprocessing_text(sentence))
        filtered_text = obscent_filter.obscene_filter(sentence)
        score_obscent = obscent_filter.obscent_score(sentence)
        return render_template(
            "result.html",
            score_bred=score_bred,
            filtered_text=filtered_text,
            score_obscent="contains obscene words" if score_obscent == 0 else "Doesn't contain obscene words"
        )


if __name__ == "__main__":
    obscent_filter = ObscentFilter(corpus_set, return_string=True)
    russian = CheckSpells()

    app.run(debug=True, host='0.0.0.0')
