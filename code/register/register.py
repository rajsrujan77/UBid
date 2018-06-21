from flask_wtf import FlaskForm
import wtforms
# from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators


class ContactForm(FlaskForm):
    name = wtforms.StringField("Name Of Student", [validators.DataRequired("Please enter your name.")])
    Gender = wtforms.RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = wtforms.TextAreaField("Address")

    email = wtforms.StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter your email address.")])

    # Age = IntegerField("age")
    # language = SelectField('Languages', choices=[('cpp', 'C++'),
    #                                              ('py', 'Python')])
    password = wtforms.PasswordField(
        'Password',
        [
            wtforms.validators.Length(min=2),
            wtforms.validators.DataRequired(),
            wtforms.validators.EqualTo('confirm', message='Passwords must match')
        ])
    confirm = wtforms.PasswordField('Repeat password')
    submit = wtforms.SubmitField("Send")
