# DomainAccessVerifierV2VerificationsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | The list of domains for which to get verification details for. | 

## Example

```python
from hostinger_api.models.domain_access_verifier_v2_verifications_list_request import DomainAccessVerifierV2VerificationsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAccessVerifierV2VerificationsListRequest from a JSON string
domain_access_verifier_v2_verifications_list_request_instance = DomainAccessVerifierV2VerificationsListRequest.from_json(json)
# print the JSON string representation of the object
print(DomainAccessVerifierV2VerificationsListRequest.to_json())

# convert the object into a dict
domain_access_verifier_v2_verifications_list_request_dict = domain_access_verifier_v2_verifications_list_request_instance.to_dict()
# create an instance of DomainAccessVerifierV2VerificationsListRequest from a dict
domain_access_verifier_v2_verifications_list_request_from_dict = DomainAccessVerifierV2VerificationsListRequest.from_dict(domain_access_verifier_v2_verifications_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


