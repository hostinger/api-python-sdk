# DomainsV1PortfolioPurchaseRequestDomainContacts

Domain contact information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **int** | Owner contact WHOIS record ID | [optional] 
**admin_id** | **int** | Administrative contact WHOIS record ID | [optional] 
**billing_id** | **int** | Billing contact WHOIS record ID | [optional] 
**tech_id** | **int** | Technical contact WHOIS record ID | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_portfolio_purchase_request_domain_contacts import DomainsV1PortfolioPurchaseRequestDomainContacts

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1PortfolioPurchaseRequestDomainContacts from a JSON string
domains_v1_portfolio_purchase_request_domain_contacts_instance = DomainsV1PortfolioPurchaseRequestDomainContacts.from_json(json)
# print the JSON string representation of the object
print(DomainsV1PortfolioPurchaseRequestDomainContacts.to_json())

# convert the object into a dict
domains_v1_portfolio_purchase_request_domain_contacts_dict = domains_v1_portfolio_purchase_request_domain_contacts_instance.to_dict()
# create an instance of DomainsV1PortfolioPurchaseRequestDomainContacts from a dict
domains_v1_portfolio_purchase_request_domain_contacts_from_dict = DomainsV1PortfolioPurchaseRequestDomainContacts.from_dict(domains_v1_portfolio_purchase_request_domain_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


