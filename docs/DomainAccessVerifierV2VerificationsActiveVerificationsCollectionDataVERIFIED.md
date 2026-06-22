# DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED

Verified verifications grouped by domain. Keys are domain names (e.g., \"byte.tld\"). This property will not be returned if no verified verifications are found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_tld** | [**DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIEDDOMAINTLD**](DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIEDDOMAINTLD.md) |  | [optional] 

## Example

```python
from hostinger_api.models.domain_access_verifier_v2_verifications_active_verifications_collection_data_verified import DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED from a JSON string
domain_access_verifier_v2_verifications_active_verifications_collection_data_verified_instance = DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED.from_json(json)
# print the JSON string representation of the object
print(DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED.to_json())

# convert the object into a dict
domain_access_verifier_v2_verifications_active_verifications_collection_data_verified_dict = domain_access_verifier_v2_verifications_active_verifications_collection_data_verified_instance.to_dict()
# create an instance of DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED from a dict
domain_access_verifier_v2_verifications_active_verifications_collection_data_verified_from_dict = DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED.from_dict(domain_access_verifier_v2_verifications_active_verifications_collection_data_verified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


