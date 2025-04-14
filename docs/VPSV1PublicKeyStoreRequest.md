# VPSV1PublicKeyStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**key** | **str** |  | 

## Example

```python
from hostinger_api.models.vpsv1_public_key_store_request import VPSV1PublicKeyStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1PublicKeyStoreRequest from a JSON string
vpsv1_public_key_store_request_instance = VPSV1PublicKeyStoreRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1PublicKeyStoreRequest.to_json())

# convert the object into a dict
vpsv1_public_key_store_request_dict = vpsv1_public_key_store_request_instance.to_dict()
# create an instance of VPSV1PublicKeyStoreRequest from a dict
vpsv1_public_key_store_request_from_dict = VPSV1PublicKeyStoreRequest.from_dict(vpsv1_public_key_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


