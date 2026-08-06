# DomainsV1PortfolioClaimResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**status** | **str** | Domain status | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_portfolio_claim_resource import DomainsV1PortfolioClaimResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1PortfolioClaimResource from a JSON string
domains_v1_portfolio_claim_resource_instance = DomainsV1PortfolioClaimResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1PortfolioClaimResource.to_json())

# convert the object into a dict
domains_v1_portfolio_claim_resource_dict = domains_v1_portfolio_claim_resource_instance.to_dict()
# create an instance of DomainsV1PortfolioClaimResource from a dict
domains_v1_portfolio_claim_resource_from_dict = DomainsV1PortfolioClaimResource.from_dict(domains_v1_portfolio_claim_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


