from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

answers = 0

app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home():
    question_num = len(responses)
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html',title=title,instructions=instructions,question_num=question_num)

@app.route('/questions/<question_num>')
def questions(question_num):
    if request.args:
        responses.append(request.args['answer'])

    
    
    if len(responses) == len(satisfaction_survey.questions):
            return render_template('thankyou.html')

    question_num = len(responses)
    question = satisfaction_survey.questions[question_num].question
    choose = satisfaction_survey.questions[question_num].choices

    return render_template('questions.html',question_num=question_num,question=question,choose=choose,responses=responses)
    