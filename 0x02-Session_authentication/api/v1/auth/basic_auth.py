#!/usr/bin/env python3
"""
empty class that inherits from auth
"""
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import base64


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic auth class ineriting from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns te base64 part of auth header
        """
        if authorization_header is not None and isinstance(
                authorization_header, str):
            head = authorization_header.split(" ")

            auth = ""
            basic_1 = ""
            if len(head) == 2:
                basic_1 = head[0]
                auth = head[1]

                if basic_1 == "Basic":
                    basic = basic_1

                    header = authorization_header

                    if header is None or not isinstance(header, str) or len(
                            basic) == 0:
                        return None
                else:
                    return None
            else:
                return None

            return auth

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """return the decoded value of base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            decoded = decoded.decode('utf-8')
            return decoded
        except base64.binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from base64
        decode value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        else:
            decoded = decoded_base64_authorization_header

        if not isinstance(decoded, str):
            return (None, None)
        if ":" not in decoded:
            return (None, None)

        email, passw = decoded.split(":")
        return (email, passw)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the user instance based on his emaland pass
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})

        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the user instance
        for a request"""
        if request is None:
            return None

        auth_header = self.authorization_header(request)

        if auth_header is None:
            return None

        credentials = self.extract_base64_authorization_header(auth_header)

        if credentials is None:
            return None

        decoded_cred = self.decode_base64_authorization_header(credentials)

        if decoded_cred is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_cred)

        if user_email is None or user_pwd is None:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)

        return user
