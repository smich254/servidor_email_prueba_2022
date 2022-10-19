from fastapi import FastAPI, Response
from starlette.status import HTTP_204_NO_CONTENT
from lib.email import email
from schema.email import Email

app = FastAPI()


@app.get("/")
def root():
    return {"Hola": "Esta es nuestra API de mensajeria instantanea!"}

@app.post("/sentemail")
def sent_email(item_email: Email):
    email(item_email.de, item_email.contras, item_email.para, item_email.asunto, item_email.cuerpo)
    return Response(status_code=204)