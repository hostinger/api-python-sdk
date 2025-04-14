# DNSV1ZoneUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overwrite** | **bool** | If &#x60;true&#x60;, resource records (RRs) matching name and type will be deleted and new RRs will be created, otherwise resource records&#39; ttl&#39;s are updated and new records are appended. If no matching RRs are found, they are created. | [optional] [default to True]
**zone** | [**List[DNSV1ZoneUpdateRequestZoneInner]**](DNSV1ZoneUpdateRequestZoneInner.md) |  | 

## Example

```python
from hostinger_api.models.dnsv1_zone_update_request import DNSV1ZoneUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1ZoneUpdateRequest from a JSON string
dnsv1_zone_update_request_instance = DNSV1ZoneUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DNSV1ZoneUpdateRequest.to_json())

# convert the object into a dict
dnsv1_zone_update_request_dict = dnsv1_zone_update_request_instance.to_dict()
# create an instance of DNSV1ZoneUpdateRequest from a dict
dnsv1_zone_update_request_from_dict = DNSV1ZoneUpdateRequest.from_dict(dnsv1_zone_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


