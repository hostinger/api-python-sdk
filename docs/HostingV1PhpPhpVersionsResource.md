# HostingV1PhpPhpVersionsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **object** | Key-value pairs of supported versions | [optional] 
**unsupported** | **object** | Key-value pairs of unsupported versions | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_php_php_versions_resource import HostingV1PhpPhpVersionsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PhpPhpVersionsResource from a JSON string
hosting_v1_php_php_versions_resource_instance = HostingV1PhpPhpVersionsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1PhpPhpVersionsResource.to_json())

# convert the object into a dict
hosting_v1_php_php_versions_resource_dict = hosting_v1_php_php_versions_resource_instance.to_dict()
# create an instance of HostingV1PhpPhpVersionsResource from a dict
hosting_v1_php_php_versions_resource_from_dict = HostingV1PhpPhpVersionsResource.from_dict(hosting_v1_php_php_versions_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


