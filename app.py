from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('resume.html', section="about")

@app.route('/about')
def about():
    return render_template('resume.html', section="about")

@app.route('/education')
def education():
    return render_template('resume.html', section="education")

@app.route('/skills')
def skills():
    return render_template('resume.html', section="skills")

@app.route('/experience')
def experience():
    return render_template('resume.html', section="experience")

if __name__ == '__main__':
    app.run(debug=True)



