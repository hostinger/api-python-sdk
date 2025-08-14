# VPSV1DockerManagerContainerStatsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_percentage** | **float** | CPU usage in percentage | [optional] 
**memory_percentage** | **float** | Memory usage in percentage | [optional] 
**memory_used** | **float** | Used memory in bytes | [optional] 
**memory_total** | **float** | Total available memory in bytes | [optional] 
**net_in** | **int** | Inbound network traffic in bytes | [optional] 
**net_out** | **int** | Outbound network traffic in bytes | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_docker_manager_container_stats_resource import VPSV1DockerManagerContainerStatsResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1DockerManagerContainerStatsResource from a JSON string
vpsv1_docker_manager_container_stats_resource_instance = VPSV1DockerManagerContainerStatsResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1DockerManagerContainerStatsResource.to_json())

# convert the object into a dict
vpsv1_docker_manager_container_stats_resource_dict = vpsv1_docker_manager_container_stats_resource_instance.to_dict()
# create an instance of VPSV1DockerManagerContainerStatsResource from a dict
vpsv1_docker_manager_container_stats_resource_from_dict = VPSV1DockerManagerContainerStatsResource.from_dict(vpsv1_docker_manager_container_stats_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


