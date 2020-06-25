import os
import base64
from datetime import datetime, timedelta

from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Tabs, Recipients, Document, RecipientViewRequest

from config import *


class DocuSignSignatureService:
    def __init__(self):
        self.api_client = ApiClient()
        self.api_client.host = base_path
        self.api_client.set_default_header("Authorization", "Bearer " + access_token)

    def envelope_setup(self):
        """
        Setup/crete the envelope
            - Provide document model
            - Create signer recipient model
            - Setup envelope defination
            - Make the api call via SDK
        """
        with open(os.path.join(APP_PATH, file_name_path), "rb") as file:
            content_bytes = file.read()
        base64_file_content = base64.b64encode(content_bytes).decode('ascii')

        # Create the document model
        document = Document( # create the DocuSign document object 
            document_base64 = base64_file_content, 
            name = 'Example document', # can be different from actual file name
            file_extension = 'pdf', # many different document types are accepted
            document_id = 1 # a label used to reference the doc
        )

        # Create the signer recipient model 
        signer = Signer( # The signer
            email = signer_email, name = signer_name, recipient_id = "1", routing_order = "1",
            client_user_id = client_user_id, # Setting the client_user_id marks the signer as embedded
        )

        # Create a sign_here tab (field on the document)
        sign_here = SignHere( # DocuSign SignHere field/tab
            document_id = '1', page_number = '1', recipient_id = '1', tab_label = 'SignHereTab',
            x_position = '195', y_position = '147')

        # Add the tabs model (including the sign_here tab) to the signer
        signer.tabs = Tabs(sign_here_tabs = [sign_here]) # The Tabs object wants arrays of the different field/tab types

        # Next, create the top level envelope definition and populate it.
        self.envelope_definition = EnvelopeDefinition(
            email_subject = "Please sign this document sent from the BVAULT",
            documents = [document], # The order in the docs array determines the order in the envelope
            recipients = Recipients(signers = [signer]), # The Recipients object wants arrays for each recipient type
            status = "sent" # requests that the envelope be created and sent.
        )
        self.envelope_api = EnvelopesApi(self.api_client)

        self.docu_envelope_handler = self.envelope_api.create_envelope(account_id, envelope_definition=self.envelope_definition)

    def create_recipient_view(self):
        """
        Create recipient view
        """
        recipient_view_request = RecipientViewRequest(
            authentication_method = authentication_method, client_user_id = client_user_id,
            recipient_id = '1', return_url = base_url + '/dsreturn',
            user_name = signer_name, email = signer_email
        )

        self.docu_recipient_handler = self.envelope_api.create_recipient_view(account_id, self.docu_envelope_handler.envelope_id,
            recipient_view_request = recipient_view_request)

        # Step 4. The Recipient View URL (the Signing Ceremony URL) has been received.
        #         Redirect the user's browser to it.
        return self.docu_recipient_handler.url

    def list_documents_in_envelope(self):
        """
        Lists all documents in the envelope
        """
        self.docu_envelope_handler = self.envelope_api.list_documents(account_id, self.docu_envelope_handler.envelope_id)
        print(self.docu_envelope_handler)

    def download_signed_document(self):
        """
        Download the signed document by the customer from docu sign
        """
        document_id = '1' # Always 1 as in the model we have only 1 document
        envelope_id = self.docu_envelope_handler.envelope_id
        temp_file = self.envelope_api.get_document(account_id, document_id, envelope_id)
        print('temp_file')
        print(temp_file)
        print('temp_file downloaded')
        return temp_file