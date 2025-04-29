# DomainsV1PortfolioPurchaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | 
**item_id** | **str** | Catalog price item ID | 
**payment_method_id** | **int** | Payment method ID | [optional] 
**domain_contacts** | [**DomainsV1PortfolioPurchaseRequestDomainContacts**](DomainsV1PortfolioPurchaseRequestDomainContacts.md) |  | [optional] 
**additional_details** | **object** | Additional registration data, possible values depends on TLD | [optional] 
**coupons** | **List[object]** | Discount coupon codes | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_portfolio_purchase_request import DomainsV1PortfolioPurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1PortfolioPurchaseRequest from a JSON string
domains_v1_portfolio_purchase_request_instance = DomainsV1PortfolioPurchaseRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1PortfolioPurchaseRequest.to_json())

# convert the object into a dict
domains_v1_portfolio_purchase_request_dict = domains_v1_portfolio_purchase_request_instance.to_dict()
# create an instance of DomainsV1PortfolioPurchaseRequest from a dict
domains_v1_portfolio_purchase_request_from_dict = DomainsV1PortfolioPurchaseRequest.from_dict(domains_v1_portfolio_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


