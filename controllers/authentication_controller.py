import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.jwt_authentication_request import JwtAuthenticationRequest  # noqa: E501
from openapi_server.models.jwt_authentication_response import JwtAuthenticationResponse  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def login(jwt_authentication_request):  # noqa: E501
    """authenticate user

     # noqa: E501

    :param jwt_authentication_request: Authentication request
    :type jwt_authentication_request: dict | bytes

    :rtype: Union[JwtAuthenticationResponse, Tuple[JwtAuthenticationResponse, int], Tuple[JwtAuthenticationResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jwt_authentication_request = JwtAuthenticationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def refresh():  # noqa: E501
    """get new access token

    send refresh token to get new access token # noqa: E501


    :rtype: Union[JwtAuthenticationResponse, Tuple[JwtAuthenticationResponse, int], Tuple[JwtAuthenticationResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def register(user):  # noqa: E501
    """register

     # noqa: E501

    :param user: The user object to be created
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
