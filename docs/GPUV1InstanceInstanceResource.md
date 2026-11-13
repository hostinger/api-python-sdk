# GPUV1InstanceInstanceResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | GPU instance ID | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**action_lock** | **str** | Whether an action is in progress on the instance | [optional] 
**pool** | [**GPUV1PoolPoolResource**](GPUV1PoolPoolResource.md) |  | [optional] 
**pool_instance** | [**GPUV1PoolPoolInstanceResource**](GPUV1PoolPoolInstanceResource.md) |  | [optional] 
**os_template** | [**GPUV1OsTemplateOsTemplateResource**](GPUV1OsTemplateOsTemplateResource.md) |  | [optional] 
**ssh_keys** | [**List[GPUV1SshKeySshKeyResource]**](GPUV1SshKeySshKeyResource.md) | Array of [&#x60;GPU.V1.SshKey.SshKeyResource&#x60;](#model/gpuv1sshkeysshkeyresource) | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_instance_instance_resource import GPUV1InstanceInstanceResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1InstanceInstanceResource from a JSON string
gpuv1_instance_instance_resource_instance = GPUV1InstanceInstanceResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1InstanceInstanceResource.to_json())

# convert the object into a dict
gpuv1_instance_instance_resource_dict = gpuv1_instance_instance_resource_instance.to_dict()
# create an instance of GPUV1InstanceInstanceResource from a dict
gpuv1_instance_instance_resource_from_dict = GPUV1InstanceInstanceResource.from_dict(gpuv1_instance_instance_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


