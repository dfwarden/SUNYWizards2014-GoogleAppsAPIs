import httplib2
import oauth2client.client
from apiclient.discovery import build

# At least on Mac OS, you need pycrypto or pyopenssl.
# pycrypto can only read PEM, pyOpenSSL can do pkcs12.
# pyOpenSSL requires a compiler to pip install.
f = file('path-to-key', 'r')
serviceacct_key = f.read()
f.close()
credentials = oauth2client.client.SignedJwtAssertionCredentials(
    'service-account-email-address',
    serviceacct_key,
    scope = [
        'https://www.googleapis.com/auth/admin.directory.user.readonly'
    ],
    sub = 'privileged-gapps-user-email-address'
    )
http = credentials.authorize(httplib2.Http())
directory = build('admin', 'directory_v1', http=http)
print directory.users().get(userKey='any-gapps-user-email-address').execute()
