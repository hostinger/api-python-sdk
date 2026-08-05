# DomainsV1MoveIncomingUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_contacts** | [**DomainsV1MoveIncomingUpdateRequestDomainContacts**](DomainsV1MoveIncomingUpdateRequestDomainContacts.md) |  | 

## Example

```python
from hostinger_api.models.domains_v1_move_incoming_update_request import DomainsV1MoveIncomingUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1MoveIncomingUpdateRequest from a JSON string
domains_v1_move_incoming_update_request_instance = DomainsV1MoveIncomingUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1MoveIncomingUpdateRequest.to_json())

# convert the object into a dict
domains_v1_move_incoming_update_request_dict = domains_v1_move_incoming_update_request_instance.to_dict()
# create an instance of DomainsV1MoveIncomingUpdateRequest from a dict
domains_v1_move_incoming_update_request_from_dict = DomainsV1MoveIncomingUpdateRequest.from_dict(domains_v1_move_incoming_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


