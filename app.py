import psycopg

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Spencer Hawkins in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg.connect("postgresql://spencer_db_1vyf_user:hllDG7XjGhJb5TGJAkrBooEwq7ltwX10@dpg-d24lc4s9c44c73aet560-a/spencer_db_1vyf")
    conn.close()
    return "Database connection successful."