# HostingV1PhpUpdatePhpVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | PHP version to switch the website to. | 

## Example

```python
from hostinger_api.models.hosting_v1_php_update_php_version_request import HostingV1PhpUpdatePhpVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PhpUpdatePhpVersionRequest from a JSON string
hosting_v1_php_update_php_version_request_instance = HostingV1PhpUpdatePhpVersionRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1PhpUpdatePhpVersionRequest.to_json())

# convert the object into a dict
hosting_v1_php_update_php_version_request_dict = hosting_v1_php_update_php_version_request_instance.to_dict()
# create an instance of HostingV1PhpUpdatePhpVersionRequest from a dict
hosting_v1_php_update_php_version_request_from_dict = HostingV1PhpUpdatePhpVersionRequest.from_dict(hosting_v1_php_update_php_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


