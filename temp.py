www = '12/02/1996'

from datetime import datetime
ppp = datetime.strptime(www, "%d/%m/%Y")

print(ppp)