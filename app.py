from flask import Flask, render_template, send_file
import os

app = Flask('Flask')


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/science')
def science():
    return render_template('science.html')


@app.route('/achievements')
def achievements():
    return render_template('achievements.html')


@app.route('/cultural')
def cultural():
    return render_template('cultural.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(app.root_path, 'static', 'pdf', filename)
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404


app.run(debug=True, host='0.0.0.0', port='8080')
