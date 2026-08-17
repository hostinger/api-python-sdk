# AgencyHostingV1PhpExtensionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | PHP extension name. | [optional] 
**description** | **str** | What the extension provides. | [optional] 
**state** | **str** | Whether the extension is currently enabled. Extensions in the \&quot;built-in\&quot; state are compiled into PHP and cannot be turned off. | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_php_extension_resource import AgencyHostingV1PhpExtensionResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1PhpExtensionResource from a JSON string
agency_hosting_v1_php_extension_resource_instance = AgencyHostingV1PhpExtensionResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1PhpExtensionResource.to_json())

# convert the object into a dict
agency_hosting_v1_php_extension_resource_dict = agency_hosting_v1_php_extension_resource_instance.to_dict()
# create an instance of AgencyHostingV1PhpExtensionResource from a dict
agency_hosting_v1_php_extension_resource_from_dict = AgencyHostingV1PhpExtensionResource.from_dict(agency_hosting_v1_php_extension_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


