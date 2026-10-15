# WordPressV1ContentGenerationResourceResult

Generated content, `null` until the status is `completed`. For `image-generation` it is the generated images object; for `website-generation` it is the generated website document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**List[WordPressV1ContentGeneratedImageResource]**](WordPressV1ContentGeneratedImageResource.md) | Generated images, each available at a temporary URL | 
**expires_at** | **datetime** | Time after which the image URLs stop working. Download the images before then. | 

## Example

```python
from hostinger_api.models.word_press_v1_content_generation_resource_result import WordPressV1ContentGenerationResourceResult

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ContentGenerationResourceResult from a JSON string
word_press_v1_content_generation_resource_result_instance = WordPressV1ContentGenerationResourceResult.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ContentGenerationResourceResult.to_json())

# convert the object into a dict
word_press_v1_content_generation_resource_result_dict = word_press_v1_content_generation_resource_result_instance.to_dict()
# create an instance of WordPressV1ContentGenerationResourceResult from a dict
word_press_v1_content_generation_resource_result_from_dict = WordPressV1ContentGenerationResourceResult.from_dict(word_press_v1_content_generation_resource_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


