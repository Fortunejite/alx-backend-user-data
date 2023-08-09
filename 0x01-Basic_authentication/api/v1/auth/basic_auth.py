from api.v1.auth.auth import Auth
"""Basic auth module"""


class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if not authorization_header:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.split()[0] == 'Basic':
            return None
        return authorization_header[6:]