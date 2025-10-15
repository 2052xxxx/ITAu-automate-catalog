#!/usr/bin/env python3


import datetime
import os
import sys
import reports
import emails

def report_title():
    today = datetime.date.today()
    formatted_date = today.strftime("%B %d, %Y")
    title = "Processed Update on {}".format(formatted_date)
    return title

def report_paragraph():
    file_path = os.path.expanduser('~') + '/supplier-data/descriptions/'
    fruits = []

    for text in os.listdir(file_path):
        if '.txt' in text:
            with open(file_path + text, "r") as file:
                content = file.readlines()
                name = content[0].strip()
                weight = content[1].strip()
                fruits.append(
                    "name: {}<br/>weight: {}".format(name, weight)
                    )
    
    return "<br/><br/>".join(fruits)

def main(argv):
    title = report_title()
    paragraph = report_paragraph()
    attachment = "/tmp/processed.pdf"

    print(title)
    print(paragraph)

    # TODO: turn this into a PDF report
    reports.generate_report(attachment, 
                    title, 
                    paragraph)
    
    # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)

# reports.generate_report ("/tmp/report.pdf", 
#                  "A Complete Inventory of My Fruit", 
#                  "The Mercedes-Benz E-Class (2009) generated the most revenue: $22749529.02</br>The Acura Integra (1995) had the most sales: 1192</br>The most popular year was 2007 with 21534 sales.", 
#                  table_data)

# sender = "automation@example.com"
# receiver = "{}@example.com".format(os.environ.get('USER'))
# subject = "List of Fruits"
# body = "Hi\n\nI'm sending an attachment with all my fruit."

# message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
# emails.send(message)