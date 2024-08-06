#!/usr/bin/env python3
"""the Authentication module for API.
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """the Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """to Check if a path require authentication.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """to Get authorization header field frm the request.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """to Get the current user frm request.
        """
        return None
