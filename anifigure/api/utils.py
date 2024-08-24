import jwt


from dataclasses import dataclass
from pathlib import Path


from anifigure.settings import BASE_DIR


@dataclass
class JWTHelper:
    private_key_path: str = (BASE_DIR / "certs" / "jwt-private.pem").read_text()
    public_key_path: str = (BASE_DIR / "certs" / "jwt-public.pem").read_text()
    algorithm: str = "RS256"


jwt_helper = JWTHelper()


def encode_token(
    payload: dict,
    algorithm: str,
    private_key: str = jwt_helper.private_key_path,
):
    encoded = jwt.encode(
        payload=payload,
        key=private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_token(
    token: str | bytes,
    algorithm: str,
    public_key: str = jwt_helper.public_key_path,
):
    decoded = jwt.decode(
        jwt=token,
        key=public_key,
        algorithms=[algorithm],
    )
    return decoded
