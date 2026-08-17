# AgencyHostingV1PhpUpdateOptionsRequestOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | php.ini directive name. | 
**value** | **str** | Value to apply. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_php_update_options_request_options_inner import AgencyHostingV1PhpUpdateOptionsRequestOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1PhpUpdateOptionsRequestOptionsInner from a JSON string
agency_hosting_v1_php_update_options_request_options_inner_instance = AgencyHostingV1PhpUpdateOptionsRequestOptionsInner.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1PhpUpdateOptionsRequestOptionsInner.to_json())

# convert the object into a dict
agency_hosting_v1_php_update_options_request_options_inner_dict = agency_hosting_v1_php_update_options_request_options_inner_instance.to_dict()
# create an instance of AgencyHostingV1PhpUpdateOptionsRequestOptionsInner from a dict
agency_hosting_v1_php_update_options_request_options_inner_from_dict = AgencyHostingV1PhpUpdateOptionsRequestOptionsInner.from_dict(agency_hosting_v1_php_update_options_request_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


