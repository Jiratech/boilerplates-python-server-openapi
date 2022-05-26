#!/usr/bin/env python3
import connexion
from flask_cors import CORS
import sys
sys.path.append('openapi')
from openapi_server import encoder

def main():
    app = connexion.App(__name__, specification_dir='./')
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi/openapi_server/openapi/openapi.yaml',
                arguments={'title': 'Learning boilerplate'},
                pythonic_params=True)

    app.run(host='0.0.0.0', port=3000, debug=True)

def apikey_auth(token, required_scopes):
    info = TOKEN_DB.get(token, None)

    if not info:
        raise OAuthProblem('Invalid token')

    return info

if __name__ == '__main__':
    main()
