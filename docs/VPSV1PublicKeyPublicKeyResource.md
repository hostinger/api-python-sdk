# VPSV1PublicKeyPublicKeyResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Public key ID | [optional] 
**name** | **str** | Public key name | [optional] 
**key** | **str** | Public key content | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_public_key_public_key_resource import VPSV1PublicKeyPublicKeyResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1PublicKeyPublicKeyResource from a JSON string
vpsv1_public_key_public_key_resource_instance = VPSV1PublicKeyPublicKeyResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1PublicKeyPublicKeyResource.to_json())

# convert the object into a dict
vpsv1_public_key_public_key_resource_dict = vpsv1_public_key_public_key_resource_instance.to_dict()
# create an instance of VPSV1PublicKeyPublicKeyResource from a dict
vpsv1_public_key_public_key_resource_from_dict = VPSV1PublicKeyPublicKeyResource.from_dict(vpsv1_public_key_public_key_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


