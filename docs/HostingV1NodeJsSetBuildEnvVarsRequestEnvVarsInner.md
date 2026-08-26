# HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Environment variable name. Must start with an uppercase letter or underscore, followed by uppercase letters, digits or underscores. | 
**value** | **str** | Environment variable value. | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_set_build_env_vars_request_env_vars_inner import HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner from a JSON string
hosting_v1_node_js_set_build_env_vars_request_env_vars_inner_instance = HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner.to_json())

# convert the object into a dict
hosting_v1_node_js_set_build_env_vars_request_env_vars_inner_dict = hosting_v1_node_js_set_build_env_vars_request_env_vars_inner_instance.to_dict()
# create an instance of HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner from a dict
hosting_v1_node_js_set_build_env_vars_request_env_vars_inner_from_dict = HostingV1NodeJsSetBuildEnvVarsRequestEnvVarsInner.from_dict(hosting_v1_node_js_set_build_env_vars_request_env_vars_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


