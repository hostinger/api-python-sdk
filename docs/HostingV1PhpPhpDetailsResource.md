# HostingV1PhpPhpDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**php_version** | **str** | Current PHP version name | [optional] 
**php_version_full** | **str** | Full PHP version name | [optional] 
**php_versions** | [**HostingV1PhpPhpVersionsResource**](HostingV1PhpPhpVersionsResource.md) |  | [optional] 
**options** | [**Dict[str, HostingV1PhpPhpOptionResource]**](HostingV1PhpPhpOptionResource.md) | PHP options keyed by option name | [optional] 
**extensions** | **object** | PHP extensions keyed by extension name | [optional] 
**conflicting_extensions** | **List[List[str]]** | Groups of extensions that conflict with each other | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_php_php_details_resource import HostingV1PhpPhpDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PhpPhpDetailsResource from a JSON string
hosting_v1_php_php_details_resource_instance = HostingV1PhpPhpDetailsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1PhpPhpDetailsResource.to_json())

# convert the object into a dict
hosting_v1_php_php_details_resource_dict = hosting_v1_php_php_details_resource_instance.to_dict()
# create an instance of HostingV1PhpPhpDetailsResource from a dict
hosting_v1_php_php_details_resource_from_dict = HostingV1PhpPhpDetailsResource.from_dict(hosting_v1_php_php_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


