from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

answers = 0

app.config['SECRET_KEY'] = 'oh-so-secret'
#test
debug = DebugToolbarExtension(app)

responses = 'responses'

@app.route('/')
def home():
    if session['responses']:
        return redirect('/questions/<question_num>') 
    question_num = 0
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html',title=title,instructions=instructions,question_num=question_num)

@app.route('/questions/<question_num>')
def questions(question_num):
    if session['responses'] == None:
        session['responses'] = []
    responses = session['responses']
    question_num = len(responses)
    
    if request.args:
        responses = session['responses']
        answer = request.args['answer']
        responses.append(answer)
        session['responses'] = responses
        
    
    if len(responses) == len(satisfaction_survey.questions):
            session['responses'] = []
            return render_template('thankyou.html')
    
    question_num = len(responses)
    question = satisfaction_survey.questions[question_num].question
    choose = satisfaction_survey.questions[question_num].choices
    
    return render_template('questions.html',question_num=question_num,question=question,choose=choose,)
    