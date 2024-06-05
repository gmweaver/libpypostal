"""Python bindings to libpostal parse_address."""
from enum import Enum
from typing import Dict, List, Optional, Tuple


class LibpostalAddressComponent(str, Enum):
    """Libpostal address component."""

    CATEGORY = "category"
    CITY = "city"
    CITY_DISTRICT = "city_district"
    COUNTRY = "country"
    COUNTRY_REGION = "country_region"
    ENTRANCE = "entrance"
    HOUSE = "house"
    HOUSE_NUMBER = "house_number"
    ISLAND = "island"
    LEVEL = "level"
    NEAR = "near"
    PO_BOX = "po_box"
    POSTCODE = "postcode"
    ROAD = "road"
    STAIRCASE = "staircase"
    STATE = "state"
    STATE_DISTRICT = "state_district"
    SUBURB = "suburb"
    UNIT = "unit"
    WORLD_REGION = "world_region"


def _parse_address(
    address: str, language: str, country_code: str
) -> List[Tuple[str, str]]:
    from libpypostal import _parser  # type: ignore # pylint: disable=no-name-in-module,import-outside-toplevel

    return _parser.parse_address(  # pylint: disable=c-extension-no-member
        address, language=language, country=country_code
    )


def parse_address(
    address: str, language: Optional[str] = None, country_code: Optional[str] = None
) -> Dict[str, List[str]]:
    """Parses address into components.

    Arguments:
        address: the address to parse.
        language: optional language code to help localize parsing.
        country_code: optional country code to help localize parsing.

    Returns:
        Dictionary of address components with format {<address component>: parsed value}.
        Generally, address component lists will only have one element, but there is a
        possibility of multiple matches. Address components not found in the input are
        set to empty lists.
    """
    address_component_tuples = _parse_address(
        address, language=language, country_code=country_code
    )

    parsed_address_components: Dict[str, List[str]] = {}

    for address_component_tuple in address_component_tuples:
        component_value, component_name = address_component_tuple

        if component_name in parsed_address_components:
            parsed_address_components[component_name].append(component_value)
        else:
            parsed_address_components[component_name] = [component_value]

    for libpostal_address_component in LibpostalAddressComponent:
        if libpostal_address_component.value not in parsed_address_components:
            parsed_address_components[libpostal_address_component.value] = []

    return parsed_address_components
