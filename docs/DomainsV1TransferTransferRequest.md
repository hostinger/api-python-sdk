# DomainsV1TransferTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | 
**auth_code** | **str** | Authorization code from the current registrar | 
**domain_contacts** | [**DomainsV1PortfolioClaimRequestDomainContacts**](DomainsV1PortfolioClaimRequestDomainContacts.md) |  | [optional] 
**should_keep_ns** | **bool** | Keep the existing nameservers of the domain | [optional] [default to True]

## Example

```python
from hostinger_api.models.domains_v1_transfer_transfer_request import DomainsV1TransferTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1TransferTransferRequest from a JSON string
domains_v1_transfer_transfer_request_instance = DomainsV1TransferTransferRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1TransferTransferRequest.to_json())

# convert the object into a dict
domains_v1_transfer_transfer_request_dict = domains_v1_transfer_transfer_request_instance.to_dict()
# create an instance of DomainsV1TransferTransferRequest from a dict
domains_v1_transfer_transfer_request_from_dict = DomainsV1TransferTransferRequest.from_dict(domains_v1_transfer_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


