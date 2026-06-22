# DomainAccessVerifierV2VerificationsActiveVerificationsCollection

Returns active verifications (PENDING and VERIFIED) grouped by status and domain. Includes last and next verification attempt dates and expiration for PENDING verifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData**](DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData.md) |  | [optional] 

## Example

```python
from hostinger_api.models.domain_access_verifier_v2_verifications_active_verifications_collection import DomainAccessVerifierV2VerificationsActiveVerificationsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAccessVerifierV2VerificationsActiveVerificationsCollection from a JSON string
domain_access_verifier_v2_verifications_active_verifications_collection_instance = DomainAccessVerifierV2VerificationsActiveVerificationsCollection.from_json(json)
# print the JSON string representation of the object
print(DomainAccessVerifierV2VerificationsActiveVerificationsCollection.to_json())

# convert the object into a dict
domain_access_verifier_v2_verifications_active_verifications_collection_dict = domain_access_verifier_v2_verifications_active_verifications_collection_instance.to_dict()
# create an instance of DomainAccessVerifierV2VerificationsActiveVerificationsCollection from a dict
domain_access_verifier_v2_verifications_active_verifications_collection_from_dict = DomainAccessVerifierV2VerificationsActiveVerificationsCollection.from_dict(domain_access_verifier_v2_verifications_active_verifications_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


