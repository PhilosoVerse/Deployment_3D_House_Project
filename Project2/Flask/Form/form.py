from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

#this will show a folder on the html file for user input,
#so the backend can use that code to request the lambert-72 coordinates

#TODO validator for streetnumbers and addresses & city names? https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2
#TODO give error message if field has wrong input  https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3
class PlotForm(FlaskForm):
    #username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    #email = StringField('Email',validators=[DataRequired(),Email()])
    street = StringField('Street',validators=[])
    streetNumber = StringField('StreetNumber',validators=[])
    postCode = StringField('PostCode', validators=[])
    city = StringField('City', validators=[])

    submit = SubmitField('Plot House',validators=[])
