from enum import IntEnum
from typing import Any, Tuple, AnyStr, Callable


BS: int

Model: IntEnum


def aes_encrypt(key: AnyStr, plain: str, /, mode: Model = ...) -> Tuple[str, str]: ...


def aes_decrypt(
  key: AnyStr, value: str, /, 
  mode: Model = ..., nonce_or_iv: str = ...) -> str: ...


def get_sha1prng_key(key: str) -> str: ...


def aes_ecb_encrypt(key: AnyStr, plaintext: str) -> str: ...
def aes_ecb_decrypt(key: AnyStr, ciphertext: str) -> str: ...
def aes_cfb_encrypt(key: AnyStr, plaintext: str) -> Tuple[str, str]: ...
def aes_cfb_decrypt(key: AnyStr, ciphertext: str, /, iv: str) -> str: ...

def to_base64(hexstring: str) -> str: ...
def sha3sum(plaintext: str) -> str: ...