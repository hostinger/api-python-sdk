# VPSV1DockerManagerContainerResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique container identifier (short form of Docker container ID) | [optional] 
**name** | **str** | Container name as defined in docker-compose or assigned by Docker | [optional] 
**image** | **str** | Docker image name and tag used to create this container | [optional] 
**command** | **str** | Command being executed inside the container (may be truncated with ...) | [optional] 
**status** | **str** | Human-readable container status including uptime, exit codes, or error information | [optional] 
**state** | **str** | Programmatic container lifecycle state for automated processing | [optional] 
**ports** | [**List[VPSV1DockerManagerContainerPortResource]**](VPSV1DockerManagerContainerPortResource.md) | Array of [&#x60;VPS.V1.DockerManager.ContainerPortResource&#x60;](#model/vpsv1dockermanagercontainerportresource) | [optional] 
**stats** | [**VPSV1DockerManagerContainerStatsResource**](VPSV1DockerManagerContainerStatsResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_docker_manager_container_resource import VPSV1DockerManagerContainerResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1DockerManagerContainerResource from a JSON string
vpsv1_docker_manager_container_resource_instance = VPSV1DockerManagerContainerResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1DockerManagerContainerResource.to_json())

# convert the object into a dict
vpsv1_docker_manager_container_resource_dict = vpsv1_docker_manager_container_resource_instance.to_dict()
# create an instance of VPSV1DockerManagerContainerResource from a dict
vpsv1_docker_manager_container_resource_from_dict = VPSV1DockerManagerContainerResource.from_dict(vpsv1_docker_manager_container_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


