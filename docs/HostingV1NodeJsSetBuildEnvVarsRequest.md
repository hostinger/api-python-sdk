# HostingV1NodeJsSetBuildEnvVarsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_vars** | [**List[HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner]**](HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner.md) | Environment variables to set. This is the full desired set: any variable not in this list is deleted, and an empty array deletes every variable. | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_set_build_env_vars_request import HostingV1NodeJsSetBuildEnvVarsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsSetBuildEnvVarsRequest from a JSON string
hosting_v1_node_js_set_build_env_vars_request_instance = HostingV1NodeJsSetBuildEnvVarsRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsSetBuildEnvVarsRequest.to_json())

# convert the object into a dict
hosting_v1_node_js_set_build_env_vars_request_dict = hosting_v1_node_js_set_build_env_vars_request_instance.to_dict()
# create an instance of HostingV1NodeJsSetBuildEnvVarsRequest from a dict
hosting_v1_node_js_set_build_env_vars_request_from_dict = HostingV1NodeJsSetBuildEnvVarsRequest.from_dict(hosting_v1_node_js_set_build_env_vars_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


