from json import dumps, JSONDecodeError
from typing import Any


def EncodeMessage(msg: Any) -> str:
    """Encodes message for LSP message.

    Args:
        msg (any): The message to be encoded.

    Returns:
        string: The encoded message.
    """
    json_str: str = ""

    try:
        json_str = dumps(msg)
    except JSONDecodeError as e:
        # TODO: add logger here
        print("Error: {0}".format(e))
        # TODO: add real exception here
        raise Exception("")
    
    rpc_string: str = "Content-Length: {}\r\n\r\n{}".format(len(json_str), json_str)

    return rpc_string