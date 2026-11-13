# GPUV1OsTemplateOsTemplateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | OS template ID | [optional] 
**name** | **str** |  | [optional] 
**kb_url** | **str** | Knowledge base article about the template | [optional] 
**dark_image_id** | **str** | Dark theme icon image ID | [optional] 
**light_image_id** | **str** | Light theme icon image ID | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_os_template_os_template_resource import GPUV1OsTemplateOsTemplateResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1OsTemplateOsTemplateResource from a JSON string
gpuv1_os_template_os_template_resource_instance = GPUV1OsTemplateOsTemplateResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1OsTemplateOsTemplateResource.to_json())

# convert the object into a dict
gpuv1_os_template_os_template_resource_dict = gpuv1_os_template_os_template_resource_instance.to_dict()
# create an instance of GPUV1OsTemplateOsTemplateResource from a dict
gpuv1_os_template_os_template_resource_from_dict = GPUV1OsTemplateOsTemplateResource.from_dict(gpuv1_os_template_os_template_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


