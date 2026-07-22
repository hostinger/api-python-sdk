# DomainsV1ForwardingUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_type** | **str** | Redirect type | 
**redirect_url** | **str** | URL to forward domain to | 

## Example

```python
from hostinger_api.models.domains_v1_forwarding_update_request import DomainsV1ForwardingUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1ForwardingUpdateRequest from a JSON string
domains_v1_forwarding_update_request_instance = DomainsV1ForwardingUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1ForwardingUpdateRequest.to_json())

# convert the object into a dict
domains_v1_forwarding_update_request_dict = domains_v1_forwarding_update_request_instance.to_dict()
# create an instance of DomainsV1ForwardingUpdateRequest from a dict
domains_v1_forwarding_update_request_from_dict = DomainsV1ForwardingUpdateRequest.from_dict(domains_v1_forwarding_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


