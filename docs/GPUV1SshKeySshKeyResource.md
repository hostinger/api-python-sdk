# GPUV1SshKeySshKeyResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | SSH key ID | [optional] 
**name** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_ssh_key_ssh_key_resource import GPUV1SshKeySshKeyResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1SshKeySshKeyResource from a JSON string
gpuv1_ssh_key_ssh_key_resource_instance = GPUV1SshKeySshKeyResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1SshKeySshKeyResource.to_json())

# convert the object into a dict
gpuv1_ssh_key_ssh_key_resource_dict = gpuv1_ssh_key_ssh_key_resource_instance.to_dict()
# create an instance of GPUV1SshKeySshKeyResource from a dict
gpuv1_ssh_key_ssh_key_resource_from_dict = GPUV1SshKeySshKeyResource.from_dict(gpuv1_ssh_key_ssh_key_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


