from methods.logger_config import logger
from typing import List

from boto3 import client


def get_available_regions(service: str = "ec2") -> List[str]:
    """
    Create a iteratable list of region available in the specified service,
    If no argument EC2 is used as default.
    Warning : Only few service are supported.
    Args:
        service (str, optional):  Name of the AWS resource.
    Returns:
        List<str> : list of region.
    """
    regions = []  # To append all avialbale EC2 regions as a list
    try:
        clt = client(service)  # AWS deafult client Session
        response = clt.describe_regions()  # response of all available regions
    except Exception as error:
        logger.error(error)
    # Iterate each response and append region name to `regions` list.
    for item in response["Regions"]:
        regions.append(
            item["RegionName"]
        )  # append each region to the list `regions`
    return regions
