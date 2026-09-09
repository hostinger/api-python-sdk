# HorizonsV1WebsitesEditWebsiteRequestMessageInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**text** | **str** | Detailed description of the changes to apply to the website. Include which sections, features, content or design should change and how. The specification should be detailed and comprehensive, covering all requested changes. | 

## Example

```python
from hostinger_api.models.horizons_v1_websites_edit_website_request_message_inner import HorizonsV1WebsitesEditWebsiteRequestMessageInner

# TODO update the JSON string below
json = "{}"
# create an instance of HorizonsV1WebsitesEditWebsiteRequestMessageInner from a JSON string
horizons_v1_websites_edit_website_request_message_inner_instance = HorizonsV1WebsitesEditWebsiteRequestMessageInner.from_json(json)
# print the JSON string representation of the object
print(HorizonsV1WebsitesEditWebsiteRequestMessageInner.to_json())

# convert the object into a dict
horizons_v1_websites_edit_website_request_message_inner_dict = horizons_v1_websites_edit_website_request_message_inner_instance.to_dict()
# create an instance of HorizonsV1WebsitesEditWebsiteRequestMessageInner from a dict
horizons_v1_websites_edit_website_request_message_inner_from_dict = HorizonsV1WebsitesEditWebsiteRequestMessageInner.from_dict(horizons_v1_websites_edit_website_request_message_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


