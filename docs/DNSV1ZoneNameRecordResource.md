# DNSV1ZoneNameRecordResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Content of the name record | [optional] 
**is_disabled** | **bool** | Flag to mark name record as disabled | [optional] 

## Example

```python
from hostinger_api.models.dnsv1_zone_name_record_resource import DNSV1ZoneNameRecordResource

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1ZoneNameRecordResource from a JSON string
dnsv1_zone_name_record_resource_instance = DNSV1ZoneNameRecordResource.from_json(json)
# print the JSON string representation of the object
print(DNSV1ZoneNameRecordResource.to_json())

# convert the object into a dict
dnsv1_zone_name_record_resource_dict = dnsv1_zone_name_record_resource_instance.to_dict()
# create an instance of DNSV1ZoneNameRecordResource from a dict
dnsv1_zone_name_record_resource_from_dict = DNSV1ZoneNameRecordResource.from_dict(dnsv1_zone_name_record_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


