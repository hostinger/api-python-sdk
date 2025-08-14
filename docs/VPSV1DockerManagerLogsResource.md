# VPSV1DockerManagerLogsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | Name of the Docker Compose service that generated these log entries | [optional] 
**entries** | [**List[VPSV1DockerManagerLogEntryResource]**](VPSV1DockerManagerLogEntryResource.md) | Array of [&#x60;VPS.V1.DockerManager.LogEntryResource&#x60;](#model/vpsv1dockermanagerlogentryresource) | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_docker_manager_logs_resource import VPSV1DockerManagerLogsResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1DockerManagerLogsResource from a JSON string
vpsv1_docker_manager_logs_resource_instance = VPSV1DockerManagerLogsResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1DockerManagerLogsResource.to_json())

# convert the object into a dict
vpsv1_docker_manager_logs_resource_dict = vpsv1_docker_manager_logs_resource_instance.to_dict()
# create an instance of VPSV1DockerManagerLogsResource from a dict
vpsv1_docker_manager_logs_resource_from_dict = VPSV1DockerManagerLogsResource.from_dict(vpsv1_docker_manager_logs_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


