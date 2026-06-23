# ReachV1ProfilesDomainsDnsRecordStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual** | [**List[ReachV1ProfilesDomainsDnsRecordStatusActualInner]**](ReachV1ProfilesDomainsDnsRecordStatusActualInner.md) |  | [optional] 
**suggested** | [**List[ReachV1ProfilesDomainsDnsRecordStatusSuggestedInner]**](ReachV1ProfilesDomainsDnsRecordStatusSuggestedInner.md) |  | [optional] 
**is_valid** | **bool** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_domains_dns_record_status import ReachV1ProfilesDomainsDnsRecordStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesDomainsDnsRecordStatus from a JSON string
reach_v1_profiles_domains_dns_record_status_instance = ReachV1ProfilesDomainsDnsRecordStatus.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesDomainsDnsRecordStatus.to_json())

# convert the object into a dict
reach_v1_profiles_domains_dns_record_status_dict = reach_v1_profiles_domains_dns_record_status_instance.to_dict()
# create an instance of ReachV1ProfilesDomainsDnsRecordStatus from a dict
reach_v1_profiles_domains_dns_record_status_from_dict = ReachV1ProfilesDomainsDnsRecordStatus.from_dict(reach_v1_profiles_domains_dns_record_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


