# VPSV1DockerManagerContentResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Contents of docker-compose file | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_docker_manager_content_resource import VPSV1DockerManagerContentResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1DockerManagerContentResource from a JSON string
vpsv1_docker_manager_content_resource_instance = VPSV1DockerManagerContentResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1DockerManagerContentResource.to_json())

# convert the object into a dict
vpsv1_docker_manager_content_resource_dict = vpsv1_docker_manager_content_resource_instance.to_dict()
# create an instance of VPSV1DockerManagerContentResource from a dict
vpsv1_docker_manager_content_resource_from_dict = VPSV1DockerManagerContentResource.from_dict(vpsv1_docker_manager_content_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


