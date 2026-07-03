# HostingV1PhpUpdatePhpExtensionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **List[str]** | PHP extensions to enable. | [optional] 
**disable** | **List[str]** | PHP extensions to disable. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_php_update_php_extensions_request import HostingV1PhpUpdatePhpExtensionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PhpUpdatePhpExtensionsRequest from a JSON string
hosting_v1_php_update_php_extensions_request_instance = HostingV1PhpUpdatePhpExtensionsRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1PhpUpdatePhpExtensionsRequest.to_json())

# convert the object into a dict
hosting_v1_php_update_php_extensions_request_dict = hosting_v1_php_update_php_extensions_request_instance.to_dict()
# create an instance of HostingV1PhpUpdatePhpExtensionsRequest from a dict
hosting_v1_php_update_php_extensions_request_from_dict = HostingV1PhpUpdatePhpExtensionsRequest.from_dict(hosting_v1_php_update_php_extensions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


