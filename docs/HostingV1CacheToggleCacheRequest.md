# HostingV1CacheToggleCacheRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Turn server-side caching on (true) or off (false) for the website. | 

## Example

```python
from hostinger_api.models.hosting_v1_cache_toggle_cache_request import HostingV1CacheToggleCacheRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1CacheToggleCacheRequest from a JSON string
hosting_v1_cache_toggle_cache_request_instance = HostingV1CacheToggleCacheRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1CacheToggleCacheRequest.to_json())

# convert the object into a dict
hosting_v1_cache_toggle_cache_request_dict = hosting_v1_cache_toggle_cache_request_instance.to_dict()
# create an instance of HostingV1CacheToggleCacheRequest from a dict
hosting_v1_cache_toggle_cache_request_from_dict = HostingV1CacheToggleCacheRequest.from_dict(hosting_v1_cache_toggle_cache_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


