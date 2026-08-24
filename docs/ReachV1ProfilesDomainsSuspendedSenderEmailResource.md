# ReachV1ProfilesDomainsSuspendedSenderEmailResource

A sender address on the connected domain that is no longer allowed to send.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**email_local_part** | **str** | The part of the address before the @. | [optional] 
**suspended_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_domains_suspended_sender_email_resource import ReachV1ProfilesDomainsSuspendedSenderEmailResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesDomainsSuspendedSenderEmailResource from a JSON string
reach_v1_profiles_domains_suspended_sender_email_resource_instance = ReachV1ProfilesDomainsSuspendedSenderEmailResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesDomainsSuspendedSenderEmailResource.to_json())

# convert the object into a dict
reach_v1_profiles_domains_suspended_sender_email_resource_dict = reach_v1_profiles_domains_suspended_sender_email_resource_instance.to_dict()
# create an instance of ReachV1ProfilesDomainsSuspendedSenderEmailResource from a dict
reach_v1_profiles_domains_suspended_sender_email_resource_from_dict = ReachV1ProfilesDomainsSuspendedSenderEmailResource.from_dict(reach_v1_profiles_domains_suspended_sender_email_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


