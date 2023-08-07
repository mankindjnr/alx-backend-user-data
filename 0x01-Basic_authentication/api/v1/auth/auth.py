#!/usr/bin/env python3
"""
creating a class to manage the api auth
"""
from flask import request
from typing import TypeVar, List


class Auth():
    """class manging the api auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """handles the paths
        """
        if path:
            if path[-1:] != "/":
                path += "/"

        if path is None or path not in excluded_paths or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """the auth header method
        """
        if request is None:
            return None
        if not request.headers['Authorization']:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """the current user method
        """
        return None
