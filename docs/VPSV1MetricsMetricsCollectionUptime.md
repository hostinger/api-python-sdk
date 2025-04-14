# VPSV1MetricsMetricsCollectionUptime

Uptime in milliseconds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Measurement unit | [optional] 
**usage** | **object** | Object, containing UNIX timestamps as a key and measurement as a value. | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_metrics_metrics_collection_uptime import VPSV1MetricsMetricsCollectionUptime

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1MetricsMetricsCollectionUptime from a JSON string
vpsv1_metrics_metrics_collection_uptime_instance = VPSV1MetricsMetricsCollectionUptime.from_json(json)
# print the JSON string representation of the object
print(VPSV1MetricsMetricsCollectionUptime.to_json())

# convert the object into a dict
vpsv1_metrics_metrics_collection_uptime_dict = vpsv1_metrics_metrics_collection_uptime_instance.to_dict()
# create an instance of VPSV1MetricsMetricsCollectionUptime from a dict
vpsv1_metrics_metrics_collection_uptime_from_dict = VPSV1MetricsMetricsCollectionUptime.from_dict(vpsv1_metrics_metrics_collection_uptime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


