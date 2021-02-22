from typing import Optional

import jwt
from jwt import ExpiredSignatureError
from starlette.authentication import AuthenticationBackend, AuthCredentials, SimpleUser
from starlette.requests import Request

from pasteme import config
from pasteme.models.user import UserModel, user_model_manager


class SecurityBackend(AuthenticationBackend):
    """
    starlette 的用户验证，
    简陋，真的简陋...

    """
    async def authenticate(self, request: Request):
        global payload
        if 'Authorization' not in request.headers:
            return

        # 就直接从请求头拿 jwt token ...
        authorization = request.headers.get('Authorization')
        token = authorization.split(' ')[1]
        try:
            payload = jwt.decode(token, algorithms=['HS256'], key=config.JWT_SECRET)
        except ExpiredSignatureError:
            pass

        username = payload.get('username')
        user: Optional[UserModel] = await user_model_manager.get_or_none(username=username)

        if user:
            return AuthCredentials(['user']), user
