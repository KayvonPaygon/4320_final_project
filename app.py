from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/reservations')
def reservations():
    return render_template('reservations.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
