# HostingV1CdnCdnStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether the Hostinger CDN is enabled for the website domain | 

## Example

```python
from hostinger_api.models.hosting_v1_cdn_cdn_status_resource import HostingV1CdnCdnStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1CdnCdnStatusResource from a JSON string
hosting_v1_cdn_cdn_status_resource_instance = HostingV1CdnCdnStatusResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1CdnCdnStatusResource.to_json())

# convert the object into a dict
hosting_v1_cdn_cdn_status_resource_dict = hosting_v1_cdn_cdn_status_resource_instance.to_dict()
# create an instance of HostingV1CdnCdnStatusResource from a dict
hosting_v1_cdn_cdn_status_resource_from_dict = HostingV1CdnCdnStatusResource.from_dict(hosting_v1_cdn_cdn_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


