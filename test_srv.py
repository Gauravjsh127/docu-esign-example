import os
import ast
import tempfile
from pathlib import Path

from flask import send_from_directory, current_app as app
from flask import jsonify
from flask import Flask, request, redirect
from docusign_srv import DocuSignSignatureService
from flask import send_file

docu_sign_signature_service = DocuSignSignatureService()

def embedded_signing_ceremony():
    print('dsdsds')
    print(tempfile.gettempdir()) # prints the current temporary directory
    docu_sign_signature_service.envelope_setup()
    return docu_sign_signature_service.create_recipient_view()


def get_envelope_id():
    return docu_sign_signature_service.docu_envelope_handler.envelope_id

def list_docs_in_envelope():
    docu_sign_signature_service.list_documents_in_envelope()

def download_doc():
    return docu_sign_signature_service.download_signed_document()

# test-app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        return redirect(embedded_signing_ceremony(), code=302)
    else:
        return '''
            <html lang="en"><body><form action="{url}" method="post">
            <input type="submit" value="Sign the document!"
                style="width:13em;height:2em;background:#1f32bb;color:white;font:bold 1.5em arial;margin: 3em;"/>
            </form></body>
        '''.format(url=request.url)
@app.route('/dsreturn', methods=['GET'])
def dsreturn():
    return '''
        <html lang="en"><body><p>The signing ceremony was completed with
          status {event}</p>
          <p>This page can also implement post-signing processing.</p></body>
    '''.format(event=request.args.get('event'))


@app.route('/envelopeId', methods=['GET'])
def envelopeId():
    envelope_id = get_envelope_id()
    return  str(envelope_id), 200

@app.route('/listdocsId', methods=['GET'])
def listdocsId():
    list_docs_in_envelope()
    return  'Success', 200

@app.route('/downloaddocs', methods=['GET'])
def downloaddocs():
    doc = download_doc()
    doc_name = Path(doc).name
    print(doc_name)
    return send_from_directory(tempfile.gettempdir(), doc_name)

app.run()