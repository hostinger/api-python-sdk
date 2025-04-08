# VPSGetPublicKeyListV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VPSV1PublicKeyPublicKeyResource]**](VPSV1PublicKeyPublicKeyResource.md) | Array of [&#x60;VPS.V1.PublicKey.PublicKeyResource&#x60;](#model/vpsv1publickeypublickeyresource) | [optional] 
**meta** | [**VPSGetFirewallListV1200ResponseMeta**](VPSGetFirewallListV1200ResponseMeta.md) |  | [optional] 

## Example

```python
from hostinger-api.models.vps_get_public_key_list_v1200_response import VPSGetPublicKeyListV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VPSGetPublicKeyListV1200Response from a JSON string
vps_get_public_key_list_v1200_response_instance = VPSGetPublicKeyListV1200Response.from_json(json)
# print the JSON string representation of the object
print(VPSGetPublicKeyListV1200Response.to_json())

# convert the object into a dict
vps_get_public_key_list_v1200_response_dict = vps_get_public_key_list_v1200_response_instance.to_dict()
# create an instance of VPSGetPublicKeyListV1200Response from a dict
vps_get_public_key_list_v1200_response_from_dict = VPSGetPublicKeyListV1200Response.from_dict(vps_get_public_key_list_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


