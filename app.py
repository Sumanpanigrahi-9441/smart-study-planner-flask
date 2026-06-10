from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/planner', methods=['GET', 'POST'])
def planner():
    if request.method == 'POST':
        subject = request.form['subject']
        exam_date = request.form['exam_date']
        hours = int(request.form['hours'])

        today = datetime.today().date()
        exam = datetime.strptime(exam_date, "%Y-%m-%d").date()

        days_left = (exam - today).days

        return render_template(
            'result.html',
            subject=subject,
            exam_date=exam_date,
            hours=hours,
            days_left=days_left
        )

    return render_template('planner.html')

if __name__ == '__main__':
    app.run(debug=True)
