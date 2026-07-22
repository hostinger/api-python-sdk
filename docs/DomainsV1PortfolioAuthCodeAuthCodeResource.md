# DomainsV1PortfolioAuthCodeAuthCodeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** | Domain authorization code used to transfer the domain to another registrar. | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_portfolio_auth_code_auth_code_resource import DomainsV1PortfolioAuthCodeAuthCodeResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1PortfolioAuthCodeAuthCodeResource from a JSON string
domains_v1_portfolio_auth_code_auth_code_resource_instance = DomainsV1PortfolioAuthCodeAuthCodeResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1PortfolioAuthCodeAuthCodeResource.to_json())

# convert the object into a dict
domains_v1_portfolio_auth_code_auth_code_resource_dict = domains_v1_portfolio_auth_code_auth_code_resource_instance.to_dict()
# create an instance of DomainsV1PortfolioAuthCodeAuthCodeResource from a dict
domains_v1_portfolio_auth_code_auth_code_resource_from_dict = DomainsV1PortfolioAuthCodeAuthCodeResource.from_dict(domains_v1_portfolio_auth_code_auth_code_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


