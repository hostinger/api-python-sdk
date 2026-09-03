# ReachV1TemplatesTemplateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Pass this as the &#x60;template_uuid&#x60; of a campaign. | [optional] 
**title** | **str** | Null for templates that were never named. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_templates_template_resource import ReachV1TemplatesTemplateResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1TemplatesTemplateResource from a JSON string
reach_v1_templates_template_resource_instance = ReachV1TemplatesTemplateResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1TemplatesTemplateResource.to_json())

# convert the object into a dict
reach_v1_templates_template_resource_dict = reach_v1_templates_template_resource_instance.to_dict()
# create an instance of ReachV1TemplatesTemplateResource from a dict
reach_v1_templates_template_resource_from_dict = ReachV1TemplatesTemplateResource.from_dict(reach_v1_templates_template_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


