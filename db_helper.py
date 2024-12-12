from fastapi import FastAPI, Request
import mysql.connector


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="casedetails"
)
app = FastAPI()

# Database connection
def get_db_connection(order_id:int ):
    cursor = cnx.cursor()
    query= "Select court_name from court where case_no = %s"
    cursor.execute(query, (order_id,))
    result = cursor.fetchone()

    cursor.close()
    cnx.close()

    if result is not None:
        return result[0]
    else:
        return None