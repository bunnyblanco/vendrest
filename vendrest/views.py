from flask import render_template
from .forms import LoginForm
from vendrest import app

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
#    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', 
            title='Home', 
            user={'name':'Bruce'},
            posts = [
            {
                'author': {'nickname': 'John'},
                'body': 'Beautiful day in Portland!'
            },
            {
                'author': {'nickname': 'Susan'},
                'body': 'The Avengers movie was so cool!'
            },
            {
                'author': {'nickname': 'Drew'},
                'body': "That's so two years ago."
            }
        ]
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
