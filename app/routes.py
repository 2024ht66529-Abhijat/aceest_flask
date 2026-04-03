from flask import Blueprint, render_template, request
routes = Blueprint('routes', __name__)

PROGRAMS = {
 'Fat Loss (FL)': {
   'workout': '4–5 days conditioning + strength; weekly progression',
   'diet': 'High protein 2000–2200 kcal; carb cycling'
 },
 'Muscle Gain (MG)': {
   'workout': '5–6 day hypertrophy split; progressive overload',
   'diet': '3000–3300 kcal surplus; protein + carbs'
 },
 'Beginner (BG)': {
   'workout': '3 day full body fundamentals; mobility focus',
   'diet': 'Maintenance calories; balanced macros'
 }
}

@routes.route('/', methods=['GET','POST'])
def home():
    selected=None
    if request.method=='POST':
        selected=PROGRAMS.get(request.form.get('program'))
    return render_template('index.html', programs=PROGRAMS, selected=selected)
