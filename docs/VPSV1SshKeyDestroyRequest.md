# VPSV1SshKeyDestroyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | SSH public keys in OpenSSH format to remove | 

## Example

```python
from hostinger_api.models.vpsv1_ssh_key_destroy_request import VPSV1SshKeyDestroyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1SshKeyDestroyRequest from a JSON string
vpsv1_ssh_key_destroy_request_instance = VPSV1SshKeyDestroyRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1SshKeyDestroyRequest.to_json())

# convert the object into a dict
vpsv1_ssh_key_destroy_request_dict = vpsv1_ssh_key_destroy_request_instance.to_dict()
# create an instance of VPSV1SshKeyDestroyRequest from a dict
vpsv1_ssh_key_destroy_request_from_dict = VPSV1SshKeyDestroyRequest.from_dict(vpsv1_ssh_key_destroy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


