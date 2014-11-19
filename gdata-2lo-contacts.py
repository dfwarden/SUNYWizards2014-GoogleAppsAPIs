import gdata.gauth
import gdata.contacts.client

SOURCE_APP_NAME = 'anything-you-want'
CONSUMER_KEY = 'your-consumer-key'  # Generally, your GApps domain
CONSUMER_SECRET = 'your-consumer-secret'
requestor_id = 'gapps-user-email-address'  # User you wish to access

two_legged_oauth_token = gdata.gauth.TwoLeggedOAuthHmacToken(
    CONSUMER_KEY, CONSUMER_SECRET, requestor_id)

contacts_client = gdata.contacts.client.ContactsClient(source=SOURCE_APP_NAME)

contacts_client.auth_token = two_legged_oauth_token

contacts_list = contacts_client.GetContacts()
for entry in contacts_list.entry:
	print entry.title.text
