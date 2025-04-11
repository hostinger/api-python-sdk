# DNSV1ZoneNameResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the record (use &#x60;@&#x60; for wildcard name) | [optional] 
**records** | [**List[DNSV1ZoneNameRecordResource]**](DNSV1ZoneNameRecordResource.md) | Array of [&#x60;DNS.V1.Zone.NameRecordResource&#x60;](#model/dnsv1zonenamerecordresource) | [optional] 
**ttl** | **int** | TTL (Time-To-Live) of the record | [optional] 
**type** | **str** | Type of the record | [optional] 

## Example

```python
from @hostinger/api.models.dnsv1_zone_name_resource import DNSV1ZoneNameResource

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1ZoneNameResource from a JSON string
dnsv1_zone_name_resource_instance = DNSV1ZoneNameResource.from_json(json)
# print the JSON string representation of the object
print(DNSV1ZoneNameResource.to_json())

# convert the object into a dict
dnsv1_zone_name_resource_dict = dnsv1_zone_name_resource_instance.to_dict()
# create an instance of DNSV1ZoneNameResource from a dict
dnsv1_zone_name_resource_from_dict = DNSV1ZoneNameResource.from_dict(dnsv1_zone_name_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


