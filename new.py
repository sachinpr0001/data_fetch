from flask import Flask,  render_template, jsonify
import pandas as pd
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# def connection():
engine = sqlalchemy.create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe", arraysize=1000)    # return dbcon

@app.route('/', methods= ['GET', 'POST'])
def main():

    try:
        sql_query = """SELECT * FROM sachin.student""";
        df = pd.read_sql(sql_query, engine)
        df.head()
        data_dict = df.to_dict('dict')
        # # print(data_dict)
        return jsonify(data_dict)
        # dfList = df.values.tolist()
        # return jsonify(dfList)
    except SQLAlchemyError as e:
        print(e)



if __name__ == '__main__':
	app.run(debug=True)

dbcon.close()