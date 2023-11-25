from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators, SubmitField

class NetflixdataSearchForm(FlaskForm):
    title_type = StringField('Type', [validators.Length(min=1, max=10)])
    submit = SubmitField("Find")
class NetflixdataForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=500)])
    title_type = StringField('Type', [validators.Length(min=1, max=10)])
    netflix_id = StringField('Netflix Id', [validators.Length(min=1, max=10)])
    synopsis = StringField('Synopsis', [validators.Length(min=1, max=1000)])
    rating = DecimalField('Ratings', [validators.NumberRange(min=0)])
    year = DecimalField('Release Year', [validators.NumberRange(min=1900)])
    imdb_id = StringField('IMDB Id', [validators.Length(min=1, max=10)])
    title_date = StringField('Title Date (YYYY-MM-DD)', [validators.Regexp(r'^\d{4}-\d{2}-\d{2}$', message="Invalid date format")])
    submit = SubmitField("Save")