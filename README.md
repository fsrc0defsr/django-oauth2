# django-oauth2
Django Oauth2 Tutorial

User(superuser) 

login: admin, 
password:admin


http://127.0.0.1:8000/o/applications/register/

Applications:

1) Authorization_grant_type = Authorization Code
    
    Name:app
    Client id: id_app
    Client secret: secret_app
    Client type: Confidentional
    Authorization grant type: Authorization code
    Redirect uris:http://localhost:8000/noexist/callback
    Algorithm:HMAC with SHA-2 256

    code_verifier:2JHGKCVCTUFQCLBN3S4M1U17Z732XR63O8UI56XG011J3ISXAWBC3007E1Y51Z2S8NN28R0P7FRRY1W2IKKSTNYPXQ0CZELJN3JJX3COFZCC7X4T093

    code_challenge: 7G4guHj7Kqqb9oTob7EzT33jbhUDrrGl0zk14XCl-2I

    {
        "access_token": "c6lHT8tyjY4oHF9rcY9R5gUlwlTesP",
        "expires_in": 36000,
        "token_type": "Bearer",
        "scope": "read write",
        "refresh_token": "SDBadsGUpjlZ9q301XOSg3hrGmrt61"
    }

2) Authorization_grant_type = Client Credentials

    Name:web
    Client id: web_id
    Client secret: web_secret
    Client type: Confidentional
    Authorization grant type: client-credentials
    
    CREDENTIAL: d2ViX2lkOndlYl9zZWNyZXQ=

    {
        "access_token": "oZxCYnWTBAF6BNOXFXhWDCZIQZbuRf",
        "expires_in": 36000,
        "token_type": "Bearer",
        "scope": "read write"
    }