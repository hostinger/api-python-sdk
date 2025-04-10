# VPSV1MetricsMetricsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Measurement unit | [optional] 
**usage** | **object** | Object, containing UNIX timestamps as a key and measurement as a value. | [optional] 

## Example

```python
from @hostinger/api.models.vpsv1_metrics_metrics_resource import VPSV1MetricsMetricsResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1MetricsMetricsResource from a JSON string
vpsv1_metrics_metrics_resource_instance = VPSV1MetricsMetricsResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1MetricsMetricsResource.to_json())

# convert the object into a dict
vpsv1_metrics_metrics_resource_dict = vpsv1_metrics_metrics_resource_instance.to_dict()
# create an instance of VPSV1MetricsMetricsResource from a dict
vpsv1_metrics_metrics_resource_from_dict = VPSV1MetricsMetricsResource.from_dict(vpsv1_metrics_metrics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


