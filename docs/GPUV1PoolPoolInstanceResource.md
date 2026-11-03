# GPUV1PoolPoolInstanceResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | GPU pool instance type ID | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cpu_cores** | **int** | Number of CPU cores | [optional] 
**ram** | **int** | Total RAM in bytes | [optional] 
**storage** | **int** | Total storage in bytes | [optional] 
**price_per_hour** | **int** | Hourly price in cents (USD) | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_pool_pool_instance_resource import GPUV1PoolPoolInstanceResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1PoolPoolInstanceResource from a JSON string
gpuv1_pool_pool_instance_resource_instance = GPUV1PoolPoolInstanceResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1PoolPoolInstanceResource.to_json())

# convert the object into a dict
gpuv1_pool_pool_instance_resource_dict = gpuv1_pool_pool_instance_resource_instance.to_dict()
# create an instance of GPUV1PoolPoolInstanceResource from a dict
gpuv1_pool_pool_instance_resource_from_dict = GPUV1PoolPoolInstanceResource.from_dict(gpuv1_pool_pool_instance_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


