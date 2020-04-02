from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def score_prediction():
    score = 0
    if request.method == "POST":
        cough = int(request.form.get("cough"))
        cold = int(request.form.get("cold"))
        diarrhea = int(request.form.get("diarrhea"))
        sore_throat = int(request.form.get("sore_throat"))
        body_aches = int(request.form.get("body_aches"))
        headache = int(request.form.get("headache"))
        fever = int(request.form.get("fever"))
        breathing = int(request.form.get("breathing"))
        fatigue = int(request.form.get("fatigue"))
        travel = int(request.form.get("travel"))
        infected_area = int(request.form.get("infected_area"))
        corona_patient = int(request.form.get("corona_patient"))
        score = (cough + cold + diarrhea + sore_throat + body_aches + headache + fever) + 2 * (
                    breathing + fatigue) + 3 * (travel + infected_area + corona_patient)
        if (score == 0):
            msg = 'Your are perfectly fine, just be safe.'
        elif (score > 0 and score <= 2):
            msg = "Above symptoms may be stress related and observe."
        elif (score >= 3 and score <= 5):
            msg = "Hydrate properly and ensure proper personal hygiene."
        elif (score >= 6 and score <= 12):
            msg = "Seek consultation from a doctor."
        else:
            msg = "Call the Corona helpline number 011-23978046 or visit hospital for corona test"
        return render_template('result.html',message = msg)
    else:
        return render_template('index.html')

@app.route('/line', methods=['GET'])
def line_graph():
    data = pd.read_csv('/home/covidassist/covidassist/india.csv')
    data_line = []
    last_update_date = data.iloc[len(data.index) - 1, 0]
    for i in data.index:
        total_cases = data.iloc[i, 1]
        total_deaths = data.iloc[i, 2]
        recovered_cases = data.iloc[i, 3]
        active_cases = data.iloc[i, 1] - data.iloc[i, 2] - data.iloc[i, 3]
        data_line.append([i, total_cases, total_deaths, active_cases, recovered_cases])
    return render_template('line.html', total_cases=total_cases, total_deaths=total_deaths,
                           active_cases=active_cases, recovered_cases=recovered_cases,
                           last_update_date=last_update_date, data_line=data_line)

@app.route('/recovery', methods=['GET'])
def recovery_graph():
    data = pd.read_csv('/home/covidassist/covidassist/india.csv')
    data_column_3 = []
    # data_column = [['Time','Growth Rate','Death Rate','Recovery Rate']]
    last_update_date = data.iloc[len(data.index) - 1, 0]
    for i in data.index:
        total_cases = data.iloc[i, 1]
        total_deaths = data.iloc[i, 2]
        recovered_cases = data.iloc[i, 3]
        active_cases = data.iloc[i, 1] - data.iloc[i, 2] - data.iloc[i, 3]
        if int(i) != len(data.index) - 1:
            data_column_3.append([i, data.iloc[i + 1, 3] - data.iloc[i, 3]])
    return render_template('recovery.html', total_cases=total_cases, total_deaths=total_deaths,
                           active_cases=active_cases, recovered_cases=recovered_cases,
                           last_update_date=last_update_date,data_column_3=data_column_3)

@app.route('/death', methods=['GET'])
def death_graph():
    data = pd.read_csv('/home/covidassist/covidassist/india.csv')
    data_column_2 = []
    last_update_date = data.iloc[len(data.index) - 1, 0]
    for i in data.index:
        total_cases = data.iloc[i, 1]
        total_deaths = data.iloc[i, 2]
        recovered_cases = data.iloc[i, 3]
        active_cases = data.iloc[i, 1] - data.iloc[i, 2] - data.iloc[i, 3]
        if int(i) != len(data.index) - 1:
            data_column_2.append([i, data.iloc[i + 1, 2] - data.iloc[i, 2]])
    return render_template('death.html', total_cases=total_cases, total_deaths=total_deaths,
                           active_cases=active_cases, recovered_cases=recovered_cases,
                           last_update_date=last_update_date,data_column_2=data_column_2)

@app.route('/growth', methods=['GET'])
def growth_graph():
    data = pd.read_csv('/home/covidassist/covidassist/india.csv')
    data_column_1 = []
    last_update_date = data.iloc[len(data.index) - 1, 0]
    for i in data.index:
        total_cases = data.iloc[i, 1]
        total_deaths = data.iloc[i, 2]
        recovered_cases = data.iloc[i, 3]
        active_cases = data.iloc[i, 1] - data.iloc[i, 2] - data.iloc[i, 3]
        if int(i) != len(data.index) - 1:
            data_column_1.append([i,data.iloc[i + 1, 1] - data.iloc[i, 1]])
    return render_template('growth.html', total_cases=total_cases, total_deaths=total_deaths,
                           active_cases=active_cases, recovered_cases=recovered_cases,
                           last_update_date=last_update_date,data_column_1=data_column_1)

@app.route('/pie', methods=['GET'])
def pie_graph():
    data = pd.read_csv('/home/covidassist/covidassist/india.csv')
    last_update_date = data.iloc[len(data.index) - 1, 0]
    for i in data.index:
        total_cases = data.iloc[i, 1]
        total_deaths = data.iloc[i, 2]
        recovered_cases = data.iloc[i, 3]
        active_cases = data.iloc[i, 1] - data.iloc[i, 2] - data.iloc[i, 3]
    return render_template('pie.html', total_cases=total_cases, total_deaths=total_deaths,
                           active_cases=active_cases, recovered_cases=recovered_cases,
                           last_update_date=last_update_date)

if __name__ == '__main__':
    app.run()
