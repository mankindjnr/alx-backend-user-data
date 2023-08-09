#!/usr/bin/env python3
"""
creating a new authentication mechanism
"""
import uuid


from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """creating a new auth mechanism
    """
    user_id_by_session_id = {}
    session_user = user_id_by_session_id

    def create_session(self, user_id: str = None) -> str:
        """creates a session id for user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.session_user[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a user id based on session id
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None

        session_value = self.session_user.get(session_id)
        return session_value
