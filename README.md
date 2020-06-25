# docu-esign-example
These quick start examples provide straight-forward code examples for quickly trying the DocuSign eSignature API with the Python SDK.

These examples do not include authentication. Instead, use the DocuSign DevCenter's OAuth token generator to create an access token.

## Installation

The examples were tested with Python v3.6.
The SDK itself works with Python v2.7 or later.

Download or clone this repository. Then:

````
cd qs-python
pip3 install docusign_esign pendulum flask
````

### Configure the example's settings
Each quick start example is a standalone file. You will configure
each of the example files:

 * **Access token:** Use the [OAuth Token Generator](https://developers.docusign.com/oauth-token-generator).
   To use the token generator, you'll need a
   [free DocuSign Developer's account.](https://go.docusign.com/o/sandbox/)

   Each access token lasts 8 hours, you will need to repeat this process
   when the token expires. You can use the same access token for
   multiple examples.

 * **Account Id:** After logging into the [DocuSign Sandbox system](https://demo.docusign.net),
   you can copy your Account Id from the dropdown menu by your name. See the figure:

   ![Figure](https://raw.githubusercontent.com/docusign/qs-python/master/documentation/account_id.png)
 * **Signer name and email:** Remember to try the DocuSign signing ceremony using both a mobile phone and a regular
   email client.
python test_srv.py
