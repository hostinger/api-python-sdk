# DomainsV1PortfolioSetupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_contacts** | [**DomainsV1PortfolioClaimRequestDomainContacts**](DomainsV1PortfolioClaimRequestDomainContacts.md) |  | [optional] 
**additional_details** | **object** | Additional registration data, possible values depends on TLD | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_portfolio_setup_request import DomainsV1PortfolioSetupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1PortfolioSetupRequest from a JSON string
domains_v1_portfolio_setup_request_instance = DomainsV1PortfolioSetupRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1PortfolioSetupRequest.to_json())

# convert the object into a dict
domains_v1_portfolio_setup_request_dict = domains_v1_portfolio_setup_request_instance.to_dict()
# create an instance of DomainsV1PortfolioSetupRequest from a dict
domains_v1_portfolio_setup_request_from_dict = DomainsV1PortfolioSetupRequest.from_dict(domains_v1_portfolio_setup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


