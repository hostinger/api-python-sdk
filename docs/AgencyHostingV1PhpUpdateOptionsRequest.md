# AgencyHostingV1PhpUpdateOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**List[AgencyHostingV1PhpUpdateOptionsRequestOptionsInner]**](AgencyHostingV1PhpUpdateOptionsRequestOptionsInner.md) | Option names and values. Each name must be one of the options returned by the options endpoint, and each value must satisfy that option&#39;s allowed_values when it declares them. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_php_update_options_request import AgencyHostingV1PhpUpdateOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1PhpUpdateOptionsRequest from a JSON string
agency_hosting_v1_php_update_options_request_instance = AgencyHostingV1PhpUpdateOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1PhpUpdateOptionsRequest.to_json())

# convert the object into a dict
agency_hosting_v1_php_update_options_request_dict = agency_hosting_v1_php_update_options_request_instance.to_dict()
# create an instance of AgencyHostingV1PhpUpdateOptionsRequest from a dict
agency_hosting_v1_php_update_options_request_from_dict = AgencyHostingV1PhpUpdateOptionsRequest.from_dict(agency_hosting_v1_php_update_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


