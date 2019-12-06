from identifier_tools.nic import verify_nic_checksum
from .utils import BadCodeType


def test_invalid_nic_format_nic_too_long():
    nic = '20170105N0001201'
    assert verify_nic_checksum(nic) is False


def test_invalid_nic_format_nic_too_short():
    nic = '20170105N00012'
    assert verify_nic_checksum(nic) is False


def test_invalid_nic_format_8_character_is_not_N():
    nic = '20170105A000120'
    assert verify_nic_checksum(nic) is False


def test_invalid_nic_format_first_part_not_numeric():
    nic = 'A0170105N000120'
    assert verify_nic_checksum(nic) is False

    nic = '2B170105N000120'
    assert verify_nic_checksum(nic) is False

    nic = '20C70105N000120'
    assert verify_nic_checksum(nic) is False

    nic = '201D0105N000120'
    assert verify_nic_checksum(nic) is False

    nic = '2017E105N000120'
    assert verify_nic_checksum(nic) is False

    nic = '20170F05N000120'
    assert verify_nic_checksum(nic) is False

    nic = '201701G5N000120'
    assert verify_nic_checksum(nic) is False

    nic = '2017010HN000120'
    assert verify_nic_checksum(nic) is False


def test_invalid_nic_format_second_part_not_numeric():
    nic = '20170105NA00120'
    assert verify_nic_checksum(nic) is False

    nic = '20170105N0B0120'
    assert verify_nic_checksum(nic) is False

    nic = '20170105N00C120'
    assert verify_nic_checksum(nic) is False

    nic = '20170105N000D20'
    assert verify_nic_checksum(nic) is False


def test_invalid_nic_format_second_part_not_greater_than_0():
    nic = '20170105N000020'
    assert verify_nic_checksum(nic) is False


def test_invalid_nic_format_checksum_not_numeric():
    nic = '20170105N0001A0'
    assert verify_nic_checksum(nic) is False

    nic = '20170105N00012B'
    assert verify_nic_checksum(nic) is False


def test_invalid_nic_format_first_part_is_not_date():
    nic = '20171505N000120'
    assert verify_nic_checksum(nic) is False

    nic = '20170135N000120'
    assert verify_nic_checksum(nic) is False

    nic = '00010105N000120'
    assert verify_nic_checksum(nic) is False


def test_invalid_input_nic_type():
    nic = ("20170401N000782", "19991011N004749")
    assert verify_nic_checksum(nic) is False

    nic = {
        "nic1": "20170401N000782",
        "nic2": "19991011N004749",
    }
    assert verify_nic_checksum(nic) is False

    nic = 201701052300120
    assert verify_nic_checksum(nic) is False

    nic = BadCodeType()
    assert verify_nic_checksum(nic) is False


def test_valid_nic():
    nic = "20170401N000782"
    assert verify_nic_checksum(nic) is True

    nic = "19991011N004749"
    assert verify_nic_checksum(nic) is True

    nic = "20170105N000120"
    assert verify_nic_checksum(nic) is True


def test_output_type_for_verify_nic_checksum():
    output = verify_nic_checksum('RANDOM0CODE')
    assert isinstance(output, bool)
    assert output is False

    output = verify_nic_checksum('20170105N000120')
    assert isinstance(output, bool)
    assert output is True
