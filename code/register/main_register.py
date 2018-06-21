from flask import Flask, render_template, request, Blueprint
from register import ContactForm

# app = Flask(__name__, template_folder='../../templates/register')
# app.secret_key = 'development key'

simple_page = Blueprint('simple_page', __name__, template_folder='../../templates/register')
@simple_page.route('/contact', methods=['GET', 'POST'])
# @app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            print("Not validated!!!")
        else:
            print("Validated!!!")
        name = request.form["password"]
        print(name)
    return render_template('register.html', form=form)
