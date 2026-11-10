# DomainsV1DomainDomainContactVerificationChannelResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | - &#x60;pending&#x60;: not verified yet. Verify it in [hPanel](https://hpanel.hostinger.com/) before   &#x60;ends_at&#x60;. - &#x60;verified&#x60;: verified, or never required for this TLD. Nothing to do. - &#x60;suspended&#x60;: not verified in time, so the domain is suspended until the owner contact is   verified in [hPanel](https://hpanel.hostinger.com/). | [optional] 
**ends_at** | **datetime** | Deadline to verify by while &#x60;status&#x60; is &#x60;pending&#x60;, after which the domain is suspended. It can still hold the past deadline once the channel is &#x60;verified&#x60; or &#x60;suspended&#x60;. | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_domain_domain_contact_verification_channel_resource import DomainsV1DomainDomainContactVerificationChannelResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1DomainDomainContactVerificationChannelResource from a JSON string
domains_v1_domain_domain_contact_verification_channel_resource_instance = DomainsV1DomainDomainContactVerificationChannelResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1DomainDomainContactVerificationChannelResource.to_json())

# convert the object into a dict
domains_v1_domain_domain_contact_verification_channel_resource_dict = domains_v1_domain_domain_contact_verification_channel_resource_instance.to_dict()
# create an instance of DomainsV1DomainDomainContactVerificationChannelResource from a dict
domains_v1_domain_domain_contact_verification_channel_resource_from_dict = DomainsV1DomainDomainContactVerificationChannelResource.from_dict(domains_v1_domain_domain_contact_verification_channel_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


