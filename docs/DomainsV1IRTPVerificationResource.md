# DomainsV1IRTPVerificationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**status** | **str** | IRTP verification status | [optional] 
**old_confirmed_at** | **datetime** | When the old registrant confirmed the change | [optional] 
**new_confirmed_at** | **datetime** | When the new registrant confirmed the change | [optional] 
**old_whois_profile_email** | **str** | Email the old registrant confirmation was sent to | [optional] 
**new_whois_profile_email** | **str** | Email the new registrant confirmation was sent to | [optional] 
**expires_at** | **datetime** | When the verification auto-cancels if unconfirmed | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_irtp_verification_resource import DomainsV1IRTPVerificationResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1IRTPVerificationResource from a JSON string
domains_v1_irtp_verification_resource_instance = DomainsV1IRTPVerificationResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1IRTPVerificationResource.to_json())

# convert the object into a dict
domains_v1_irtp_verification_resource_dict = domains_v1_irtp_verification_resource_instance.to_dict()
# create an instance of DomainsV1IRTPVerificationResource from a dict
domains_v1_irtp_verification_resource_from_dict = DomainsV1IRTPVerificationResource.from_dict(domains_v1_irtp_verification_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


