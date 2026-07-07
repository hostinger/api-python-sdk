# VPSV1PublicKeyListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VPSV1PublicKeyPublicKeyResource]**](VPSV1PublicKeyPublicKeyResource.md) | Array of [&#x60;VPS.V1.PublicKey.PublicKeyResource&#x60;](#model/vpsv1publickeypublickeyresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_public_key_list_response import VPSV1PublicKeyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1PublicKeyListResponse from a JSON string
vpsv1_public_key_list_response_instance = VPSV1PublicKeyListResponse.from_json(json)
# print the JSON string representation of the object
print(VPSV1PublicKeyListResponse.to_json())

# convert the object into a dict
vpsv1_public_key_list_response_dict = vpsv1_public_key_list_response_instance.to_dict()
# create an instance of VPSV1PublicKeyListResponse from a dict
vpsv1_public_key_list_response_from_dict = VPSV1PublicKeyListResponse.from_dict(vpsv1_public_key_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


