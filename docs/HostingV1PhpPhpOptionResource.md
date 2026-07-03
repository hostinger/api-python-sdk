# HostingV1PhpPhpOptionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Declared option type (e.g. bool, string) | [optional] 
**value** | **str** | Current value for this website | [optional] 
**comment** | **str** | Human-readable description | [optional] 
**default** | **str** | Default value | [optional] 
**range** | **str** | Allowed value range or limits, when applicable | [optional] 
**max** | **str** | Maximum value allowed by the account hosting plan, when applicable | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_php_php_option_resource import HostingV1PhpPhpOptionResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PhpPhpOptionResource from a JSON string
hosting_v1_php_php_option_resource_instance = HostingV1PhpPhpOptionResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1PhpPhpOptionResource.to_json())

# convert the object into a dict
hosting_v1_php_php_option_resource_dict = hosting_v1_php_php_option_resource_instance.to_dict()
# create an instance of HostingV1PhpPhpOptionResource from a dict
hosting_v1_php_php_option_resource_from_dict = HostingV1PhpPhpOptionResource.from_dict(hosting_v1_php_php_option_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


