import os

# Docu sign rest api 
base_path = 'https://demo.docusign.net/restapi'

# Docusign developer portal
# Obtain an OAuth access token from https://developers.docusign.com/oauth-token-generator
access_token = ''
account_id = ''

# Recipient Information: BV logged in customer account 
signer_name = ''

signer_email = ''

# The document you wish to send. Path is relative to the root directory of this repo.
file_name_path = '*.pdf'

# The url of this web application
base_url = 'http://localhost:5000'

client_user_id = '123' # Used to indicate that the signer will use an embedded
                       # Signing Ceremony. Represents the signer's userId within
                       # your application.

authentication_method = 'None' # How is this application authenticating
                               # the signer? See the `authenticationMethod' definition
                               # https://developers.docusign.com/esign-rest-api/reference/Envelopes/EnvelopeViews/createRecipient

# Constants
APP_PATH = os.path.dirname(os.path.abspath(__file__))
