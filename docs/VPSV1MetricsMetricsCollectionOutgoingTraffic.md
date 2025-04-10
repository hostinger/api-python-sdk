# VPSV1MetricsMetricsCollectionOutgoingTraffic

Outgoing traffic in bytes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Measurement unit | [optional] 
**usage** | **object** | Object, containing UNIX timestamps as a key and measurement as a value. | [optional] 

## Example

```python
from @hostinger/api.models.vpsv1_metrics_metrics_collection_outgoing_traffic import VPSV1MetricsMetricsCollectionOutgoingTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1MetricsMetricsCollectionOutgoingTraffic from a JSON string
vpsv1_metrics_metrics_collection_outgoing_traffic_instance = VPSV1MetricsMetricsCollectionOutgoingTraffic.from_json(json)
# print the JSON string representation of the object
print(VPSV1MetricsMetricsCollectionOutgoingTraffic.to_json())

# convert the object into a dict
vpsv1_metrics_metrics_collection_outgoing_traffic_dict = vpsv1_metrics_metrics_collection_outgoing_traffic_instance.to_dict()
# create an instance of VPSV1MetricsMetricsCollectionOutgoingTraffic from a dict
vpsv1_metrics_metrics_collection_outgoing_traffic_from_dict = VPSV1MetricsMetricsCollectionOutgoingTraffic.from_dict(vpsv1_metrics_metrics_collection_outgoing_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


