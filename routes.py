from app import app
from flask import render_template, request, url_for
import requests as req


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


@app.route('/todos')
def todos():
    url = 'https://jsonplaceholder.typicode.com/todos'
    data = req.get(url).json()
    return render_template('todos.html', title='Задачи', data=data)

