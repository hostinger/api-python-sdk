# VPSV1MetricsMetricsCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_usage** | [**VPSV1MetricsMetricsResource**](VPSV1MetricsMetricsResource.md) |  | [optional] 
**ram_usage** | [**VPSV1MetricsMetricsResource**](VPSV1MetricsMetricsResource.md) |  | [optional] 
**disk_space** | [**VPSV1MetricsMetricsResource**](VPSV1MetricsMetricsResource.md) |  | [optional] 
**outgoing_traffic** | [**VPSV1MetricsMetricsResource**](VPSV1MetricsMetricsResource.md) |  | [optional] 
**incoming_traffic** | [**VPSV1MetricsMetricsResource**](VPSV1MetricsMetricsResource.md) |  | [optional] 
**uptime** | [**VPSV1MetricsMetricsResource**](VPSV1MetricsMetricsResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_metrics_metrics_collection import VPSV1MetricsMetricsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1MetricsMetricsCollection from a JSON string
vpsv1_metrics_metrics_collection_instance = VPSV1MetricsMetricsCollection.from_json(json)
# print the JSON string representation of the object
print(VPSV1MetricsMetricsCollection.to_json())

# convert the object into a dict
vpsv1_metrics_metrics_collection_dict = vpsv1_metrics_metrics_collection_instance.to_dict()
# create an instance of VPSV1MetricsMetricsCollection from a dict
vpsv1_metrics_metrics_collection_from_dict = VPSV1MetricsMetricsCollection.from_dict(vpsv1_metrics_metrics_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


