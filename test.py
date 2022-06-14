"""
Script to test all modules.
"""

from typing import List
from logging import Logger

import logging
import sys

from boto3 import resource, client

# Creates a logger file to keep track of EC2 instance activity
logger: Logger = logging.getLogger("POC SCRIPT")
file_handler = logging.FileHandler("poc_logger.log")
console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s : %(message)s"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def getInstaceWithTag(
    tag: str = "poc", value: str = "*", region_name: str = ""
) -> List[str]:
    """
    Get the available list of EC2 instance_id in the  default  region with tag
    `poc` and `key`

    Args:
        tag (str, optional):  An EC2 instance tag `Name`  Defaults to "poc".
        value (str, optional): An EC2 instance tag `Key` Deafults to "".
        region_nmae (str , optional) : Region name where EC2 instanse located

    Returns:
        List<str> : List of ec2 instance id.
    """
    # logger.debug(
    #     "Checking EC2 instances  with Tag `" + tag + "` and Key : `" + value)

    filters = [{"Name": "tag:" + tag, "Values": [value]}]
    instance_id: List[str] = []
    try:
        ec2 = (
            resource("ec2", region_name=region_name)
            if region_name != ""
            else resource("ec2")
        )

        instances = ec2.instances.filter(Filters=filters)
    except Exception as e:
        logger.error(e)
        return []
    else:
        instance_id = [instance.id for instance in instances]
        logger.debug(
            str(len(instance_id))
            + f" EC2 intances found in the  \
{(region_name if region_name != '' else 'default region ')}\
  tag `{tag}` "
        )
        return instance_id


# TODO Create a class
def terminateInstance(id: List[str]) -> bool:
    """
    To terminate all avialable EC2 instanse in id

    Args:
        id (List[str]): List of EC2 instance ID

    Returns:
        Boolean
    """
    if len(id) <= 0:
        logger.warning("Nothing to delete, no ec2 instance found ")
        return False
    else:
        ec2 = resource("ec2")
        try:
            logger.debug("Deleting the EC2 instances in list : " + str(id))
            ec2.instances.filter(InstanceIds=id).terminate()
        except Exception as e:
            logger.error(e)
            return False
        else:
            return True


# TODO convert list to generator
def get_available_regions(service: str) -> List[str]:

    regions = []
    clt = client(service)
    response = clt.describe_regions()
    for item in response["Regions"]:
        regions.append(item["RegionName"])
    return regions


# TODO not authorized to perfom this
def get_all_resources():
    clt = client("resourcegroupstaggingapi")
    print(clt.get_resources(ResourceTypeFilters=["ec2:instance"]))


if __name__ == "__main__":
    logger.debug("POC script started")
    ids = []
    regions = get_available_regions("ec2")
    for region in regions:
        ids.extend(getInstaceWithTag(region_name=region))
    logger.debug(
        f"{len(ids)} instance deleted Successfully ✅"
    ) if terminateInstance(ids) else logger.warning(
        "Instance deletion failed ❌"
    )
