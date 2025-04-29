# DomainsV1DomainDomainExtendedResourceDomainContacts

WHOIS profiles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_id** | **int** | Admin WHOIS profile ID | [optional] 
**owner_id** | **int** | Owner WHOIS profile ID | [optional] 
**billing_id** | **int** | Billing WHOIS profile ID | [optional] 
**tech_id** | **int** | Technician WHOIS profile ID | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_domain_domain_extended_resource_domain_contacts import DomainsV1DomainDomainExtendedResourceDomainContacts

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1DomainDomainExtendedResourceDomainContacts from a JSON string
domains_v1_domain_domain_extended_resource_domain_contacts_instance = DomainsV1DomainDomainExtendedResourceDomainContacts.from_json(json)
# print the JSON string representation of the object
print(DomainsV1DomainDomainExtendedResourceDomainContacts.to_json())

# convert the object into a dict
domains_v1_domain_domain_extended_resource_domain_contacts_dict = domains_v1_domain_domain_extended_resource_domain_contacts_instance.to_dict()
# create an instance of DomainsV1DomainDomainExtendedResourceDomainContacts from a dict
domains_v1_domain_domain_extended_resource_domain_contacts_from_dict = DomainsV1DomainDomainExtendedResourceDomainContacts.from_dict(domains_v1_domain_domain_extended_resource_domain_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


