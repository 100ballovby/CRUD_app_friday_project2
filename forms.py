from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField, widgets
from wtforms.validators import DataRequired
from models import Company


class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()],
                       render_kw={'class': 'form-control my-3',
                                  'placeholder': 'Name'})
    username = StringField('Username', validators=[DataRequired()],
                           render_kw={'class': 'form-control my-3',
                                      'placeholder': 'User Name'})
    email = EmailField('Email', validators=[DataRequired()],
                       render_kw={'class': 'form-control my-3',
                                  'placeholder': 'example@example.com'})
    street = StringField('Street', validators=[DataRequired()],
                         render_kw={'class': 'form-control my-3',
                                    'placeholder': 'Street'})
    city = StringField('City', validators=[DataRequired()],
                       render_kw={'class': 'form-control my-3',
                                  'placeholder': 'City'})
    phone = StringField('Phone', validators=[DataRequired()],
                        render_kw={'class': 'form-control my-3',
                                   'placeholder': '+375291234567'})
    company_id = SelectField('Company', coerce=int,
                             render_kw={'class': 'form-select'})
    submit = SubmitField('Add', render_kw={'class': 'btn btn-primary mt-3'})

    def __init__(self):
        super().__init__()
        companies = []
        for company in Company.query.all():
            companies.append((company.id, company.name))
        self.company_id.choices = companies


class CompanyForm(FlaskForm):
    name = StringField('Company Name', validators=[DataRequired()],
                       render_kw={'class': 'form-control my-3',
                                  'placeholder': 'Company name'})
    website = StringField('Website', validators=[DataRequired()],
                          render_kw={'class': 'form-control my-3', 'placeholder': 'Website'})
    submit = SubmitField('Add', render_kw={'class': 'btn btn-primary mt-3'})
