# WordPressV1LoginLoginLinksResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Primary auto-login URL for the WordPress installation | [optional] 
**fallback** | **str** | Fallback auto-login URL using the temporary Hostinger domain | [optional] 
**default** | **str** | Default WordPress admin URL used when auto-login is unavailable | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_login_login_links_resource import WordPressV1LoginLoginLinksResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1LoginLoginLinksResource from a JSON string
word_press_v1_login_login_links_resource_instance = WordPressV1LoginLoginLinksResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1LoginLoginLinksResource.to_json())

# convert the object into a dict
word_press_v1_login_login_links_resource_dict = word_press_v1_login_login_links_resource_instance.to_dict()
# create an instance of WordPressV1LoginLoginLinksResource from a dict
word_press_v1_login_login_links_resource_from_dict = WordPressV1LoginLoginLinksResource.from_dict(word_press_v1_login_login_links_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


