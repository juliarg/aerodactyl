from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
								Length, EqualTo)
from models import User

def name_exists(form, field):
	if User.select().where(User.username == field.data).exists():
		raise ValidationError('User with that name already exists.')


def email_exists(form, field):
	if User.select().where(User.email == field.data).exists():
		raise ValidationError('Email already exists.')

def is_university_email(form, field): 
	# domain = field.data.split('@') # domain is an array of two strings -- before and after the @ symbol
	if ("columbia.edu" not in field.data) and ("barnard.edu" not in field.data): 
		raise ValidationError('Please enter a valid @columbia.edu or @barnard.edu address.')


class RegisterForm(Form):
	username = StringField(
		'Username',
		validators = [
			DataRequired(),
			Regexp(
				r'^[a-zA-Z0-9_]+$',
				message = ("Username should be one word, letters, "
						"numbers, and underscores only")
			),
			name_exists
		])
	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(),
			email_exists,
			is_university_email
		])
	password = PasswordField(
		'Password', 
		validators=[
			DataRequired(),
			Length(min = 2),
			EqualTo('password2', message='Passwords must match')
		])
	password2 = PasswordField(
		'Confirm Password', 
		validators=[DataRequired()])
		

class NewListingForm(Form): 
	address = StringField(
		'Street address',
		validators = [
		DataRequired()
		]) # update this later 
	startDate = StringField(
		'Start Date',
		validators = [
		DataRequired()
		]) # update this later 
	endDate = StringField(
		'End Date',
		validators = [
		DataRequired()
		]) # update this later 
	


class LoginForm(Form):

	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
		