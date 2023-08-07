#!/usr/bin/env python3
"""
creating a class to manage the api auth
"""
from flask import request



class Auth():
    """class manging the api auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """handles the paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """the auth header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """the current user method
        """
        return None
