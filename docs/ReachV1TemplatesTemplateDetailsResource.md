# ReachV1TemplatesTemplateDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Pass this as the &#x60;template_uuid&#x60; of a campaign. | [optional] 
**title** | **str** | Null for templates that were never named. | [optional] 
**template_content** | **str** | Full HTML of the template, with personalization tags such as &#x60;{{name}}&#x60; unrendered. Null when the stored HTML cannot be read. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_templates_template_details_resource import ReachV1TemplatesTemplateDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1TemplatesTemplateDetailsResource from a JSON string
reach_v1_templates_template_details_resource_instance = ReachV1TemplatesTemplateDetailsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1TemplatesTemplateDetailsResource.to_json())

# convert the object into a dict
reach_v1_templates_template_details_resource_dict = reach_v1_templates_template_details_resource_instance.to_dict()
# create an instance of ReachV1TemplatesTemplateDetailsResource from a dict
reach_v1_templates_template_details_resource_from_dict = ReachV1TemplatesTemplateDetailsResource.from_dict(reach_v1_templates_template_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


