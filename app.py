from flask import Flask, json, render_template
import pandas as pd
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from time import perf_counter()
app = Flask(__name__)
start_time = perf_counter()
engine = sqlalchemy.create_engine("oracle://system:admin@localhost:1521/xe", arraysize=1000)    # return dbcon

@app.route('/')
def main():

    try:
        sql_query = """SELECT * FROM sachin.student"""
        df = pd.read_sql(sql_query, engine)
        df.head()
        data_dict = df.to_dict('dict')
        response = app.response_class(
        response=json.dumps(data_dict),
        status=200,
        mimetype='application/json'
        )
        return response
    except SQLAlchemyError as e:
        print(e)
def hello(number : int) -> int:
    return number

print('The time taken to fetch data from Oracle and send it to Flask is ', perf_counter() - start_time , 'seconds.')

if __name__ == '__main__':
	app.run(debug=True)
