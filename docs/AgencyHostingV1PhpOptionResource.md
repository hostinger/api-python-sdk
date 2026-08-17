# AgencyHostingV1PhpOptionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | php.ini directive name. | [optional] 
**description** | **str** | What the directive controls. | [optional] 
**default_value** | **str** | Value applied when no custom value is set. | [optional] 
**allowed_values** | **List[str]** | Values this option accepts. Null when the option accepts any value of its type. | [optional] 
**value** | **str** | Value currently in effect for the website. | [optional] 
**type** | **str** | Whether the option takes a single value or a list of values. | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_php_option_resource import AgencyHostingV1PhpOptionResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1PhpOptionResource from a JSON string
agency_hosting_v1_php_option_resource_instance = AgencyHostingV1PhpOptionResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1PhpOptionResource.to_json())

# convert the object into a dict
agency_hosting_v1_php_option_resource_dict = agency_hosting_v1_php_option_resource_instance.to_dict()
# create an instance of AgencyHostingV1PhpOptionResource from a dict
agency_hosting_v1_php_option_resource_from_dict = AgencyHostingV1PhpOptionResource.from_dict(agency_hosting_v1_php_option_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


