# DomainsV1ForwardingStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | 
**redirect_type** | **str** | Redirect type | 
**redirect_url** | **str** | URL to forward domain to | 

## Example

```python
from hostinger_api.models.domains_v1_forwarding_store_request import DomainsV1ForwardingStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1ForwardingStoreRequest from a JSON string
domains_v1_forwarding_store_request_instance = DomainsV1ForwardingStoreRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1ForwardingStoreRequest.to_json())

# convert the object into a dict
domains_v1_forwarding_store_request_dict = domains_v1_forwarding_store_request_instance.to_dict()
# create an instance of DomainsV1ForwardingStoreRequest from a dict
domains_v1_forwarding_store_request_from_dict = DomainsV1ForwardingStoreRequest.from_dict(domains_v1_forwarding_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


