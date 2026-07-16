# DomainsV1PortfolioRenewalRenewalInformationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**status** | **str** | Domain status | [optional] 
**expires_at** | **datetime** | Domain expiration date | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_portfolio_renewal_renewal_information_resource import DomainsV1PortfolioRenewalRenewalInformationResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1PortfolioRenewalRenewalInformationResource from a JSON string
domains_v1_portfolio_renewal_renewal_information_resource_instance = DomainsV1PortfolioRenewalRenewalInformationResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1PortfolioRenewalRenewalInformationResource.to_json())

# convert the object into a dict
domains_v1_portfolio_renewal_renewal_information_resource_dict = domains_v1_portfolio_renewal_renewal_information_resource_instance.to_dict()
# create an instance of DomainsV1PortfolioRenewalRenewalInformationResource from a dict
domains_v1_portfolio_renewal_renewal_information_resource_from_dict = DomainsV1PortfolioRenewalRenewalInformationResource.from_dict(domains_v1_portfolio_renewal_renewal_information_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


