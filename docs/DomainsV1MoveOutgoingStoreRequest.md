# DomainsV1MoveOutgoingStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_customer_email** | **str** | Email address of the Hostinger account receiving the domain | 

## Example

```python
from hostinger_api.models.domains_v1_move_outgoing_store_request import DomainsV1MoveOutgoingStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1MoveOutgoingStoreRequest from a JSON string
domains_v1_move_outgoing_store_request_instance = DomainsV1MoveOutgoingStoreRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1MoveOutgoingStoreRequest.to_json())

# convert the object into a dict
domains_v1_move_outgoing_store_request_dict = domains_v1_move_outgoing_store_request_instance.to_dict()
# create an instance of DomainsV1MoveOutgoingStoreRequest from a dict
domains_v1_move_outgoing_store_request_from_dict = DomainsV1MoveOutgoingStoreRequest.from_dict(domains_v1_move_outgoing_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


