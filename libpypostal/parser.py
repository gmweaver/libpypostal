"""Python bindings to libpostal parse_address."""
from enum import Enum
from typing import Dict, List, Literal, Optional, Tuple, Union, overload


class AddressComponent(str, Enum):
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
    address: str, language: Optional[str] = None, country_code: Optional[str] = None
) -> List[Tuple[str, str]]:
    from libpypostal import _parser  # type: ignore # pylint: disable=no-name-in-module,import-outside-toplevel

    return _parser.parse_address(  # pylint: disable=c-extension-no-member
        address, language=language, country=country_code
    )


@overload
def parse_address(
    address: str,
    merge_multiple_matches: Literal[True],
    language: Optional[str] = None,
    country_code: Optional[str] = None,
) -> Dict[AddressComponent, str]:
    ...


@overload
def parse_address(
    address: str,
    merge_multiple_matches: Literal[False],
    language: Optional[str] = None,
    country_code: Optional[str] = None,
) -> Dict[AddressComponent, List[str]]:
    ...


def parse_address(
    address: str,
    merge_multiple_matches: bool,
    language: Optional[str] = None,
    country_code: Optional[str] = None,
) -> Union[Dict[AddressComponent, str], Dict[AddressComponent, List[str]]]:
    """Parses address into components.

    Arguments:
        address: the address to parse.
        merge_multiple_matches: indicates whether to merge multiple matches for a component.
        language: optional language code to help localize parsing.
        country_code: optional country code to help localize parsing.

    Returns:
        If merge_multiple_matches is set to False, the return type is Dict[str, List[str]]. If
        set to True, a simple concatenation of matches is done with a single space and the return
        type is Dict[str, str]. Given multiple matches are rare, many use cases may prefer the
        simple concatenation, but there is still the ability to use custom logic to handle multiple
        matches if needed.
    """
    address_component_tuples = _parse_address(
        address, language=language, country_code=country_code
    )

    parsed_address_components: Dict[AddressComponent, List[str]] = {}
    for component_value, component_name in address_component_tuples:
        if component_name in parsed_address_components:
            parsed_address_components[AddressComponent(component_name)].append(
                component_value
            )
        else:
            parsed_address_components[AddressComponent(component_name)] = [
                component_value
            ]

    if merge_multiple_matches:
        return {
            component_name: " ".join(component_value)
            for component_name, component_value in parsed_address_components.items()
        }

    return parsed_address_components
