startSurveyBtn = document.querySelector('#start-survey')

startSurveyBtn.addEventListener('click', startSurveyBtnClick)

function startSurveyBtnClick(evt) {
    window.location.href = 'http://127.0.0.1:5000/questions/0'
}

