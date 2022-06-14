from typing import List

from methods.logger_config import logger

from boto3 import resource


def terminate_instance_with_id(id: List[str]) -> bool:
    """
    To terminate all avialable EC2 instanse in argument list
    Args:
        id (List[str]): List of EC2 instance ID

    Returns:
        Boolean : return True if instance succesfuly terminate else false

    """
    # return false if id is empty
    if len(id) <= 0:
        logger.warning("Nothing to delete, zero instance found.")
        return False
    else:
        ec2 = resource("ec2")  # aws client session of EC2 resource
        try:
            logger.debug("Deleting the EC2 instances in list : " + str(id))
            ec2.instances.filter(
                InstanceIds=id
            ).terminate()  # Terminate all instance with  in the list.
        except Exception as e:
            logger.error(e)
            return False
        else:
            return True
