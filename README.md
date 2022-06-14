# aws-ec2-instance-terminator

## To Setup up the script
```
python3 -m pip install -r requirement.txt

```
## To get all instanse id (defualt : Key = 'poc' , Value = '*' )
```
get_all_instance_id() # retuns list of instanse id
```
## You can change filter tag by passing optional argumnet
## eg : to get instance id with Name aws-test-server
```
get_all_instance_id(tag="Name",value="aws-test-server")

```

## To delete all instanse 
```
terminate_all_instanse(id) # `id` is the list of instance.
```
