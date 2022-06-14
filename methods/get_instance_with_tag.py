from typing import List
from methods.logger_config import logger

from boto3 import resource


def get_instance_with_tag(
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
    # to filter instance based on the Key and value
    filters = [{"Name": "tag:" + tag, "Values": [value]}]
    instance_id: List[str] = []  # To store EC2 instance id in the given region
    try:

        # To set default region as AWS client if region argument  is not
        # specified
        ec2 = (
            resource("ec2", region_name=region_name)
            if region_name != ""
            else resource("ec2")
        )
        # To store list of EC2 instance object based on the filter.
        instances = ec2.instances.filter(Filters=filters)
    except Exception as e:
        logger.error(e)
        return []
    else:
        # Create a iteratable instance id from instance object.
        instance_id = [instance.id for instance in instances]
        logger.debug(
            str(len(instance_id))
            + f" EC2 intances found in the  \
{(region_name if region_name != '' else 'default region ')}\
  tag `{tag}` "
        )
        return instance_id
