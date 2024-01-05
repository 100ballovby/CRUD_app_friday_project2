from sqlalchemy.sql.functions import current_user

from app import app, db
from flask import render_template, request, url_for, redirect
from models import User, Company, ToDo
from forms import UserForm, CompanyForm, ToDoForm
from datetime import datetime


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


@app.route('/users/add-user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():  # если форма отправлена
        new_user = User(
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            street=form.street.data,
            city=form.city.data,
            phone=form.phone.data,
            company_id=form.company_id.data
        )  # создать нового пользователя
        db.session.add(new_user)  # добавить его в базу
        db.session.commit()  # сохранить изменения
        return redirect(url_for('users_list'))  # перенаправить обратно на список
    return render_template('add_user.html', form=form)


@app.route('/companies/add-company', methods=['GET', 'POST'])
def add_company():
    form = CompanyForm()
    if form.validate_on_submit():
        new_company = Company(
            name=form.name.data,
            website=form.website.data
        )
        db.session.add(new_company)
        db.session.commit()
        return redirect(url_for('companies_list'))
    return render_template('add_company.html', form=form)


@app.route('/todos/add-todo', methods=['GET', 'POST'])
def add_todo():
    form = ToDoForm()
    todos = ToDo.query.order_by(ToDo.created_at.desc()).all()
    today = datetime.now()
    if form.validate_on_submit():
        new_todo = ToDo(
            title=form.title.data,
            user_id=form.user_id.data,
            created_at=today,
            deadline=today
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('add_todo'))
    return render_template('add_todo.html', title="Add new ToDo",
                           form=form, todos=todos)
