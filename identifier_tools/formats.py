import re

from . import formats_constants as constants
from .mappers import territory_to_parent_mapper


def verify_identifier_format(identifier: str, identifier_type: str, allow_unknown_type: bool = True) -> bool:
    """
    Validate identifier format, based on its type
    """
    if not isinstance(identifier, str) or not isinstance(identifier_type, str):
        result = False
    elif identifier_type in constants.IDENTIFIER_FORMATS:
        result = bool(re.match(constants.IDENTIFIER_FORMATS[identifier_type], identifier))
    elif allow_unknown_type:
        result = bool(re.match("[^+,]{1,50}", identifier))
    else:
        result = False

    return result


def verify_national_identifier_country(country_code: str, national_id_type: str) -> bool:
    """
    Checks if the national identifier type belongs to the specified country.

    :param country_code: String, containing ISO2 format country code.
    :param national_id_type: String, containing national identifier type.
    :return:
        True if identifier type belongs to the country.
        False if identifier type DOESN'T belong to the country.
    """
    if country_code != "MC":  # Monaco doesn't have identifiers which starts with FR (parent)
        country_iso2_mapped = territory_to_parent_mapper(country_code)
    else:
        country_iso2_mapped = country_code

    country_national_codes = [x for x in constants.ECB_NATIONAL_IDENTIFIERS if x.startswith(country_iso2_mapped)]

    if national_id_type.startswith(country_iso2_mapped) \
            or national_id_type == "BIC" \
            or (
                national_id_type.startswith("GEN") and (len(country_national_codes) == 0 or country_iso2_mapped
                                                        in constants.GEN_IDENTIFIER_COUNTRY_EXCEPTIONS)):
        return True
    else:
        return False
