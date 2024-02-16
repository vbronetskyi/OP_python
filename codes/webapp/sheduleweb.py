from flask import Flask, render_template, request, redirect
from shedule_for_CK import CK_shedule

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    rooms = request.form['rooms']
    title = 'Here are results:'
    results = CK_shedule(int(phrase), int(letters), rooms).split('\n')
    return render_template('results.html', the_phrase = phrase,
    the_letters = letters, the_title=title, the_results=results, the_rooms = rooms)

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to schedule_for_CK on the web')

if __name__ == '__main__':
    app.run(debug = True)
