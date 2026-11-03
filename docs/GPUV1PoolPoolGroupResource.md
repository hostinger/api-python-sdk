# GPUV1PoolPoolGroupResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | GPU pool group ID | [optional] 
**name** | **str** |  | [optional] 
**vram** | **int** | Total VRAM in bytes | [optional] 
**is_available** | **bool** | Whether the group has any available pools | [optional] 
**min_price_per_hour** | **float** | Lowest hourly price of the group instance types, in the requested currency | [optional] 
**pools** | [**List[GPUV1PoolPoolResource]**](GPUV1PoolPoolResource.md) | Array of [&#x60;GPU.V1.Pool.PoolResource&#x60;](#model/gpuv1poolpoolresource) | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_pool_pool_group_resource import GPUV1PoolPoolGroupResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1PoolPoolGroupResource from a JSON string
gpuv1_pool_pool_group_resource_instance = GPUV1PoolPoolGroupResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1PoolPoolGroupResource.to_json())

# convert the object into a dict
gpuv1_pool_pool_group_resource_dict = gpuv1_pool_pool_group_resource_instance.to_dict()
# create an instance of GPUV1PoolPoolGroupResource from a dict
gpuv1_pool_pool_group_resource_from_dict = GPUV1PoolPoolGroupResource.from_dict(gpuv1_pool_pool_group_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


