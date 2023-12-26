from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)


# Creating a connection object.
host = 'mysql-service'
user = 'root'
password = 'root'
database = 'mydb'

# Establishing the connection 
connection = pymysql.connect(host=host, user=user, password=password, database=database)


@app.route('/')
def hello():
    return 'Your Flask Server Running'

@app.route('/getitems', methods=['GET'])
def get_items():
    try:
        item = []
	# Create a cursor object for interacting with the MySQL database
        cur = connection.cursor()

        # Execute an SQL query to select all items from the 'items' table
        cur.execute('SELECT * FROM mytable')

        # Fetch all the data (items) from the executed query
        data = cur.fetchall()

        # Close the database cursor
        cur.close()

        # Create a list of dictionaries to structure the retrieved items
        items = [{'id': item[0], 'username': item[1], 'phone': item[2],  'email': item[3]} for item in data]

        # Create a response dictionary for a successful operation
        response = {
            'error': False,
            'message': 'Items Fetched Successfully',
            'data': data
        }

        # Return a JSON response with HTTP status code 200 (OK)
        return jsonify(response), 200
    except Exception as e:
        # Handle any exceptions that may occur during the process
        response = {
            'error': False,
            'message': f'Error Occurred: {e}',
            'data': None
        }

        # Return a JSON response with HTTP status code 500 (Internal Server Error)
        return jsonify(response), 500

    cur.close()
    connection.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
