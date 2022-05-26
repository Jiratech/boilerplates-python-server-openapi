import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error_message import ErrorMessage  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def create_user(user):  # noqa: E501
    """create user

    create any type of user # noqa: E501

    :param user: The user object to be created
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(user_id):  # noqa: E501
    """delete user

    Delete a user using an id # noqa: E501

    :param user_id: 
    :type user_id: str
    :type user_id: str

    :rtype: Union[ErrorMessage, Tuple[ErrorMessage, int], Tuple[ErrorMessage, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_by_id(user_id):  # noqa: E501
    """get one user

    Get one user using an id # noqa: E501

    :param user_id: 
    :type user_id: str
    :type user_id: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_users():  # noqa: E501
    """get all users

     # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'


def modify_user(user_id, user):  # noqa: E501
    """modify one user

    Modify a user using an id # noqa: E501

    :param user_id: 
    :type user_id: str
    :type user_id: str
    :param user: The user object to be created
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
