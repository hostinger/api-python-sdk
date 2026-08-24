# ReachV1ProfilesDomainsSendingDomainResource

The sending domain connected to the profile.  When no domain is connected every field is `null` and `suspended_sender_emails` is empty, so the shape stays the same whether or not the profile is set up for sending.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain campaigns are sent from. It may be a subdomain of the domain that was connected, so it will not always match the website domain. | [optional] 
**status** | **str** | Campaigns can only be sent while the domain is &#x60;active&#x60;. | [optional] 
**created_at** | **datetime** | When the domain was connected to the profile. | [optional] 
**updated_at** | **datetime** | When the domain or its verification state last changed. | [optional] 
**suspended_sender_emails** | [**List[ReachV1ProfilesDomainsSuspendedSenderEmailResource]**](ReachV1ProfilesDomainsSuspendedSenderEmailResource.md) | Sender addresses on this domain that have been suspended. A campaign using one of them will not go out even while the domain itself is active. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_domains_sending_domain_resource import ReachV1ProfilesDomainsSendingDomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesDomainsSendingDomainResource from a JSON string
reach_v1_profiles_domains_sending_domain_resource_instance = ReachV1ProfilesDomainsSendingDomainResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesDomainsSendingDomainResource.to_json())

# convert the object into a dict
reach_v1_profiles_domains_sending_domain_resource_dict = reach_v1_profiles_domains_sending_domain_resource_instance.to_dict()
# create an instance of ReachV1ProfilesDomainsSendingDomainResource from a dict
reach_v1_profiles_domains_sending_domain_resource_from_dict = ReachV1ProfilesDomainsSendingDomainResource.from_dict(reach_v1_profiles_domains_sending_domain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


