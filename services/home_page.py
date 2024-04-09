from flask import Blueprint, render_template


blueprint = Blueprint(
    'home_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/')
def home_page():
    return render_template('home.html', title='Home')
