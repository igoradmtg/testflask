from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def start_page():
    return "Start!"

@app.route('/index')
def index():
    return 'Index Page'
    
@app.route('/status')
def status():
    return "Сделано на flask"
    
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'
    
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/url')
def url(name=None):
    text = url_for('show_user_profile', username='Papa igor')+"<br>"
    text += url_for('status')
    return text 

if __name__ == "__main__":
    app.run()