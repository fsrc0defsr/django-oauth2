import random
import string
import base64
import hashlib

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))

code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')

print(code_verifier)
print(code_challenge)


client_id="web_id"
secret="web_secret"
credential = "{0}:{1}".format(client_id, secret)
print(base64.b64encode(credential.encode("utf-8")))