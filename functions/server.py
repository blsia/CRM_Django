import os
import serverless_wsgi
from django.core.wsgi import get_wsgi_application

# Arahkan ke settings project dcrm
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcrm.settings')

application = get_wsgi_application()

def handler(event, context):
    # Pembersihan path URL agar Django tidak 404
    if 'path' in event:
        event['path'] = event['path'].replace('/.netlify/functions/server', '')
        if not event['path']:
            event['path'] = '/'

    return serverless_wsgi.handle_request(application, event, context)