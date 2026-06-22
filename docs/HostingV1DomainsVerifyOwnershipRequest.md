# HostingV1DomainsVerifyOwnershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain to verify ownership for | 

## Example

```python
from hostinger_api.models.hosting_v1_domains_verify_ownership_request import HostingV1DomainsVerifyOwnershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DomainsVerifyOwnershipRequest from a JSON string
hosting_v1_domains_verify_ownership_request_instance = HostingV1DomainsVerifyOwnershipRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1DomainsVerifyOwnershipRequest.to_json())

# convert the object into a dict
hosting_v1_domains_verify_ownership_request_dict = hosting_v1_domains_verify_ownership_request_instance.to_dict()
# create an instance of HostingV1DomainsVerifyOwnershipRequest from a dict
hosting_v1_domains_verify_ownership_request_from_dict = HostingV1DomainsVerifyOwnershipRequest.from_dict(hosting_v1_domains_verify_ownership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


