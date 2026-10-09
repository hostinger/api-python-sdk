# VPSV1SshKeyStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | SSH public keys in OpenSSH format to add | 

## Example

```python
from hostinger_api.models.vpsv1_ssh_key_store_request import VPSV1SshKeyStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1SshKeyStoreRequest from a JSON string
vpsv1_ssh_key_store_request_instance = VPSV1SshKeyStoreRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1SshKeyStoreRequest.to_json())

# convert the object into a dict
vpsv1_ssh_key_store_request_dict = vpsv1_ssh_key_store_request_instance.to_dict()
# create an instance of VPSV1SshKeyStoreRequest from a dict
vpsv1_ssh_key_store_request_from_dict = VPSV1SshKeyStoreRequest.from_dict(vpsv1_ssh_key_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


