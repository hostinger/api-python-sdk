# ReachV1TemplatesStoreRequest

Create a reusable email template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_content** | **str** | The email body as HTML. It is sanitised before it is stored, so the saved template can differ from what was sent - inline any styles the email clients need and keep the markup self-contained. | 
**title** | **str** | Name the template is listed under. Not shown to the recipients. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_templates_store_request import ReachV1TemplatesStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1TemplatesStoreRequest from a JSON string
reach_v1_templates_store_request_instance = ReachV1TemplatesStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1TemplatesStoreRequest.to_json())

# convert the object into a dict
reach_v1_templates_store_request_dict = reach_v1_templates_store_request_instance.to_dict()
# create an instance of ReachV1TemplatesStoreRequest from a dict
reach_v1_templates_store_request_from_dict = ReachV1TemplatesStoreRequest.from_dict(reach_v1_templates_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


