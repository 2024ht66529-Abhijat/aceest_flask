from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

PROGRAMS = {
    'Fat Loss (FL)': {
        'workout': 'Adaptive fat‑loss training (cardio + strength, autoregulated)',
        'diet': 'Flexible calorie deficit with weekly adjustments'
    },
    'Muscle Gain (MG)': {
        'workout': 'Advanced hypertrophy with volume cycling and progression',
        'diet': 'Lean bulk nutrition with macro tracking'
    },
    'Athletic Performance (AP)': {
        'workout': 'Speed, power, and conditioning blocks',
        'diet': 'Performance‑based fueling plan'
    }
}

@routes.route('/', methods=['GET','POST'])
def home():
    selected = None
    if request.method == 'POST':
        selected = PROGRAMS.get(request.form.get('program'))
    return render_template('index.html', programs=PROGRAMS, selected=selected)
