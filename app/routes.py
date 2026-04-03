from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

PROGRAMS = {
    'Fat Loss (FL)': {
        'workout': '4–5 days conditioning + strength with deload weeks',
        'diet': '2000–2200 kcal high‑protein, macro‑cycled diet'
    },
    'Muscle Gain (MG)': {
        'workout': 'Periodized hypertrophy split (5–6 days/week)',
        'diet': '3000–3400 kcal calorie‑surplus nutrition plan'
    },
    'Beginner (BG)': {
        'workout': '3 day full‑body fundamentals, mobility & technique',
        'diet': 'Maintenance calories, balanced macronutrients'
    }
}

@routes.route('/', methods=['GET', 'POST'])
def home():
    selected = None
    if request.method == 'POST':
        selected = PROGRAMS.get(request.form.get('program'))
    return render_template('index.html', programs=PROGRAMS, selected=selected)
