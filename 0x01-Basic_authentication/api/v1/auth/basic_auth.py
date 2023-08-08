#!/usr/bin/env python3
"""
empty class that inherits from auth
"""
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
