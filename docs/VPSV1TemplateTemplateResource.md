# VPSV1TemplateTemplateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Template ID | [optional] 
**name** | **str** | Template name | [optional] 
**description** | **str** | Template description | [optional] 
**documentation** | **str** | Link to official OS documentation | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_template_template_resource import VPSV1TemplateTemplateResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1TemplateTemplateResource from a JSON string
vpsv1_template_template_resource_instance = VPSV1TemplateTemplateResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1TemplateTemplateResource.to_json())

# convert the object into a dict
vpsv1_template_template_resource_dict = vpsv1_template_template_resource_instance.to_dict()
# create an instance of VPSV1TemplateTemplateResource from a dict
vpsv1_template_template_resource_from_dict = VPSV1TemplateTemplateResource.from_dict(vpsv1_template_template_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


