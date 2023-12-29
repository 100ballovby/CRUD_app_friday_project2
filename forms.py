from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired
from models import Company


class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    company_id = SelectField('Company', coerce=int)
    submit = SubmitField('Add')

    def __init__(self):
        super().__init__()
        companies = []
        for company in Company.query.all():
            companies.append((company.id, company.name))
        self.company_id.choices = companies


class CompanyForm(FlaskForm):
    name = StringField('Company Name', validators=[DataRequired()])
    website = StringField('Website', validators=[DataRequired()])

