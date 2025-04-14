# DNSV1ZoneDestroyRequestFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the record | 
**type** | **str** | Type of the record | 

## Example

```python
from hostinger_api.models.dnsv1_zone_destroy_request_filters_inner import DNSV1ZoneDestroyRequestFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1ZoneDestroyRequestFiltersInner from a JSON string
dnsv1_zone_destroy_request_filters_inner_instance = DNSV1ZoneDestroyRequestFiltersInner.from_json(json)
# print the JSON string representation of the object
print(DNSV1ZoneDestroyRequestFiltersInner.to_json())

# convert the object into a dict
dnsv1_zone_destroy_request_filters_inner_dict = dnsv1_zone_destroy_request_filters_inner_instance.to_dict()
# create an instance of DNSV1ZoneDestroyRequestFiltersInner from a dict
dnsv1_zone_destroy_request_filters_inner_from_dict = DNSV1ZoneDestroyRequestFiltersInner.from_dict(dnsv1_zone_destroy_request_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


