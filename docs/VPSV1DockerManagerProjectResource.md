# VPSV1DockerManagerProjectResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Docker Compose project name (derived from directory name or compose file) | [optional] 
**status** | **str** | Raw output from docker compose ps command showing service count and states | [optional] 
**state** | **str** | Derived project state parsed from the raw docker compose status | [optional] 
**path** | **str** | Full filesystem path to the docker-compose.yml file | [optional] 
**containers** | [**List[VPSV1DockerManagerContainerResource]**](VPSV1DockerManagerContainerResource.md) | Array of [&#x60;VPS.V1.DockerManager.ContainerResource&#x60;](#model/vpsv1dockermanagercontainerresource) | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_docker_manager_project_resource import VPSV1DockerManagerProjectResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1DockerManagerProjectResource from a JSON string
vpsv1_docker_manager_project_resource_instance = VPSV1DockerManagerProjectResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1DockerManagerProjectResource.to_json())

# convert the object into a dict
vpsv1_docker_manager_project_resource_dict = vpsv1_docker_manager_project_resource_instance.to_dict()
# create an instance of VPSV1DockerManagerProjectResource from a dict
vpsv1_docker_manager_project_resource_from_dict = VPSV1DockerManagerProjectResource.from_dict(vpsv1_docker_manager_project_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


