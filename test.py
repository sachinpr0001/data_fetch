from flask import Flask,  render_template, jsonify
import pandas as pd
import cx_Oracle
import pymysql

# app = Flask(__name__)

# def connection():
dbcon = cx_Oracle.connect('system/admin@localhost:1521/xe')
    # return dbcon

# @app.route('/', methods= ['GET', 'POST'])
# def main():

try:
    SQL_Query = pd.read_sql_query(
    '''SELECT * FROM sachin.student''', dbcon)
    df = pd.DataFrame(SQL_Query, columns=['roll_no', 'name', 'age', 'gender', 'city'])
    df.head()

#     data_dict = df.to_dict('dict')

    # # print(data_dict)
#     return jsonify(data_dict)
    # dfList = df.values.tolist()
    # return jsonify(dfList)
except:
    print("Error: unable to convert the data")



# if __name__ == '__main__':
# 	app.run(debug=True)

dbcon.close()