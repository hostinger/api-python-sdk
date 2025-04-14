# DNSV1ZoneUpdateRequestZoneInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the record (use &#x60;@&#x60; for wildcard name) | 
**records** | [**List[DNSV1ZoneUpdateRequestZoneInnerRecordsInner]**](DNSV1ZoneUpdateRequestZoneInnerRecordsInner.md) | Records assigned to the name | [optional] 
**ttl** | **int** | TTL (Time-To-Live) of the record | [optional] 
**type** | **str** | Type of the record | 

## Example

```python
from hostinger_api.models.dnsv1_zone_update_request_zone_inner import DNSV1ZoneUpdateRequestZoneInner

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1ZoneUpdateRequestZoneInner from a JSON string
dnsv1_zone_update_request_zone_inner_instance = DNSV1ZoneUpdateRequestZoneInner.from_json(json)
# print the JSON string representation of the object
print(DNSV1ZoneUpdateRequestZoneInner.to_json())

# convert the object into a dict
dnsv1_zone_update_request_zone_inner_dict = dnsv1_zone_update_request_zone_inner_instance.to_dict()
# create an instance of DNSV1ZoneUpdateRequestZoneInner from a dict
dnsv1_zone_update_request_zone_inner_from_dict = DNSV1ZoneUpdateRequestZoneInner.from_dict(dnsv1_zone_update_request_zone_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


