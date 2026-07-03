# HostingV1PhpPhpInfoResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **str** | HTML string containing the full phpinfo page | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_php_php_info_resource import HostingV1PhpPhpInfoResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PhpPhpInfoResource from a JSON string
hosting_v1_php_php_info_resource_instance = HostingV1PhpPhpInfoResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1PhpPhpInfoResource.to_json())

# convert the object into a dict
hosting_v1_php_php_info_resource_dict = hosting_v1_php_php_info_resource_instance.to_dict()
# create an instance of HostingV1PhpPhpInfoResource from a dict
hosting_v1_php_php_info_resource_from_dict = HostingV1PhpPhpInfoResource.from_dict(hosting_v1_php_php_info_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


