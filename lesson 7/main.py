from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

path = 'candidates.json'
candidates = load_candidates_from_json(path)
app = Flask(__name__)


@app.route('/')
def get_all_user():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<x>')
def get_one_candidate(x):
    item = get_candidate(x, candidates)
    if item:
        return render_template('single.html', item=item)
    return "NOT FOUND"


@app.route('/search/<candidate_name>')
def get_name(candidate_name):
    items = get_candidates_by_name(candidate_name, candidates)
    if items:
        return render_template('search.html', candidates=items)
    return "NOT FOUND"


@app.route('/skill/<skill_name>')
def get_skill(skill_name):
    items = get_candidates_by_skill(skill_name, candidates)
    if items:
        return render_template('skill.html', skill=skill_name, candidates=items)
    return "NOT FOUND"


if __name__=='__main__':
    app.run(port=5000)
