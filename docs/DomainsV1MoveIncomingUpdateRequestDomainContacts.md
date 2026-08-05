# DomainsV1MoveIncomingUpdateRequestDomainContacts

WHOIS profiles of the accepting account. Only the contact types required by the TLD are applied, but all four IDs must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **int** | Owner contact WHOIS record ID | 
**admin_id** | **int** | Administrative contact WHOIS record ID | 
**billing_id** | **int** | Billing contact WHOIS record ID | 
**tech_id** | **int** | Technical contact WHOIS record ID | 

## Example

```python
from hostinger_api.models.domains_v1_move_incoming_update_request_domain_contacts import DomainsV1MoveIncomingUpdateRequestDomainContacts

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1MoveIncomingUpdateRequestDomainContacts from a JSON string
domains_v1_move_incoming_update_request_domain_contacts_instance = DomainsV1MoveIncomingUpdateRequestDomainContacts.from_json(json)
# print the JSON string representation of the object
print(DomainsV1MoveIncomingUpdateRequestDomainContacts.to_json())

# convert the object into a dict
domains_v1_move_incoming_update_request_domain_contacts_dict = domains_v1_move_incoming_update_request_domain_contacts_instance.to_dict()
# create an instance of DomainsV1MoveIncomingUpdateRequestDomainContacts from a dict
domains_v1_move_incoming_update_request_domain_contacts_from_dict = DomainsV1MoveIncomingUpdateRequestDomainContacts.from_dict(domains_v1_move_incoming_update_request_domain_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


