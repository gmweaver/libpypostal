# pylint: disable=missing-module-docstring,missing-function-docstring,
from unittest.mock import MagicMock, patch

from libpypostal import parser


@patch("libpypostal.parser._parse_address")
def test_parse_address_single_match_each_component(
    mock__parser_parse_address: MagicMock,
) -> None:
    test_address = "123 Bayes Way, Beverly Hills, CA 90210 US"
    mock__parser_parse_address.return_value = [
        ("123", "house_number"),
        ("bayes way", "road"),
        ("beverly hills", "city"),
        ("ca", "state"),
        ("90210", "postcode"),
        ("us", "country"),
    ]
    expected = {
        "house_number": ["123"],
        "road": ["bayes way"],
        "city": ["beverly hills"],
        "state": ["ca"],
        "postcode": ["90210"],
        "country": ["us"],
    }

    actual = parser.parse_address(test_address, merge_multiple_matches=False)

    assert actual == expected
    mock__parser_parse_address.assert_called_once_with(
        test_address, language=None, country_code=None
    )


@patch("libpypostal.parser._parse_address")
def test_parse_address_single_match_each_component_merged_matches(
    mock__parser_parse_address: MagicMock,
) -> None:
    test_address = "123 Bayes Way, Beverly Hills, CA 90210 US"
    mock__parser_parse_address.return_value = [
        ("123", "house_number"),
        ("bayes way", "road"),
        ("beverly hills", "city"),
        ("ca", "state"),
        ("90210", "postcode"),
        ("us", "country"),
    ]
    expected = {
        "house_number": "123",
        "road": "bayes way",
        "city": "beverly hills",
        "state": "ca",
        "postcode": "90210",
        "country": "us",
    }

    actual = parser.parse_address(test_address, merge_multiple_matches=True)

    assert actual == expected
    mock__parser_parse_address.assert_called_once_with(
        test_address, language=None, country_code=None
    )


@patch("libpypostal.parser._parse_address")
def test_parse_address_multiple_matches_for_component(
    mock__parser_parse_address: MagicMock,
) -> None:
    test_address = "123 Bayes Way, Beverly Hills, CA 90210 California US"
    mock__parser_parse_address.return_value = [
        ("123", "house_number"),
        ("bayes way", "road"),
        ("beverly hills", "city"),
        ("ca", "state"),
        ("california", "state"),
        ("90210", "postcode"),
        ("us", "country"),
    ]
    expected = {
        "house_number": ["123"],
        "road": ["bayes way"],
        "city": ["beverly hills"],
        "state": ["ca", "california"],
        "postcode": ["90210"],
        "country": ["us"],
    }

    actual = parser.parse_address(test_address, merge_multiple_matches=False)

    assert actual == expected
    mock__parser_parse_address.assert_called_once_with(
        test_address, language=None, country_code=None
    )


@patch("libpypostal.parser._parse_address")
def test_parse_address_multiple_matches_for_component_merge_matches(
    mock__parser_parse_address: MagicMock,
) -> None:
    test_address = "123 Bayes Way, Beverly Hills, CA 90210 California US"
    mock__parser_parse_address.return_value = [
        ("123", "house_number"),
        ("bayes way", "road"),
        ("beverly hills", "city"),
        ("ca", "state"),
        ("california", "state"),
        ("90210", "postcode"),
        ("us", "country"),
    ]
    expected = {
        "house_number": "123",
        "road": "bayes way",
        "city": "beverly hills",
        "state": "ca california",
        "postcode": "90210",
        "country": "us",
    }

    actual = parser.parse_address(test_address, merge_multiple_matches=True)

    assert actual == expected
    mock__parser_parse_address.assert_called_once_with(
        test_address, language=None, country_code=None
    )
