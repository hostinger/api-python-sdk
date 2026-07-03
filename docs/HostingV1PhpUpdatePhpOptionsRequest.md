# HostingV1PhpUpdatePhpOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**Dict[str, HostingV1PhpUpdatePhpOptionsRequestOptionsValue]**](HostingV1PhpUpdatePhpOptionsRequestOptionsValue.md) | Map of PHP options to update, keyed by option name. Only include options you want to change. | 

## Example

```python
from hostinger_api.models.hosting_v1_php_update_php_options_request import HostingV1PhpUpdatePhpOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PhpUpdatePhpOptionsRequest from a JSON string
hosting_v1_php_update_php_options_request_instance = HostingV1PhpUpdatePhpOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1PhpUpdatePhpOptionsRequest.to_json())

# convert the object into a dict
hosting_v1_php_update_php_options_request_dict = hosting_v1_php_update_php_options_request_instance.to_dict()
# create an instance of HostingV1PhpUpdatePhpOptionsRequest from a dict
hosting_v1_php_update_php_options_request_from_dict = HostingV1PhpUpdatePhpOptionsRequest.from_dict(hosting_v1_php_update_php_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


