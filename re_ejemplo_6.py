import re

email_address = "Please contact us at: support@datacamp.com, xyz@datacamp.com blablablabal erick@erick.com"

#'addresses' is a list that stores all the possible match
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
for address in addresses:
    print(address)