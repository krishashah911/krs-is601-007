from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators, SubmitField
from wtforms import ValidationError

def validate_not_empty(form, field):
    if not field.data or field.data.strip() == '':
        raise ValidationError('This field is required.')

def validate_numeric(form, field):
    if not field.data.isdigit():
        raise ValidationError('This field must be numeric.')
class NetflixdataSearchForm(FlaskForm):
    title_type = StringField('Type', [validators.Length(min=1, max=10)])
    submit = SubmitField("Find")
class NetflixdataForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=500)])
    title_type = StringField('Type', [validators.Length(min=1, max=10)])
    netflix_id = StringField('Netflix Id', [validators.Length(min=8, max=10)])
    synopsis = StringField('Synopsis', [validators.Length(min=1, max=1000)])
    year = StringField('Release Year (YYYY)', [validators.Length(min=4)])
    #imdb_id = StringField('IMDB Id', [validators.Length(min=1, max=10)])
    title_date = StringField('Title Date (YYYY-MM-DD)', [validators.Regexp(r'^\d{4}-\d{2}-\d{2}$', message="Invalid date format")])
    submit = SubmitField("Save")

class RatingsdataForm(FlaskForm):
    ratings = DecimalField('Ratings', [validators.NumberRange(min=0, max=5)])
    heading = StringField('Heading', [validators.Length(min=1, max=50)])
    comments = StringField('Comments') 
    submit = SubmitField("Save")   