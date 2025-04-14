# VPSV1PublicKeyAttachRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | Public Key IDs to attach | 

## Example

```python
from hostinger-api.models.vpsv1_public_key_attach_request import VPSV1PublicKeyAttachRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1PublicKeyAttachRequest from a JSON string
vpsv1_public_key_attach_request_instance = VPSV1PublicKeyAttachRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1PublicKeyAttachRequest.to_json())

# convert the object into a dict
vpsv1_public_key_attach_request_dict = vpsv1_public_key_attach_request_instance.to_dict()
# create an instance of VPSV1PublicKeyAttachRequest from a dict
vpsv1_public_key_attach_request_from_dict = VPSV1PublicKeyAttachRequest.from_dict(vpsv1_public_key_attach_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


