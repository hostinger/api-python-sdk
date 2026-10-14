# WordPressV1ContentGenerateImagesRequest

Generate images from a prompt and an image type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | What the image should show. For the logo type, the wordmark and mark to render. | 
**image_type** | **str** | Kind of image to generate. It sets the default size and cropping. | 
**num_of_images** | **int** | How many images to generate | [optional] [default to 1]
**width** | **int** | Output width in pixels. Defaults per image type and is ignored for the logo type. | [optional] 
**height** | **int** | Output height in pixels. Defaults per image type and is ignored for the logo type. | [optional] 
**style** | **str** | Style tokens appended to photographic prompts. Ignored for the logo type. | [optional] 
**color_guidance** | **str** | Colour direction for the logo type only. It is not rendered as text. | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_content_generate_images_request import WordPressV1ContentGenerateImagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ContentGenerateImagesRequest from a JSON string
word_press_v1_content_generate_images_request_instance = WordPressV1ContentGenerateImagesRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ContentGenerateImagesRequest.to_json())

# convert the object into a dict
word_press_v1_content_generate_images_request_dict = word_press_v1_content_generate_images_request_instance.to_dict()
# create an instance of WordPressV1ContentGenerateImagesRequest from a dict
word_press_v1_content_generate_images_request_from_dict = WordPressV1ContentGenerateImagesRequest.from_dict(word_press_v1_content_generate_images_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


