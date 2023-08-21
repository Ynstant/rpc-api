import re
from hashlib import sha256

import rpc_api
from pydantic import BaseSettings
from unidecode import unidecode


def cee_identity_key(cls, phone_number: str, last_name: str):
    def process_last_name(name: str):
        # Capitalize name
        capitalized_name = name.upper()

        # Normalize accented characters
        normalized_name = unidecode(capitalized_name)

        # Remove special characters
        name_without_special_characters = "".join(
            c if c.isalnum() else " " for c in normalized_name
        )

        # Remove duplicate spaces
        final_name = re.sub(" +", " ", name_without_special_characters)

        return final_name

    processed_last_name = process_last_name(last_name)

    return sha256(f"{phone_number}-{processed_last_name}".encode("utf-8")).hexdigest()
