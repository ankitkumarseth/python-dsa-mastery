"""
LeetCode 271: Encode and Decode Strings (Medium)

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
"""
import pytest

class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        pass

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        pass

# ==========================
# PYTEST SUITE
# ==========================
def test_standard():
    codec = Codec()
    strs = ["Hello", "World"]
    assert codec.decode(codec.encode(strs)) == strs
    assert codec.decode(codec.encode(["lint","code","love","you"])) == ["lint","code","love","you"]

def test_edge_cases():
    codec = Codec()
    assert codec.decode(codec.encode([""])) == [""]
    assert codec.decode(codec.encode([])) == []
    # Contains potential delimiter characters
    assert codec.decode(codec.encode(["#", "##", "123#"])) == ["#", "##", "123#"]

def test_tle_large_input():
    codec = Codec()
    strs = ["a" * 1000] * 1000
    assert codec.decode(codec.encode(strs)) == strs
