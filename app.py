from flask import Flask, render_template
import os

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
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)
