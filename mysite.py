
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cycle.db'
db = SQLAlchemy(app)


class Organization(db.Model):                            #База данных колонки
    id = db.Column(db.Integer, primary_key=True) #уникальный номер
    organization_name = db.Column(db.String(100)) #Название
    address = db.Column(db.String(100))            #Адресс
    type_organization = db.Column(db.String(50))    #Тип заведения(кафе, магазин итд)
    opening_hours = db.Column(db.String(20))         #Время работы
    description_promotion = db.Column(db.String(500)) #Описание акции


@app.route("/")
def index():
    organizations = Organization.query.all()
    return render_template('index.html', organizations=organizations, search_name="")


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_name = request.form.get('NameOrganization', '')

    if search_name.strip() == "":
        organizations = Organization.query.all()
    else:
        organizations = Organization.query.filter(Organization.organization_name.ilike(f'%{search_name}%')).all()

    return render_template('index.html', organizations=organizations, search_name=search_name)


if __name__ == '__main__':
    app.run(debug=True)
