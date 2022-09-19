from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaaaa'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign-in')
def signin():
    return render_template('signin.html')

@app.route('/sign-up')
def signup():
    return render_template("signup.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/signup", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html',form=form)


@app.route("/signin", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('signin.html', form=form)
if __name__ == "__main__":
    app.run('0.0.0.0',port=8080,debug=False)