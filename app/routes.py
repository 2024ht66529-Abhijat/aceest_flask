from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

PROGRAMS = {
    'Fat Loss (FL)': {
        'workout': 'Conditioning + Strength (4x/week)',
        'diet': '2000-2200 kcal high-protein diet'
    },
    'Muscle Gain (MG)': {
        'workout': 'Hypertrophy split (5x/week)',
        'diet': '3000-3300 kcal surplus nutrition'
    },
    'Beginner (BG)': {
        'workout': 'Full body fundamentals (3x/week)',
        'diet': 'Maintenance calories, balanced nutrition'
    }
}

@routes.route('/', methods=['GET', 'POST'])
def home():
    details = None
    if request.method == 'POST':
        program = request.form.get('program')
        details = PROGRAMS.get(program)
    return render_template('index.html', programs=PROGRAMS, details=details)
