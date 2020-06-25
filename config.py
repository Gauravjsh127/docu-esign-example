import os

# Docu sign rest api 
base_path = 'https://demo.docusign.net/restapi'

# Docusign developer portal
# Obtain an OAuth access token from https://developers.docusign.com/oauth-token-generator
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjY4MTg1ZmYxLTRlNTEtNGNlOS1hZjFjLTY4OTgxMjIwMzMxNyJ9.eyJUb2tlblR5cGUiOjUsIklzc3VlSW5zdGFudCI6MTU5MzA1MjgwNywiZXhwIjoxNTkzMDgxNjA3LCJVc2VySWQiOiIwNzViMzc2Yi1lYTk2LTQ5MTYtOWYzOC1lMjdkNzI2OGRmMGUiLCJzaXRlaWQiOjEsInNjcCI6WyJzaWduYXR1cmUiLCJjbGljay5tYW5hZ2UiLCJvcmdhbml6YXRpb25fcmVhZCIsInJvb21fZm9ybXMiLCJncm91cF9yZWFkIiwicGVybWlzc2lvbl9yZWFkIiwidXNlcl9yZWFkIiwidXNlcl93cml0ZSIsImFjY291bnRfcmVhZCIsImRvbWFpbl9yZWFkIiwiaWRlbnRpdHlfcHJvdmlkZXJfcmVhZCIsImR0ci5yb29tcy5yZWFkIiwiZHRyLnJvb21zLndyaXRlIiwiZHRyLmRvY3VtZW50cy5yZWFkIiwiZHRyLmRvY3VtZW50cy53cml0ZSIsImR0ci5wcm9maWxlLnJlYWQiLCJkdHIucHJvZmlsZS53cml0ZSIsImR0ci5jb21wYW55LnJlYWQiLCJkdHIuY29tcGFueS53cml0ZSJdLCJhdWQiOiJmMGYyN2YwZS04NTdkLTRhNzEtYTRkYS0zMmNlY2FlM2E5NzgiLCJhenAiOiJmMGYyN2YwZS04NTdkLTRhNzEtYTRkYS0zMmNlY2FlM2E5NzgiLCJpc3MiOiJodHRwczovL2FjY291bnQtZC5kb2N1c2lnbi5jb20vIiwic3ViIjoiMDc1YjM3NmItZWE5Ni00OTE2LTlmMzgtZTI3ZDcyNjhkZjBlIiwiYW1yIjpbImludGVyYWN0aXZlIl0sImF1dGhfdGltZSI6MTU5MzA1MjgwNSwicHdpZCI6IjI2ODQyMTUwLWM1ODMtNDU4Ny1hZGQ4LTgxNWI0YmNhZGI2MSJ9.19aHgvU_wxNdET6D2kIlSfonpNvcAdQK76Q_o1DUabU1CpfSfsbkIBmUiD9EGA0lWo5gQXT6OR66t3qzxxM6ahkWNepJ1_lT6gfcQedFtQ_o2X-OZr5NvZ1JBkFPcR3Pk8lT-oQwI4VDLY2KeNqlefVfBB_auZXNCEBg_SB4YkGaiVysSMWElkAXmT2lnODU8BDl-bqqI8oZO9u0sMc2y4N_YShJ4YYn6AscSWhmBHGKQlvCDixuHEEJ6HqyVUX7D6Zi78dJ08dUX-Co4AjS8MZyEtgJmqAleQEB4xOOqrAXR0Q4aEIYH0sFPdE91LVMnuhTDaQHM66SzizFJRnXAw'

account_id = '10848808'

# Recipient Information: BV logged in customer account 
signer_name = 'Bill'

signer_email = 'Bill@example.com'

# The document you wish to send. Path is relative to the root directory of this repo.
file_name_path = 'loan-form.pdf'

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