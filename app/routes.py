from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

PROGRAMS = {
    'Fat Loss (FL)': {
        'workout': 'Phase-based fat loss training with conditioning and strength',
        'diet': 'Calorie cycling with adaptive weekly deficit'
    },
    'Muscle Gain (MG)': {
        'workout': 'Volume and intensity periodized hypertrophy programming',
        'diet': 'Lean bulk strategy with macro tracking'
    },
    'Athletic Performance (AP)': {
        'workout': 'Speed, agility, power and conditioning microcycles',
        'diet': 'Performance-oriented fueling and recovery nutrition'
    }
}

@routes.route('/', methods=['GET','POST'])
def home():
    selected = None
    if request.method == 'POST':
        selected = PROGRAMS.get(request.form.get('program'))
    return render_template('index.html', programs=PROGRAMS, selected=selected)
