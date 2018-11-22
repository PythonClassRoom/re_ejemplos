import re
heading  = r'<h1>TITLE</h1>'
re.match(r'<.*?>', heading).group()