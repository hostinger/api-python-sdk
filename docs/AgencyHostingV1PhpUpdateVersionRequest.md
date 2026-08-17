# AgencyHostingV1PhpUpdateVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | PHP version to switch the website to, as major.minor. Must be one of the versions returned by the available versions endpoint. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_php_update_version_request import AgencyHostingV1PhpUpdateVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1PhpUpdateVersionRequest from a JSON string
agency_hosting_v1_php_update_version_request_instance = AgencyHostingV1PhpUpdateVersionRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1PhpUpdateVersionRequest.to_json())

# convert the object into a dict
agency_hosting_v1_php_update_version_request_dict = agency_hosting_v1_php_update_version_request_instance.to_dict()
# create an instance of AgencyHostingV1PhpUpdateVersionRequest from a dict
agency_hosting_v1_php_update_version_request_from_dict = AgencyHostingV1PhpUpdateVersionRequest.from_dict(agency_hosting_v1_php_update_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


