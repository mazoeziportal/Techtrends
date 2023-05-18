import sqlite3
import logging , sys

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
from logging import StreamHandler
from datetime import datetime


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection



# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)



@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:

        app.logger.error("Article with post id \"{}\" not found.".format(post_id))
        return render_template('404.html'),  404
         
    else:

        app.logger.info('Article "{title}" retrieved!'.format(title=post['title']))
#        app.logger.info('Article "{title}" retrieved!')
        return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
        app.logger.info('"About Us" page was retrieved!')
        return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            app.logger.info("A new article entitled:' + \"{}\" + title + \"{}\" + ' was created!".format(title))
            return redirect(url_for('index'))

    return render_template('create.html')
    # Define the health endpoint

@app.route('/healthz')
def status():
#    should_fail =True

    try:
#        get_db_connection.execute("SELECT 1")
        get_db_connection()
        should_fail = False
    except Exception as e:
#        return("Health check failed: {e}")


#    if should_fail:
        response = app.response_class(
            response=json.dumps({"result":"Error - Unhealthy"}),
            status=500,
            mimetype='application/json'
    ) 

    else:
        response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    return response   


@app.route('/metrics')
def metrics():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM posts')
    db_connection_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT (*) FROM Posts')
    post_count = cursor.fetchone()[0]

    cursor.close()
    connection.close()
    return {"db_connection_count": db_connection_count, "post_count": post_count}

    
    
# start the application on port 3111
if __name__ == "__main__":
    # set logger to handle STDOUT and STDERR 
    stdout_handler =  logging.StreamHandler(sys.stdout)
    stderr_handler =  logging.StreamHandler(sys.stderr)
    handlers = [stderr_handler, stdout_handler]
    logging.basicConfig(level=logging.DEBUG, handlers=handlers)    
    app.run(host='0.0.0.0', port='3111')
