from flask import Blueprint, render_template, request
routes = Blueprint('routes', __name__)

PROGRAMS = {
    'Fat Loss': {'desc': 'Fat-burning workouts with calorie deficit diet'},
    'Muscle Gain': {'desc': 'Strength & hypertrophy focused program'},
    'Athletic Performance': {'desc': 'Speed, agility & endurance training'}
}

@routes.route('/', methods=['GET','POST'])
def home():
    selected = None
    if request.method == 'POST':
        selected = PROGRAMS.get(request.form.get('program'))
    return render_template('index.html', programs=PROGRAMS, selected=selected)
