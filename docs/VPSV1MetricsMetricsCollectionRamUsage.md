# VPSV1MetricsMetricsCollectionRamUsage

RAM usage in bytes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Measurement unit | [optional] 
**usage** | **object** | Object, containing UNIX timestamps as a key and measurement as a value. | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_metrics_metrics_collection_ram_usage import VPSV1MetricsMetricsCollectionRamUsage

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1MetricsMetricsCollectionRamUsage from a JSON string
vpsv1_metrics_metrics_collection_ram_usage_instance = VPSV1MetricsMetricsCollectionRamUsage.from_json(json)
# print the JSON string representation of the object
print(VPSV1MetricsMetricsCollectionRamUsage.to_json())

# convert the object into a dict
vpsv1_metrics_metrics_collection_ram_usage_dict = vpsv1_metrics_metrics_collection_ram_usage_instance.to_dict()
# create an instance of VPSV1MetricsMetricsCollectionRamUsage from a dict
vpsv1_metrics_metrics_collection_ram_usage_from_dict = VPSV1MetricsMetricsCollectionRamUsage.from_dict(vpsv1_metrics_metrics_collection_ram_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


