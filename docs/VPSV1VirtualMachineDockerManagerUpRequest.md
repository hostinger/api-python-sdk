# VPSV1VirtualMachineDockerManagerUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** | Docker Compose project name using alphanumeric characters, dashes, and underscores only | 
**content** | **str** | URL pointing to docker-compose.yaml file, Github repository or raw YAML content of the compose file | 
**environment** | **str** | Project environment variables | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_virtual_machine_docker_manager_up_request import VPSV1VirtualMachineDockerManagerUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineDockerManagerUpRequest from a JSON string
vpsv1_virtual_machine_docker_manager_up_request_instance = VPSV1VirtualMachineDockerManagerUpRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineDockerManagerUpRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_docker_manager_up_request_dict = vpsv1_virtual_machine_docker_manager_up_request_instance.to_dict()
# create an instance of VPSV1VirtualMachineDockerManagerUpRequest from a dict
vpsv1_virtual_machine_docker_manager_up_request_from_dict = VPSV1VirtualMachineDockerManagerUpRequest.from_dict(vpsv1_virtual_machine_docker_manager_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


