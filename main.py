'''
Mani Ajorloo
'''
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# def send_html_email(sender, recipient, subject, html_content, text_content):
    
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = recipient
#     # if text_content else "This is the plain text version of the email."
#     part1 = MIMEText(text_content , 'plain')
#     part2 = MIMEText(html_content, 'html')
    
#     msg.attach(part1)
#     msg.attach(part2)
    
    
#     with smtplib.SMTP('smtp.gmail.com', 587) as s:
#         s.starttls()
#         s.login(sender, 'password') # your Password
#         s.send_message(msg)
#         print("Email sent successfully!") 

# html_content = """
# <html>
#     <body">
#         <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" width="500"/>
#         <h1 style="color:blue;">This is the HTML Body of the Email
#         <p>This email contains both plain text and HTML versions.</p>
#         <p>Winter is coming!</p>
#         </h1>
#     </body>
# </html>
# """
# text_content = """
# This is the plain text version of the email :   \n
# Winter is coming!
# Here's a list :
# - Item 1
# - Item 2 
# - Item 3
# """
# send_html_email(
#     "Origin@gmail.com",
#     "Destination@gmail.com",
#     "HTML Email Test",
#     html_content,
#     text_content,
# )


import yagmail

yag = yagmail.SMTP(
    "Your@gmail.com",  # your Gmail
    "password"           # your Password
)

contents = [
    "This is the body, and here is just text",
    "You can even send HTML with yagmail",
    "<h1>This is an HTML Header</h1><p>This is a paragraph in HTML.</p>",
    "You can also attach files",
    ]

attachments = [
    'download.jpg'
]

yag.send(
    to="Destafafcastion@gmail.com",
    subject='subject',
    contents=contents,
    attachments=attachments
) 









