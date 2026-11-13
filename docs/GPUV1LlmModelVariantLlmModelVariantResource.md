# GPUV1LlmModelVariantLlmModelVariantResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | LLM model variant ID | [optional] 
**model_tag** | **str** |  | [optional] 
**parameter_count** | **int** |  | [optional] 
**capabilities** | **List[str]** |  | [optional] 
**dark_image_id** | **str** | Dark theme icon image ID | [optional] 
**light_image_id** | **str** | Light theme icon image ID | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_llm_model_variant_llm_model_variant_resource import GPUV1LlmModelVariantLlmModelVariantResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1LlmModelVariantLlmModelVariantResource from a JSON string
gpuv1_llm_model_variant_llm_model_variant_resource_instance = GPUV1LlmModelVariantLlmModelVariantResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1LlmModelVariantLlmModelVariantResource.to_json())

# convert the object into a dict
gpuv1_llm_model_variant_llm_model_variant_resource_dict = gpuv1_llm_model_variant_llm_model_variant_resource_instance.to_dict()
# create an instance of GPUV1LlmModelVariantLlmModelVariantResource from a dict
gpuv1_llm_model_variant_llm_model_variant_resource_from_dict = GPUV1LlmModelVariantLlmModelVariantResource.from_dict(gpuv1_llm_model_variant_llm_model_variant_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


