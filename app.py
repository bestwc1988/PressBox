###############################
###App Name:    PressBox
###Author:      Hai Lang
###Creation:    16 Sep 2012
###Last Update: 16 Sep 2012
###############################

###Library Imports
from flask import Flask, request, render_template, Markup, url_for, redirect, session, abort
#Flask -> Web Micro Framework
#request -> Handles HTTP Requests
#render_template -> Template Rendering
#Markup -> Disable HTML Esacpe
#url_for -> URL Generator 
#session -> Session Management
#abort -> Abort Request to Error Pages. [404, 400..]
###############################

###App Configuration
__HOST = '0.0.0.0'
__DEBUG = True
###############################

###App Initialization
app = Flask(__name__)
###############################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<path:post_path>/')
def show_post(post_path = None):
    return 'Post %s' % post_path

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'hailang'\
            and request.form['password'] == '123':
                ###User login successfully. Set session and redirect back to main page
                session['logged_user'] = request.form['username']
                return redirect(url_for('index'))
    else:
        error = 'Invalid Username or Password!'
    ###The following code is executed if the request method was GET
    ###Or the credentials were invalid
    return render_template('login.html', error = error)

@app.route('/logout')
def logout():
    session.pop('logged_user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host = __HOST, debug = __DEBUG)
