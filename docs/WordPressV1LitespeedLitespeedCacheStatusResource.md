# WordPressV1LitespeedLitespeedCacheStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_installed** | **bool** | Whether the LiteSpeed Cache plugin is installed on the WordPress installation | [optional] 
**is_active** | **bool** | Whether the LiteSpeed Cache plugin is active on the WordPress installation | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_litespeed_litespeed_cache_status_resource import WordPressV1LitespeedLitespeedCacheStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1LitespeedLitespeedCacheStatusResource from a JSON string
word_press_v1_litespeed_litespeed_cache_status_resource_instance = WordPressV1LitespeedLitespeedCacheStatusResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1LitespeedLitespeedCacheStatusResource.to_json())

# convert the object into a dict
word_press_v1_litespeed_litespeed_cache_status_resource_dict = word_press_v1_litespeed_litespeed_cache_status_resource_instance.to_dict()
# create an instance of WordPressV1LitespeedLitespeedCacheStatusResource from a dict
word_press_v1_litespeed_litespeed_cache_status_resource_from_dict = WordPressV1LitespeedLitespeedCacheStatusResource.from_dict(word_press_v1_litespeed_litespeed_cache_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


