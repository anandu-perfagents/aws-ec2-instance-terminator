from typing import List

from methods.get_available_regions import get_available_regions
from methods.get_instance_with_tag import get_instance_with_tag


def get_all_instance_id(tag: str = "poc", value: str = "*") -> List:
    """
    Create a iteratable list of EC2 insatnce id from all avialble region.
    Args:
        tag (str, optional):  An EC2 instance tag `Name`  Defaults to "poc".
        value (str, optional): An EC2 instance tag `Key` Deafults to "".
    Returns:
        List<str> : list of region.
    """
    ids = []  # To store all instance ID from different region.
    regions = get_available_regions("ec2")
    for region in regions:
        ids.extend(
            get_instance_with_tag(tag=tag, value=value, region_name=region)
        )
    return ids
