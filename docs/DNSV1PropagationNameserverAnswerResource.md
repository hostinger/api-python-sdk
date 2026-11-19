# DNSV1PropagationNameserverAnswerResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nameserver** | **str** | Authoritative nameserver | [optional] 
**records** | **List[str]** | Records the nameserver serves; null or empty when it serves none | [optional] 
**ttl** | **int** | TTL in seconds: how long resolvers may keep serving a previously cached value | [optional] 

## Example

```python
from hostinger_api.models.dnsv1_propagation_nameserver_answer_resource import DNSV1PropagationNameserverAnswerResource

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1PropagationNameserverAnswerResource from a JSON string
dnsv1_propagation_nameserver_answer_resource_instance = DNSV1PropagationNameserverAnswerResource.from_json(json)
# print the JSON string representation of the object
print(DNSV1PropagationNameserverAnswerResource.to_json())

# convert the object into a dict
dnsv1_propagation_nameserver_answer_resource_dict = dnsv1_propagation_nameserver_answer_resource_instance.to_dict()
# create an instance of DNSV1PropagationNameserverAnswerResource from a dict
dnsv1_propagation_nameserver_answer_resource_from_dict = DNSV1PropagationNameserverAnswerResource.from_dict(dnsv1_propagation_nameserver_answer_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


