# DomainsV1ForwardingForwardingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**redirect_type** | **str** | Redirect type | [optional] 
**redirect_url** | **str** | URL domain is forwarded to | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_forwarding_forwarding_resource import DomainsV1ForwardingForwardingResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1ForwardingForwardingResource from a JSON string
domains_v1_forwarding_forwarding_resource_instance = DomainsV1ForwardingForwardingResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1ForwardingForwardingResource.to_json())

# convert the object into a dict
domains_v1_forwarding_forwarding_resource_dict = domains_v1_forwarding_forwarding_resource_instance.to_dict()
# create an instance of DomainsV1ForwardingForwardingResource from a dict
domains_v1_forwarding_forwarding_resource_from_dict = DomainsV1ForwardingForwardingResource.from_dict(domains_v1_forwarding_forwarding_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


