# DNSV1PropagationAuthoritativeAnswerResource

What the authoritative nameservers serve now: the best signal of the current record value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **str** | DNS zone that holds the record | [optional] 
**nameservers** | [**List[DNSV1PropagationNameserverAnswerResource]**](DNSV1PropagationNameserverAnswerResource.md) | Answer of each authoritative nameserver of the zone | [optional] 

## Example

```python
from hostinger_api.models.dnsv1_propagation_authoritative_answer_resource import DNSV1PropagationAuthoritativeAnswerResource

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1PropagationAuthoritativeAnswerResource from a JSON string
dnsv1_propagation_authoritative_answer_resource_instance = DNSV1PropagationAuthoritativeAnswerResource.from_json(json)
# print the JSON string representation of the object
print(DNSV1PropagationAuthoritativeAnswerResource.to_json())

# convert the object into a dict
dnsv1_propagation_authoritative_answer_resource_dict = dnsv1_propagation_authoritative_answer_resource_instance.to_dict()
# create an instance of DNSV1PropagationAuthoritativeAnswerResource from a dict
dnsv1_propagation_authoritative_answer_resource_from_dict = DNSV1PropagationAuthoritativeAnswerResource.from_dict(dnsv1_propagation_authoritative_answer_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


