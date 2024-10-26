from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL, Optional, ValidationError
from flask_wtf.file import FileAllowed
import re

def custom_url_validator(form, field):
    url_pattern = re.compile(r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?$')
    if not url_pattern.match(field.data):
        raise ValidationError('Invalid URL. Please enter a valid URL (e.g., https://www.example.com).')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    profile_picture = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Update Profile')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class WishlistItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_url = StringField('Item URL', validators=[Optional(), custom_url_validator])
    price_range = SelectField('Price Range', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], validators=[DataRequired()])
    public = BooleanField('Let others see on Shopping List')
    notes = TextAreaField('Notes', validators=[Optional(), Length(max=500)])
    submit = SubmitField('Add to Wishlist')

class EditWishlistItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_url = StringField('Item URL', validators=[Optional(), custom_url_validator])
    price_range = SelectField('Price Range', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], validators=[DataRequired()])
    public = BooleanField('Let others see on Shopping List')
    notes = TextAreaField('Notes', validators=[Optional(), Length(max=500)])
    submit = SubmitField('Update Item')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Add Comment')
