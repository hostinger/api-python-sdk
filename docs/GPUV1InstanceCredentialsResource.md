# GPUV1InstanceCredentialsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | SSH host | [optional] 
**port** | **int** | SSH port | [optional] 
**username** | **str** | SSH username | [optional] 
**password** | **str** | SSH password | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_instance_credentials_resource import GPUV1InstanceCredentialsResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1InstanceCredentialsResource from a JSON string
gpuv1_instance_credentials_resource_instance = GPUV1InstanceCredentialsResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1InstanceCredentialsResource.to_json())

# convert the object into a dict
gpuv1_instance_credentials_resource_dict = gpuv1_instance_credentials_resource_instance.to_dict()
# create an instance of GPUV1InstanceCredentialsResource from a dict
gpuv1_instance_credentials_resource_from_dict = GPUV1InstanceCredentialsResource.from_dict(gpuv1_instance_credentials_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


