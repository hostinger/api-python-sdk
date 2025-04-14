# VPSV1MetricsMetricsCollectionCpuUsage

CPU usage in percentage, 0 - 100%

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Measurement unit | [optional] 
**usage** | **object** | Object, containing UNIX timestamps as a key and measurement as a value. | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_metrics_metrics_collection_cpu_usage import VPSV1MetricsMetricsCollectionCpuUsage

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1MetricsMetricsCollectionCpuUsage from a JSON string
vpsv1_metrics_metrics_collection_cpu_usage_instance = VPSV1MetricsMetricsCollectionCpuUsage.from_json(json)
# print the JSON string representation of the object
print(VPSV1MetricsMetricsCollectionCpuUsage.to_json())

# convert the object into a dict
vpsv1_metrics_metrics_collection_cpu_usage_dict = vpsv1_metrics_metrics_collection_cpu_usage_instance.to_dict()
# create an instance of VPSV1MetricsMetricsCollectionCpuUsage from a dict
vpsv1_metrics_metrics_collection_cpu_usage_from_dict = VPSV1MetricsMetricsCollectionCpuUsage.from_dict(vpsv1_metrics_metrics_collection_cpu_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


