# VPSV1SshKeySshKeyResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | SSH public key in OpenSSH format | [optional] 
**type** | **str** | SSH key type | [optional] 
**data** | **str** | SSH key data (base64 encoded public key) | [optional] 
**name** | **str** | SSH key comment/name | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_ssh_key_ssh_key_resource import VPSV1SshKeySshKeyResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1SshKeySshKeyResource from a JSON string
vpsv1_ssh_key_ssh_key_resource_instance = VPSV1SshKeySshKeyResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1SshKeySshKeyResource.to_json())

# convert the object into a dict
vpsv1_ssh_key_ssh_key_resource_dict = vpsv1_ssh_key_ssh_key_resource_instance.to_dict()
# create an instance of VPSV1SshKeySshKeyResource from a dict
vpsv1_ssh_key_ssh_key_resource_from_dict = VPSV1SshKeySshKeyResource.from_dict(vpsv1_ssh_key_ssh_key_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


