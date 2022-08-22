from dominate.svg import view
from flask import render_template, Flask
from flask import Flask
from flask_bootstrap import Bootstrap

view: Flask = Flask(__name__)
bootstrap = Bootstrap(view)

def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))
    for item in data:
        print(item.name())


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')



def end_view():
    print('Goodbye!')
