import re

email_address = "Please contact us at: xyz@datacamp.com"
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'erick@python-class.com', email_address)
print(new_email_address)