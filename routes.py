from app import app, db
from flask import render_template, request, url_for
import requests as req
from script import list_to_db
from models import User, Company


@app.route('/')
def index():  # функция для главной страницы (она ее отображает)
    user = {'username': 'GreatRaksin'}
    # list_to_db(db)
    return render_template('index.html', title='Главная страница', user=user)


@app.route('/about')
def about():
    return render_template('about.html', title='О нас')


@app.route('/contacts')
def contacts():
    return render_template('contact.html', title='Контакты')


@app.route('/todos')
def todos():
    url = 'https://jsonplaceholder.typicode.com/todos'
    data = req.get(url).json()
    return render_template('todos.html', title='Задачи', data=data)


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
    instance = User.query.get(id=id)
    return render_template('user_page.html', title="О пользователе", user=instance)
