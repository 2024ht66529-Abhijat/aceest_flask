from flask import Blueprint, render_template, request
routes = Blueprint('routes', __name__)

PROGRAMS = {
    'Fat Loss (FL)': 'Structured fat loss plan ~2000 kcal',
    'Muscle Gain (MG)': 'Hypertrophy muscle gain plan ~3200 kcal',
    'Beginner (BG)': 'Beginner full body fitness program'
}

@routes.route('/', methods=['GET', 'POST'])
def home():
    selected = None
    if request.method == 'POST':
        selected = PROGRAMS.get(request.form.get('program'))
    return render_template('index.html', programs=PROGRAMS, selected=selected)
