from flask import Flask, json, render_template
import pandas as pd
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import time
app = Flask(__name__)
start_time = datetime.now()
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

time.sleep(1)
end_time = datetime.now()
diff = end_time - start_time
time_taken = diff.seconds + diff.microseconds/1000000
print('The time taken to fetch data from Oracle and send it to Flask is ', time_taken , 'seconds.')

if __name__ == '__main__':
	app.run(debug=True)

