from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from past.builtins import raw_input
import json
import view
from model import Person

st_web: Flask = Flask(__name__)
bootstrap = Bootstrap(st_web)
model = []


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


@st_web.route("/")
def start_web():
    result = list()
    with open('db.json') as json_file:
        data = json.load(json_file)
        for p in data['employees']:
            person = Person(p['ID'], p['first_name'], p['last_name'])
            result.append(person)
    return render_template("people.html", value=result)

@st_web.route('/person_delete/<string:id>')
def person_delete(ID):
    for person in model:
        if person.id_person == ID:
            model.remove(person)

    return redirect('/people')

@st_web.route('/perupdate', methods=['POST'])
def perupdate():
    
    model.remove('ID')
    show_all()
    
    return render_template('person_detail.html', value=show_all())


@st_web.route('/person_update/<string:id>', methods=['GET'])
def person_update(id, get=None):
    data = 0
    data = get.all()
    

    return render_template('person_update.html', data=show_all())



# @st_web.rounte('/people')
# def people():
#   return render_template('people.html')

def start():
    view.start_view()
    input = raw_input()
    if input == 'y':
        return show_all()
    else:
        return view.end_view()


if __name__ == "__main__":
    # running controller function
    start()
    st_web.run()
