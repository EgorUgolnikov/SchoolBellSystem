# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import time

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')

if not DATABASE_URI:
    DATABASE_URI = 'sqlite:///bells.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)


class Bell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

with app.app_context():
    db.create_all()

DAYS = ['Понедельник', 'Вторник', 'Среда',
        'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


@app.route('/')
def manage_bells():
    bells = Bell.query.order_by(Bell.start_time).all()
    grouped_bells = {day: [] for day in DAYS}

    for bell in bells:
        grouped_bells[bell.day].append(bell)

    return render_template('bells.html',
                           days=DAYS,
                           bells=grouped_bells)


@app.route('/add', methods=['POST'])
def add_bell():
    try:
        start = time.fromisoformat(request.form['start'])
        end = time.fromisoformat(request.form['end'])

        if start >= end:
            flash('Ошибка: Время окончания должно быть позже начала', 'danger')
            return redirect(url_for('manage_bells'))

        bell = Bell(
            day=request.form['day'],
            start_time=start,
            end_time=end
        )

        db.session.add(bell)
        db.session.commit()
        flash('Звонок успешно добавлен', 'success')
    except Exception as e:
        flash(f'Ошибка при добавлении: {str(e)}', 'danger')

    return redirect(url_for('manage_bells'))


@app.route('/edit/<int:id>', methods=['POST'])
def edit_bell(id):
    try:
        bell = Bell.query.get_or_404(id)
        bell.day = request.form['day']
        bell.start_time = time.fromisoformat(request.form['start'])
        bell.end_time = time.fromisoformat(request.form['end'])

        if bell.start_time >= bell.end_time:
            flash('Ошибка: Время окончания должно быть позже начала', 'danger')
            return redirect(url_for('manage_bells'))

        db.session.commit()
        flash('Изменения сохранены', 'success')
    except Exception as e:
        flash(f'Ошибка при редактировании: {str(e)}', 'danger')

    return redirect(url_for('manage_bells'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_bell(id):
    try:
        bell = Bell.query.get_or_404(id)
        db.session.delete(bell)
        db.session.commit()
        flash('Звонок успешно удален', 'success')
    except Exception as e:
        flash(f'Ошибка при удалении: {str(e)}', 'danger')

    return redirect(url_for('manage_bells'))


@app.route('/toggle/<int:id>', methods=['POST'])
def toggle_bell(id):
    try:
        bell = Bell.query.get_or_404(id)
        bell.is_active = not bell.is_active
        db.session.commit()
    except Exception as e:
        flash(f'Ошибка при изменении статуса: {str(e)}', 'danger')

    return redirect(url_for('manage_bells'))


if __name__ == '__main__':
    app.run(debug=True)