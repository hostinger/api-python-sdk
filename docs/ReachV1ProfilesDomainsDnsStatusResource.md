# ReachV1ProfilesDomainsDnsStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**mx** | [**ReachV1ProfilesDomainsDnsRecordStatus**](ReachV1ProfilesDomainsDnsRecordStatus.md) |  | [optional] 
**spf** | [**ReachV1ProfilesDomainsDnsRecordStatus**](ReachV1ProfilesDomainsDnsRecordStatus.md) |  | [optional] 
**dkim** | [**ReachV1ProfilesDomainsDnsRecordStatus**](ReachV1ProfilesDomainsDnsRecordStatus.md) |  | [optional] 
**dmarc** | [**ReachV1ProfilesDomainsDnsRecordStatus**](ReachV1ProfilesDomainsDnsRecordStatus.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_domains_dns_status_resource import ReachV1ProfilesDomainsDnsStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesDomainsDnsStatusResource from a JSON string
reach_v1_profiles_domains_dns_status_resource_instance = ReachV1ProfilesDomainsDnsStatusResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesDomainsDnsStatusResource.to_json())

# convert the object into a dict
reach_v1_profiles_domains_dns_status_resource_dict = reach_v1_profiles_domains_dns_status_resource_instance.to_dict()
# create an instance of ReachV1ProfilesDomainsDnsStatusResource from a dict
reach_v1_profiles_domains_dns_status_resource_from_dict = ReachV1ProfilesDomainsDnsStatusResource.from_dict(reach_v1_profiles_domains_dns_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


