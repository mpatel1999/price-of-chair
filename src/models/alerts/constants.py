import os

COLLECTION = "alerts"
ALERT_TIMEOUT = 10
URL= os.environ.get('MAILGUN_URL')
API_KEY=os.environ.get('MAILGUN_API_KEY')
FROM=os.environ.get('MAILGUN_FROM')
