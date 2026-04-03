from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

PROGRAMS = {
    'Fat Loss (FL)': {
        'workout': 'Fat‑loss focused conditioning + strength (4–5 days/week)',
        'diet': 'High‑protein diet, 2000–2200 kcal/day'
    },
    'Muscle Gain (MG)': {
        'workout': 'Structured hypertrophy training split (5–6 days/week)',
        'diet': 'Calorie surplus nutrition, 3000–3300 kcal/day'
    },
    'Beginner (BG)': {
        'workout': 'Introductory full‑body workouts (3 days/week)',
        'diet': 'Balanced maintenance‑level nutrition'
    }
}

@routes.route('/', methods=['GET', 'POST'])
def home():
    selected = None
    if request.method == 'POST':
        program = request.form.get('program')
        selected = PROGRAMS.get(program)
    return render_template('index.html', programs=PROGRAMS, selected=selected)
