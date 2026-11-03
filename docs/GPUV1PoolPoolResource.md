# GPUV1PoolPoolResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | GPU pool ID | [optional] 
**name** | **str** |  | [optional] 
**gpus** | **int** | Number of GPUs | [optional] 
**vram** | **int** | Total VRAM in bytes | [optional] 
**is_available** | **bool** | Whether the pool has available instances for booking | [optional] 
**region** | [**GPUV1RegionRegionResource**](GPUV1RegionRegionResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_pool_pool_resource import GPUV1PoolPoolResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1PoolPoolResource from a JSON string
gpuv1_pool_pool_resource_instance = GPUV1PoolPoolResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1PoolPoolResource.to_json())

# convert the object into a dict
gpuv1_pool_pool_resource_dict = gpuv1_pool_pool_resource_instance.to_dict()
# create an instance of GPUV1PoolPoolResource from a dict
gpuv1_pool_pool_resource_from_dict = GPUV1PoolPoolResource.from_dict(gpuv1_pool_pool_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


