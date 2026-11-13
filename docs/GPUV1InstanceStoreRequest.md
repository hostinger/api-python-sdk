# GPUV1InstanceStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_instance_id** | **int** | Instance type ID from the pool instance types list | 
**os_template_id** | **int** | OS template ID available for the selected instance type | 
**name** | **str** | Instance name, unique among your instances. Letters, numbers, dashes and underscores only | 
**public_keys** | **List[str]** | SSH public keys to add to the instance | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_instance_store_request import GPUV1InstanceStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1InstanceStoreRequest from a JSON string
gpuv1_instance_store_request_instance = GPUV1InstanceStoreRequest.from_json(json)
# print the JSON string representation of the object
print(GPUV1InstanceStoreRequest.to_json())

# convert the object into a dict
gpuv1_instance_store_request_dict = gpuv1_instance_store_request_instance.to_dict()
# create an instance of GPUV1InstanceStoreRequest from a dict
gpuv1_instance_store_request_from_dict = GPUV1InstanceStoreRequest.from_dict(gpuv1_instance_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


