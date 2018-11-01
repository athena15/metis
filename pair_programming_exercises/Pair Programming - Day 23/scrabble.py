from flask import Flask, request, render_template

app = Flask('Scrabble Scoring')

point_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
                'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q':10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4,
                'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

@app.route('/')
def welcome():
    return 'Welcome to Scrabble Score'

@app.route('/hand/<letters>')
def points(letters):
    score = 0

    for char in letters:
        score += point_values[char.upper()]
    
    return render_template('score.html', word=letters, score=score)

if __name__ == '__main__':
    app.run()