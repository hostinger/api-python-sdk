# WordPressV1ContentGenerationResource

State of an AI content generation and, once completed, its result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation_id** | **str** | Generation ID (UUID) used to poll for the result | 
**type** | **str** | Kind of generation, determines the shape of &#x60;result&#x60; | 
**status** | **str** | &#x60;in-progress&#x60; while the generation is still running, &#x60;completed&#x60; once &#x60;result&#x60; is available, &#x60;failed&#x60; when the generation stopped without a result. | 
**result** | [**WordPressV1ContentGenerationResourceResult**](WordPressV1ContentGenerationResourceResult.md) |  | 

## Example

```python
from hostinger_api.models.word_press_v1_content_generation_resource import WordPressV1ContentGenerationResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ContentGenerationResource from a JSON string
word_press_v1_content_generation_resource_instance = WordPressV1ContentGenerationResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ContentGenerationResource.to_json())

# convert the object into a dict
word_press_v1_content_generation_resource_dict = word_press_v1_content_generation_resource_instance.to_dict()
# create an instance of WordPressV1ContentGenerationResource from a dict
word_press_v1_content_generation_resource_from_dict = WordPressV1ContentGenerationResource.from_dict(word_press_v1_content_generation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


