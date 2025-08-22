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
    except ():
        # TODO: add logger here
        print("")
        return ""
    
    rpc_string: str = f"Content-Length: :d\r\n\r\n:s".format(len(json_str), json_str)

    return json_str