# HostingV1NodeJsEnvVarResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Environment variable name | [optional] 
**value** | **str** | Always the literal string ********. Real values cannot be read back through this API. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_env_var_resource import HostingV1NodeJsEnvVarResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsEnvVarResource from a JSON string
hosting_v1_node_js_env_var_resource_instance = HostingV1NodeJsEnvVarResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsEnvVarResource.to_json())

# convert the object into a dict
hosting_v1_node_js_env_var_resource_dict = hosting_v1_node_js_env_var_resource_instance.to_dict()
# create an instance of HostingV1NodeJsEnvVarResource from a dict
hosting_v1_node_js_env_var_resource_from_dict = HostingV1NodeJsEnvVarResource.from_dict(hosting_v1_node_js_env_var_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


