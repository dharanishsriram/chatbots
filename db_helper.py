from fastapi import FastAPI, Request
import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="casedetails"
)
app = FastAPI()

# Database connection
def get_db_connection(order_id:int ):
    cursor = cnx.cursor(buffered=True)
    query= "Select court_name from court where case_no = %s"
    cursor.execute(query, (order_id,))
    result = cursor.fetchall()
    cursor.close()


    if result is not None:
        return result
    else:
        return None