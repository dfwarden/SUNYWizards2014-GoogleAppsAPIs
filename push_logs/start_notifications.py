# System libraries
import time
from datetime import datetime, timedelta

# Google deps
import httplib2
import oauth2client.client
from apiclient import discovery, errors as apiclient_errors


# Read .p12 file, use it to authorize HTTP requests to Google API.
f = file('path-to-p12-file'rb')
serviceacct_key = f.read()
f.close()
credentials = oauth2client.client.SignedJwtAssertionCredentials(
    'service-account-email-address',
    serviceacct_key,
    scope = [
        'https://www.googleapis.com/auth/admin.reports.usage.readonly',
        'https://www.googleapis.com/auth/admin.reports.audit.readonly',
    ],
    sub = 'privileged-gapps-user-email-address')
http = httplib2.Http()
http = credentials.authorize(http)
reports = discovery.build('admin', 'reports_v1', http=http)

expire = datetime.now() + timedelta(hours=6)  # Max allowed by google
expire_unix = int(time.mktime(expire.timetuple()))
expire_milliseconds = expire_unix * 1000

reports.activities().watch(userKey='all', applicationName='admin', body=dict(type='web_hook', address='url-of-pushtolog.php', id='unique-admin-channel-name'.format(expire_unix), expiration=expire_milliseconds)).execute()
reports.activities().watch(userKey='all', applicationName='login', body=dict(type='web_hook', address='url-of-pushtolog.php', id='unique-login-channel-name'.format(expire_unix))).execute()
reports.activities().watch(userKey='all', applicationName='drive', body=dict(type='web_hook', address='url-of-pushtolog.php', id='unique-drive-channel-name'.format(expire_unix))).execute()
