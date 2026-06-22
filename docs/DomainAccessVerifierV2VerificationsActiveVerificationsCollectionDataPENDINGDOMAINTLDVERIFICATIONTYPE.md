# DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE

Verification type (\"NAMESERVERS\" or \"TXT\"). Only verification types that exist for this domain will be present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | **List[str]** | Verification records | [optional] 
**last_verification_attempt** | **str** | Datetime when last verification attempt occurred | [optional] 
**next_verification_attempt** | **str** | Datetime when next verification attempt will occur | [optional] 
**verification_expiration** | **str** | Datetime when verification expires | [optional] 

## Example

```python
from hostinger_api.models.domain_access_verifier_v2_verifications_active_verifications_collection_data_pendingdomaintldverificationtype import DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE from a JSON string
domain_access_verifier_v2_verifications_active_verifications_collection_data_pendingdomaintldverificationtype_instance = DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE.from_json(json)
# print the JSON string representation of the object
print(DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE.to_json())

# convert the object into a dict
domain_access_verifier_v2_verifications_active_verifications_collection_data_pendingdomaintldverificationtype_dict = domain_access_verifier_v2_verifications_active_verifications_collection_data_pendingdomaintldverificationtype_instance.to_dict()
# create an instance of DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE from a dict
domain_access_verifier_v2_verifications_active_verifications_collection_data_pendingdomaintldverificationtype_from_dict = DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE.from_dict(domain_access_verifier_v2_verifications_active_verifications_collection_data_pendingdomaintldverificationtype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


