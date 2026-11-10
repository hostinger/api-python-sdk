# DomainsV1DomainDomainContactVerificationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**DomainsV1DomainDomainContactVerificationChannelResource**](DomainsV1DomainDomainContactVerificationChannelResource.md) |  | [optional] 
**phone** | [**DomainsV1DomainDomainContactVerificationChannelResource**](DomainsV1DomainDomainContactVerificationChannelResource.md) |  | [optional] 
**contact_name** | [**DomainsV1DomainDomainContactVerificationChannelResource**](DomainsV1DomainDomainContactVerificationChannelResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_domain_domain_contact_verification_resource import DomainsV1DomainDomainContactVerificationResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1DomainDomainContactVerificationResource from a JSON string
domains_v1_domain_domain_contact_verification_resource_instance = DomainsV1DomainDomainContactVerificationResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1DomainDomainContactVerificationResource.to_json())

# convert the object into a dict
domains_v1_domain_domain_contact_verification_resource_dict = domains_v1_domain_domain_contact_verification_resource_instance.to_dict()
# create an instance of DomainsV1DomainDomainContactVerificationResource from a dict
domains_v1_domain_domain_contact_verification_resource_from_dict = DomainsV1DomainDomainContactVerificationResource.from_dict(domains_v1_domain_domain_contact_verification_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


