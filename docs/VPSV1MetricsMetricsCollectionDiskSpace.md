# VPSV1MetricsMetricsCollectionDiskSpace

Disk space usage in bytes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Measurement unit | [optional] 
**usage** | **object** | Object, containing UNIX timestamps as a key and measurement as a value. | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_metrics_metrics_collection_disk_space import VPSV1MetricsMetricsCollectionDiskSpace

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1MetricsMetricsCollectionDiskSpace from a JSON string
vpsv1_metrics_metrics_collection_disk_space_instance = VPSV1MetricsMetricsCollectionDiskSpace.from_json(json)
# print the JSON string representation of the object
print(VPSV1MetricsMetricsCollectionDiskSpace.to_json())

# convert the object into a dict
vpsv1_metrics_metrics_collection_disk_space_dict = vpsv1_metrics_metrics_collection_disk_space_instance.to_dict()
# create an instance of VPSV1MetricsMetricsCollectionDiskSpace from a dict
vpsv1_metrics_metrics_collection_disk_space_from_dict = VPSV1MetricsMetricsCollectionDiskSpace.from_dict(vpsv1_metrics_metrics_collection_disk_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


