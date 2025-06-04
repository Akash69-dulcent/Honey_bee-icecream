from flask import Flask, render_template, request
import MySQLdb

# Create connection object
mysql = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",  # XAMPP default
    db="akash"
)

def create_app():
    app = Flask(__name__)
    register_resources(app)
    return app

def register_resources(app):
    # Homepage
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")
            mobile = request.form.get("contact")
            message = request.form.get("mesage")  # Fixed typo in variable name
            
            if name and email:
                try:
                    cur = mysql.cursor()
                    # Fixed SQL query - added missing parameter and fixed syntax
                    cur.execute("INSERT INTO user (name, email, contact, mesage) VALUES (%s, %s, %s, %s)", 
                              (name, email, mobile, message))
                    mysql.commit()
                    cur.close()
                except MySQLdb.Error as e:
                    mysql.rollback()
                    print(f"Error inserting data: {e}")
        
        # Fetch all users
        cur = mysql.cursor()
        cur.execute("SELECT * FROM user")
        users = cur.fetchall()
        cur.close()
        return render_template('contact.html', users=users)  # Fixed variable name

    @app.route('/info', methods=['GET'])
    def info():
        return render_template('info.html')

if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 8000, debug=True)