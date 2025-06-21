from flask import Flask, render_template, request, redirect, url_for
import pymysql as sql


app = Flask(__name__)

def db_connect():
    conn = sql.connect(host='localhost', port=3306, user='root', password='', database='grass')
    cur = conn.cursor()
    return conn, cur

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/academic-qualification')
def academic_qualification():
    return render_template('academic_qualification.html')

@app.route('/professional-experience')
def professional_experience():
    return render_template('professional_experience.html')

@app.route('/skills-interests')
def skills_interests():
    return render_template('skills_interests.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/training-certifications')
def training_certifications():
    return render_template('training_certifications.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')


@app.route('/aftersubmit/', methods =['GET', 'POST'])
def after_submit():
    if request.method == 'GET':
        return redirect(url_for('contact'))
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        db, cursor = db_connect()
        cmd = f"select * from contact where email = '{email}'"
        data =  cursor.execute(cmd)
        if data:
            msg = 'email already exists...'
            return render_template('contact.html', data = msg)
        else:
            cmd = f"insert into contact values('{name}', '{email}', {phone}, '{message}')"
            cursor.execute(cmd)
            db.commit()
            db.close()
            msg = 'Details are sent successfully... :)'
            return render_template('contact.html', data = msg)
   
@app.route('/resume/')
def resume():
    return render_template('resume.html')
         
    
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))  
    app.run(host='0.0.0.0', port=port, debug=True)