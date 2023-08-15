# Flask is micro framework

from flask import Flask,render_template


skills_app = Flask(__name__)

skills = [('Go',95),('html',20),('css',30),('php',25),('js',50),('nodejs',100),('Python',80)]

@skills_app.route('/')
def home_page():
    return render_template('home_page.html',page_title="Home Page",skills=skills,title="My Skills",description="This is my skills")

@skills_app.route('/about')
def about():
    return render_template('about.html',page_title="About Page")

@skills_app.route('/add')
def add_new():
    return render_template('add.html',page_title="Add")

if __name__ == '__main__':
    skills_app.run(debug=True)
