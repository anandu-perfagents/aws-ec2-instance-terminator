from methods.terminate_instance_with_id import terminate_instance_with_id

from methods.logger_config import logger
from typing import List


def terminate_all_instanse(id: List[str]) -> bool:
    """
    To terminate all instance in the id.

    Args :
        id (Lis[str], *) : List of EC2 instance id.
    return :
    """
    if terminate_instance_with_id(id):
        logger.debug(f"{len(id)} instance deleted Successfully ✅")
        return True
    else:
        logger.warning("Instance deletion failed ❌")
        return False
