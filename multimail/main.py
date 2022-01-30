
        filename = row[0] + '.pdf'
        with open(filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        email.encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="manuscrito_a_evaluar.pdf"')
        msg.attach(part)
