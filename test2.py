"""
To  get all instance from different region and terminate all instance with tag

"""


from get_all_instance_id import get_all_instance_id
from terminate_all_instance import terminate_all_instanse

# to get all instance with key tagged `poc` from all region
id = get_all_instance_id()

# to teminate all ec2 insatanse in list `id`
terminate_all_instanse(id)
