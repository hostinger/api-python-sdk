# GPUV1RegionRegionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Region ID | [optional] 
**name** | **str** | Region name | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** | ISO 3166-1 alpha-2 country code | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_region_region_resource import GPUV1RegionRegionResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1RegionRegionResource from a JSON string
gpuv1_region_region_resource_instance = GPUV1RegionRegionResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1RegionRegionResource.to_json())

# convert the object into a dict
gpuv1_region_region_resource_dict = gpuv1_region_region_resource_instance.to_dict()
# create an instance of GPUV1RegionRegionResource from a dict
gpuv1_region_region_resource_from_dict = GPUV1RegionRegionResource.from_dict(gpuv1_region_region_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


