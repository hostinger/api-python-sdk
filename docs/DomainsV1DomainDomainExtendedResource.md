# DomainsV1DomainDomainExtendedResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**status** | **str** | Status of the domain | [optional] 
**message** | **str** |  | [optional] 
**is_privacy_protection_allowed** | **bool** | Is privacy protection allowed for the domain | [optional] 
**is_privacy_protected** | **bool** | Is privacy protection enabled for the domain | [optional] 
**is_lockable** | **bool** | Is domain allowed to be locked | [optional] 
**is_locked** | **bool** | Is domain locked | [optional] 
**name_servers** | [**DomainsV1DomainDomainExtendedResourceNameServers**](DomainsV1DomainDomainExtendedResourceNameServers.md) |  | [optional] 
**child_name_servers** | **List[List[str]]** | Child name servers | [optional] 
**domain_contacts** | [**DomainsV1DomainDomainExtendedResourceDomainContacts**](DomainsV1DomainDomainExtendedResourceDomainContacts.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**var_60_days_lock_expires_at** | **datetime** |  | [optional] 
**registered_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_domain_domain_extended_resource import DomainsV1DomainDomainExtendedResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1DomainDomainExtendedResource from a JSON string
domains_v1_domain_domain_extended_resource_instance = DomainsV1DomainDomainExtendedResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1DomainDomainExtendedResource.to_json())

# convert the object into a dict
domains_v1_domain_domain_extended_resource_dict = domains_v1_domain_domain_extended_resource_instance.to_dict()
# create an instance of DomainsV1DomainDomainExtendedResource from a dict
domains_v1_domain_domain_extended_resource_from_dict = DomainsV1DomainDomainExtendedResource.from_dict(domains_v1_domain_domain_extended_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


