from app import app, db
from flask import render_template, request, url_for, redirect
from models import User, Company, ToDo


@app.route('/')
def index():  # функция для главной страницы (она ее отображает)
    user = {'username': 'GreatRaksin'}
    return render_template('index.html', title='Главная страница', user=user)


@app.route('/about')
def about():
    return render_template('about.html', title='О нас')


@app.route('/contacts')
def contacts():
    return render_template('contact.html', title='Контакты')


@app.route('/users-list')
def users_list():
  users = User.query.all()  # выгружаем все компании из БД
  return render_template('users-list.html', title='Пользователи', users=users)


@app.route('/company-list')
def companies_list():
  companies = Company.query.all()  # выгружаем всех пользователей из БД
  return render_template('company-list.html',
                         title='Компании',
                         companies=companies)


@app.route('/users/<id>')
def user(id):
    """Функция должна находить пользователя по id в списке пользователей и выдавать страницу с информацией о нем"""
    instance = User.query.get(id)
    user_todos = ToDo.query.filter_by(user_id=id)
    return render_template('user_page.html', title="О пользователе",
                           user=instance, todos=user_todos)


@app.route('/users/delete/<id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users_list'))


@app.route('/users/add-user')
def add_user():
    return render_template('add_user.html')
