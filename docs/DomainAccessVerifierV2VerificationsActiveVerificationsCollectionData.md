# DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData

List of active verifications by status. If no verifications are found, this will return an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | [**DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDING**](DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDING.md) |  | [optional] 
**verified** | [**DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED**](DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED.md) |  | [optional] 

## Example

```python
from hostinger_api.models.domain_access_verifier_v2_verifications_active_verifications_collection_data import DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData from a JSON string
domain_access_verifier_v2_verifications_active_verifications_collection_data_instance = DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData.from_json(json)
# print the JSON string representation of the object
print(DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData.to_json())

# convert the object into a dict
domain_access_verifier_v2_verifications_active_verifications_collection_data_dict = domain_access_verifier_v2_verifications_active_verifications_collection_data_instance.to_dict()
# create an instance of DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData from a dict
domain_access_verifier_v2_verifications_active_verifications_collection_data_from_dict = DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData.from_dict(domain_access_verifier_v2_verifications_active_verifications_collection_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


