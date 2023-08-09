# REAST API AUTHENTICATION

## BasicAuth (Basic Authentication)
Unlike the classic session token authentication where after the first time the client sends their username and password and the server allocates a session token to that user that every time the clients communicates with the server, the token is used.

With REST API  which has no state, the classic session token method won't work, there are several ways for authentication in REST API, one of them is BasicAuth.

With BasicAuth, the client sends their username and password with every request, the server checks the username and password and if they are correct, the server responds with the requested data.
This is stored in the Authorization header of the request, the value of the header is the word Basic followed by a space and a base64-encoded string username:password.

## -------------------------------------------------------------------------------------------
The server decodes the base64-encoded string and checks the username and password.

username:password -> base64 -> dXNlcm5hbWU6cGFzc3dvcmQ= -> base64 decode -> username:password

Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ= -> base64 decode -> username:password

Always send the Authorization header over HTTPS, otherwise, the username and password can be intercepted by a third party.
## -------------------------------------------------------------------------------------------

# Better Solution
## DigestAuth (Digest Authentication)
DigestAuth is a better solution than BasicAuth, it uses a hash function to hash the username, password, and other information, and then sends the hash value to the server, the server checks the hash value and if it is correct, the server responds with the requested data.

## Asymmetric cryptography
Asymmetric cryptography is a cryptographic system that uses pairs of keys: public keys, which may be disseminated widely, and private keys, which are known only to the owner. The generation of such keys depends on cryptographic algorithms based on mathematical problems to produce one-way functions. Effective security requires keeping the private key private; the public key can be openly distributed without compromising security.

## 0Auth (OAuth)
OAuth is an open standard for access delegation, commonly used as a way for Internet users to grant websites or applications access to their information on other websites but without giving them the passwords. This mechanism is used by companies such as Amazon, Google, Facebook, Microsoft, and Twitter to permit the users to share information about their accounts with third-party applications or websites.

## JWT (JSON Web Token)
JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.

## ======================================================================================
# Base64 In python

Base64 is a group of similar binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation. The term Base64 originates from a specific MIME content transfer encoding.

### example
```python
import base64

# encode string
message = "Hello world"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

# decode string
base64_message = 'SGVsbG8gd29ybGQ='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)
```

## ======================================================================================
# HTTP HEADER AUTHORIZATION

The HTTP Authorization request header contains the credentials to authenticate a user agent with a server, usually, but not necessarily, after the server has responded with a __401 Unauthorized__ status and the __WWW-Authenticate__ header.
