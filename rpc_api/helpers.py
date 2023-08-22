import re
from hashlib import sha256

from rpc_api.models.identity import Identity
from rpc_api.models.identity_travel_pass import IdentityTravelPass
from typing import Optional
from unidecode import unidecode


def identity_key(phone_number: str, last_name: str) -> str:
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


def user_identity(
    phone: str,
    last_name: str,
    operator_user_id: str,
    travel_pass: Optional[IdentityTravelPass] = None,
    over_18: Optional[bool] = None,
) -> Identity:
    return Identity(
        identity_key=identity_key(phone_number=phone, last_name=last_name),
        operator_user_id=operator_user_id,
        travel_pass=travel_pass,
        over_18=over_18,
    )
