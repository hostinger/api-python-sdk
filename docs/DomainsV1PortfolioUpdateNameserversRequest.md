# DomainsV1PortfolioUpdateNameserversRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ns1** | **str** | First name server | 
**ns2** | **str** | Second name server | 
**ns3** | **str** | Third name server | [optional] 
**ns4** | **str** | Fourth name server | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_portfolio_update_nameservers_request import DomainsV1PortfolioUpdateNameserversRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1PortfolioUpdateNameserversRequest from a JSON string
domains_v1_portfolio_update_nameservers_request_instance = DomainsV1PortfolioUpdateNameserversRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1PortfolioUpdateNameserversRequest.to_json())

# convert the object into a dict
domains_v1_portfolio_update_nameservers_request_dict = domains_v1_portfolio_update_nameservers_request_instance.to_dict()
# create an instance of DomainsV1PortfolioUpdateNameserversRequest from a dict
domains_v1_portfolio_update_nameservers_request_from_dict = DomainsV1PortfolioUpdateNameserversRequest.from_dict(domains_v1_portfolio_update_nameservers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


