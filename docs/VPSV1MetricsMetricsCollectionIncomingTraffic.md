# VPSV1MetricsMetricsCollectionIncomingTraffic

Incoming traffic in bytes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Measurement unit | [optional] 
**usage** | **object** | Object, containing UNIX timestamps as a key and measurement as a value. | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_metrics_metrics_collection_incoming_traffic import VPSV1MetricsMetricsCollectionIncomingTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1MetricsMetricsCollectionIncomingTraffic from a JSON string
vpsv1_metrics_metrics_collection_incoming_traffic_instance = VPSV1MetricsMetricsCollectionIncomingTraffic.from_json(json)
# print the JSON string representation of the object
print(VPSV1MetricsMetricsCollectionIncomingTraffic.to_json())

# convert the object into a dict
vpsv1_metrics_metrics_collection_incoming_traffic_dict = vpsv1_metrics_metrics_collection_incoming_traffic_instance.to_dict()
# create an instance of VPSV1MetricsMetricsCollectionIncomingTraffic from a dict
vpsv1_metrics_metrics_collection_incoming_traffic_from_dict = VPSV1MetricsMetricsCollectionIncomingTraffic.from_dict(vpsv1_metrics_metrics_collection_incoming_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


