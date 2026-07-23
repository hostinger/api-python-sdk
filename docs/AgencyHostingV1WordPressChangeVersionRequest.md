# AgencyHostingV1WordPressChangeVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Target WordPress core version to install. Must be one of the available versions. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_word_press_change_version_request import AgencyHostingV1WordPressChangeVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WordPressChangeVersionRequest from a JSON string
agency_hosting_v1_word_press_change_version_request_instance = AgencyHostingV1WordPressChangeVersionRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WordPressChangeVersionRequest.to_json())

# convert the object into a dict
agency_hosting_v1_word_press_change_version_request_dict = agency_hosting_v1_word_press_change_version_request_instance.to_dict()
# create an instance of AgencyHostingV1WordPressChangeVersionRequest from a dict
agency_hosting_v1_word_press_change_version_request_from_dict = AgencyHostingV1WordPressChangeVersionRequest.from_dict(agency_hosting_v1_word_press_change_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


