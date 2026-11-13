# GPUV1MetricsMetricsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Unix timestamp of the measurement | [optional] 
**cpu_percentage** | **float** | CPU utilisation in percent | [optional] 
**memory_used** | **float** | Used memory in bytes | [optional] 
**gpu_percentage** | **float** | GPU utilisation in percent | [optional] 
**gpu_memory_used** | **float** | Used GPU memory in bytes | [optional] 
**gpu_tflops** | **float** | GPU throughput in TFLOPS | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_metrics_metrics_resource import GPUV1MetricsMetricsResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1MetricsMetricsResource from a JSON string
gpuv1_metrics_metrics_resource_instance = GPUV1MetricsMetricsResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1MetricsMetricsResource.to_json())

# convert the object into a dict
gpuv1_metrics_metrics_resource_dict = gpuv1_metrics_metrics_resource_instance.to_dict()
# create an instance of GPUV1MetricsMetricsResource from a dict
gpuv1_metrics_metrics_resource_from_dict = GPUV1MetricsMetricsResource.from_dict(gpuv1_metrics_metrics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


