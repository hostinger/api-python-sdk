# DomainsV1TransferTransferResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**status** | **str** | Transfer status | [optional] 
**initiated_at** | **datetime** | When the transfer was initiated | [optional] 
**completed_at** | **datetime** | When the transfer completed | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_transfer_transfer_resource import DomainsV1TransferTransferResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1TransferTransferResource from a JSON string
domains_v1_transfer_transfer_resource_instance = DomainsV1TransferTransferResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1TransferTransferResource.to_json())

# convert the object into a dict
domains_v1_transfer_transfer_resource_dict = domains_v1_transfer_transfer_resource_instance.to_dict()
# create an instance of DomainsV1TransferTransferResource from a dict
domains_v1_transfer_transfer_resource_from_dict = DomainsV1TransferTransferResource.from_dict(domains_v1_transfer_transfer_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


