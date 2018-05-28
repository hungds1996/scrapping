from xlrd import *
from pathlib import Path
import requests
# book = open_workbook(str(Path('contacts.xlsx').resolve()))
# sheet = book.sheet_by_index(0)

def send_complex_message():
    return requests.post(
        "https://api.mailgun.net/v3/www.designbold.com/messages",
        auth=("api", "key-f172a219158506101603136fa3b21db5"),
        files=[("attachment", ("1weivw.jpg", open("Files/1weivw.jpg","rb").read())),
               ("attachment", ("codecanyonCookies.txt", open("Files/codecanyonCookies.txt","rb").read()))],
        data={"from": "Dinh Sy Hung <hung.ds@designbold.com>",
              "to": "hungds1996@gmail.com",
            #   "cc": "baz@example.com",
            #   "bcc": "bar@example.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!",
              "html": '''<html><h3>Create email templates that look great everywhere.</h3>
<p>All templates are fully tested and mobile ready. Build it once and use it on any device. Build your new email template, and download it for free or upload it into a new or existing Campaign Monitor account.</p></html>'''})


send_complex_message()