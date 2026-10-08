"""
pip install Pillow cryptography
"""

"""Compare ECB and CBC pixel encryption. Requires Pillow and cryptography."""

import argparse
import os
from pathlib import Path

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("ecb", "cbc"), default="ecb")
    args = parser.parse_args()
    source = Path(__file__).with_name("wojak.png")
    destination = source.with_name(f"wojak-{args.mode}.png")

    with Image.open(source) as image:
        image = image.convert("RGB")
        pixels = image.tobytes()
        size = image.size

    # Fixed public key for comparison, not secure storage.
    key = bytes.fromhex("00112233445566778899aabbccddeeff")
    block_size = algorithms.AES.block_size // 8
    padded = pixels + b"\x00" * (-len(pixels) % block_size)
    metadata = PngInfo()
    if args.mode == "cbc":
        iv = os.urandom(block_size)
        mode = modes.CBC(iv)
        metadata.add_text("iv", iv.hex())
    else:
        mode = modes.ECB()
    encryptor = Cipher(algorithms.AES(key), mode).encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()

    # Truncate only for display; a partial final block would not be recoverable.
    encrypted_image = Image.frombytes("RGB", size, ciphertext[:len(pixels)])
    encrypted_image.save(destination, pnginfo=metadata)
    print(f"Saved {destination} ({size[0]} x {size[1]})")


if __name__ == "__main__":
    main()
