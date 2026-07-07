# WordPressV1MemcachedToggleMemcachedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Activate (true) or deactivate (false) the Memcached object cache for the WordPress installation. | 

## Example

```python
from hostinger_api.models.word_press_v1_memcached_toggle_memcached_request import WordPressV1MemcachedToggleMemcachedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1MemcachedToggleMemcachedRequest from a JSON string
word_press_v1_memcached_toggle_memcached_request_instance = WordPressV1MemcachedToggleMemcachedRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1MemcachedToggleMemcachedRequest.to_json())

# convert the object into a dict
word_press_v1_memcached_toggle_memcached_request_dict = word_press_v1_memcached_toggle_memcached_request_instance.to_dict()
# create an instance of WordPressV1MemcachedToggleMemcachedRequest from a dict
word_press_v1_memcached_toggle_memcached_request_from_dict = WordPressV1MemcachedToggleMemcachedRequest.from_dict(word_press_v1_memcached_toggle_memcached_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


