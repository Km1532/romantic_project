from flask import Flask, render_template

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def home():
    return render_template('index.html')

# Шаблон історії
@app.route('/story')
def story():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True)
