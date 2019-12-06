import datetime
from .iso import verify_iso7064_code
from .formats import verify_identifier_format


def verify_nic_checksum(nic: str) -> bool:
    """
    Verify the validity of NIČ checksum

    NIČ is unique identifier issued by NBS for foreign (non-SK) subjects.
    """
    if not isinstance(nic, str):
        return False
    else:
        nic = nic.strip()

    if not verify_identifier_format(nic, 'NIC'):
        return False

    if not int(nic[9:13]) > 0:
        return False

    try:
        datetime.date(year=int(nic[:4]), month=int(nic[4:6]), day=int(nic[6:8]))
    except ValueError:
        return False

    return verify_iso7064_code(nic)
