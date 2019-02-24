from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('관리자명', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('E-메일', validators=[DataRequired(), Email()])

    password = PasswordField('비밀번호', validators=[DataRequired()])
    confirm_password = PasswordField('비밀번호 확인', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('관리자등록')

class LoginForm(FlaskForm):
    email = StringField('E-메일', validators=[DataRequired(), Email()])

    password = PasswordField('비밀번호', validators=[DataRequired()])
    remember = BooleanField('메일저장')
    submit = SubmitField('로그인')