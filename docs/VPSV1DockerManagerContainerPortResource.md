# VPSV1DockerManagerContainerPortResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Port mapping type - published (accessible from host), exposed (only internal), or range variants | [optional] 
**protocol** | **str** | Network protocol used for communication | [optional] 
**host_ip** | **str** | IP address on host where port is bound (null for exposed-only ports) | [optional] 
**host_port** | **int** | Port number on host machine (null for exposed-only or range ports) | [optional] 
**container_port** | **int** | Port number inside container (null for range ports) | [optional] 
**host_port_start** | **int** | Starting port number in host port range (null for single ports) | [optional] 
**host_port_end** | **int** | Ending port number in host port range (null for single ports) | [optional] 
**container_port_start** | **int** | Starting port number in container port range (null for single ports) | [optional] 
**container_port_end** | **int** | Ending port number in container port range (null for single ports) | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_docker_manager_container_port_resource import VPSV1DockerManagerContainerPortResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1DockerManagerContainerPortResource from a JSON string
vpsv1_docker_manager_container_port_resource_instance = VPSV1DockerManagerContainerPortResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1DockerManagerContainerPortResource.to_json())

# convert the object into a dict
vpsv1_docker_manager_container_port_resource_dict = vpsv1_docker_manager_container_port_resource_instance.to_dict()
# create an instance of VPSV1DockerManagerContainerPortResource from a dict
vpsv1_docker_manager_container_port_resource_from_dict = VPSV1DockerManagerContainerPortResource.from_dict(vpsv1_docker_manager_container_port_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


