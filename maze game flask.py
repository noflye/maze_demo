from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def maze_game():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('maze.html', name=name)
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_game():
    name = request.form['name']
    return render_template('play.html', name=name)

@app.route('/choice1', methods=['POST'])
def choice_1():
    choice1 = request.form['choice']
    if choice1 == 'left':
        result = "You have encountered a zombie. It kills you. \nGAME OVER"
    elif choice1 == 'right':
        result = "You have advanced."
    return render_template('choice1.html', result=result)

@app.route('/choice2', methods=['POST'])
def choice_2():
    choice2 = request.form['choice']
    if choice2 == 'left':
        result = "You have advanced."
    elif choice2 == 'right':
        result = "You have encountered a spider. It kills you. \nGAME OVER"
    return render_template('choice2.html', result=result)

@app.route('/choice3', methods=['POST'])
def choice_3():
    choice3 = request.form['choice']
    if choice3 == 'left':
        result = "You have encountered a Lich. It kills you. \nGAME OVER"
    elif choice3 == 'right':
        name = request.form['name']
        result = f"You have found the way out, congrats {name}. \nYou are no longer lost."
    return render_template('choice3.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
