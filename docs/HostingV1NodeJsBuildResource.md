# HostingV1NodeJsBuildResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Build UUID | [optional] 
**state** | **str** | Build state | [optional] 
**options** | [**HostingV1NodeJsBuildOptionsResource**](HostingV1NodeJsBuildOptionsResource.md) |  | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_build_resource import HostingV1NodeJsBuildResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsBuildResource from a JSON string
hosting_v1_node_js_build_resource_instance = HostingV1NodeJsBuildResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsBuildResource.to_json())

# convert the object into a dict
hosting_v1_node_js_build_resource_dict = hosting_v1_node_js_build_resource_instance.to_dict()
# create an instance of HostingV1NodeJsBuildResource from a dict
hosting_v1_node_js_build_resource_from_dict = HostingV1NodeJsBuildResource.from_dict(hosting_v1_node_js_build_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


