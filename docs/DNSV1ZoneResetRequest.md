# DNSV1ZoneResetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync** | **bool** | Determines if operation should be run synchronously | [optional] [default to True]
**reset_email_records** | **bool** | Determines if email records should be reset | [optional] [default to True]
**whitelisted_record_types** | **List[str]** | Specifies which record types to not reset | [optional] 

## Example

```python
from hostinger-api.models.dnsv1_zone_reset_request import DNSV1ZoneResetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1ZoneResetRequest from a JSON string
dnsv1_zone_reset_request_instance = DNSV1ZoneResetRequest.from_json(json)
# print the JSON string representation of the object
print(DNSV1ZoneResetRequest.to_json())

# convert the object into a dict
dnsv1_zone_reset_request_dict = dnsv1_zone_reset_request_instance.to_dict()
# create an instance of DNSV1ZoneResetRequest from a dict
dnsv1_zone_reset_request_from_dict = DNSV1ZoneResetRequest.from_dict(dnsv1_zone_reset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


