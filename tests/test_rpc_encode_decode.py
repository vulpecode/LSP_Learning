"""Tests for rpc message enconding and decoding."""
from rpc.rpc_message import EncodeMessage

EncodingExample: dict[str, bool] = { "Testing": True }

class TestClass:
    """Test class."""
    Testing: bool = False

# === TEST_ENCODE_BAD_INPUT ===
def test_encode_message_correct() -> None:
    """Test encoding a message."""
    expected: str = "Content-Length: 17\r\n\r\n{\"Testing\": true}"
    actual: str = EncodeMessage(EncodingExample)

    assert (expected == actual)

# === TEST_ENCODE_BAD_INPUT ===
def test_encode_bad_input() -> None:
    """Test encoding a message with a nonsense input."""
    try:
        encoded_str: str = EncodeMessage(TestClass)
    except Exception:
        return

    assert (False)