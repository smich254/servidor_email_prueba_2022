import smtplib
from email.message import EmailMessage

def email(de, contras, para, asunto, cuerpo):
    # Variable creada para guardar el asunto del
    
    # Quien envia el email
    sender_email_address = de

    # Contraseña de la aplicacion
    email_password = contras
    
    # Quien recive el email
    receiver_email_address = para

    # correo electronico
    email_subject = asunto
    
    # El proveedor de email en uso
    email_smtp = "smtp.gmail.com"


    # Create an email message object
    message = EmailMessage()

    # Configure email headers
    message['Subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address

    # Set email body text
    message.set_content(cuerpo)

    # Set smtp server and port
    server = smtplib.SMTP(email_smtp, '587')

    # Identify this client to the SMTP server
    server.ehlo()

    # Secure the SMTP connection
    server.starttls()

    # Login to email account
    server.login(sender_email_address, email_password)

    # Send email
    server.send_message(message)

    # Close connection to server 
    server.quit()