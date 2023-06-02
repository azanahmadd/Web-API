from flask import Flask, render_template, request, redirect, url_for,flash
import psycopg2 
import psycopg2.extras

app=Flask(__name__, template_folder='templates')
app.secret_key = "cairocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "cms_demo"
DB_USER = "postgres"
DB_PASS = "1122"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM custom_emp"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)
@app.route('/custom_employee', methods=['POST'])
def add_student():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        label = request.form['label']
        description = request.form['description']
        help_text = request.form['help_text']
        created_by = request.form['created_by']
        created_date = request.form['created_date']
        last_modified_date = request.form['last_modified_date']

        cur.execute("INSERT INTO custom_emp (name, label, description, help_text, created_by, created_date, last_modified_date) VALUES (%s,%s,%s,%s,%s,%s,%s)", (name, label, description, help_text, created_by, created_date, last_modified_date))
        conn.commit()
        flash('Student Added successfully')
        return redirect(url_for('Index'))
if __name__ == '__main__':
    app.run(debug=True)