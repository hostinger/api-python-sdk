# DNSV1ZoneDestroyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[DNSV1ZoneDestroyRequestFiltersInner]**](DNSV1ZoneDestroyRequestFiltersInner.md) | Filter records for deletion | 

## Example

```python
from hostinger_api.models.dnsv1_zone_destroy_request import DNSV1ZoneDestroyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1ZoneDestroyRequest from a JSON string
dnsv1_zone_destroy_request_instance = DNSV1ZoneDestroyRequest.from_json(json)
# print the JSON string representation of the object
print(DNSV1ZoneDestroyRequest.to_json())

# convert the object into a dict
dnsv1_zone_destroy_request_dict = dnsv1_zone_destroy_request_instance.to_dict()
# create an instance of DNSV1ZoneDestroyRequest from a dict
dnsv1_zone_destroy_request_from_dict = DNSV1ZoneDestroyRequest.from_dict(dnsv1_zone_destroy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


