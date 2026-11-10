# DomainsV1DomainDomainVerificationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | What registration waits for: - &#x60;manual_review&#x60;: a check you cannot complete yourself, such as a review of the order by   Hostinger. You have nothing to do. - &#x60;sms_code&#x60;: a code was sent by SMS to the phone number of the owner WHOIS profile. Enter it   in [hPanel](https://hpanel.hostinger.com/). - &#x60;contact_verification&#x60;: the registry requires the owner WHOIS profile to be verified first,   by email, phone number or contact name. Complete it in   [hPanel](https://hpanel.hostinger.com/); registration resumes once the profile is verified. | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_domain_domain_verification_resource import DomainsV1DomainDomainVerificationResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1DomainDomainVerificationResource from a JSON string
domains_v1_domain_domain_verification_resource_instance = DomainsV1DomainDomainVerificationResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1DomainDomainVerificationResource.to_json())

# convert the object into a dict
domains_v1_domain_domain_verification_resource_dict = domains_v1_domain_domain_verification_resource_instance.to_dict()
# create an instance of DomainsV1DomainDomainVerificationResource from a dict
domains_v1_domain_domain_verification_resource_from_dict = DomainsV1DomainDomainVerificationResource.from_dict(domains_v1_domain_domain_verification_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


