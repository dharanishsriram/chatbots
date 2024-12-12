from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
import db_helper

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.post("/")
async def handle_post(request: Request):
    # Parse JSON payload
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']


    if intent == "case_details":
        return case_track(parameters)

def case_track(parameters: dict):
     order_id =parameters['number']
     cs=db_helper.get_db_connection(order_id)

     if cs:
         fulfillment_text=f"The case details for case_id : {order_id} is {cs}"
     else:
        fulfillment_text=f"The case details for case_id : {order_id} is None"

     return JSONResponse(content={"fulfillmentText": fulfillment_text})
