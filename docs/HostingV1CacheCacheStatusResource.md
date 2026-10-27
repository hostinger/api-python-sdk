# HostingV1CacheCacheStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether server-side caching is enabled for the website | 
**is_cacheless_mode_enabled** | **bool** | Whether development (cacheless) mode is on. While it is on, caching is bypassed even when &#x60;is_enabled&#x60; is true. Can take a few minutes to follow a cacheless mode toggle. | 

## Example

```python
from hostinger_api.models.hosting_v1_cache_cache_status_resource import HostingV1CacheCacheStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1CacheCacheStatusResource from a JSON string
hosting_v1_cache_cache_status_resource_instance = HostingV1CacheCacheStatusResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1CacheCacheStatusResource.to_json())

# convert the object into a dict
hosting_v1_cache_cache_status_resource_dict = hosting_v1_cache_cache_status_resource_instance.to_dict()
# create an instance of HostingV1CacheCacheStatusResource from a dict
hosting_v1_cache_cache_status_resource_from_dict = HostingV1CacheCacheStatusResource.from_dict(hosting_v1_cache_cache_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


