# AgencyHostingV1OrdersResourceUsageMetricsMetricResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_percent** | **float** | CPU usage percentage at this sample | [optional] 
**memory_bytes** | **int** | Memory usage in bytes at this sample | [optional] 
**processes** | **int** | Number of processes at this sample | [optional] 
**timestamp** | **int** | Unix timestamp of the sample | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_resource_usage_metrics_metric_resource import AgencyHostingV1OrdersResourceUsageMetricsMetricResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersResourceUsageMetricsMetricResource from a JSON string
agency_hosting_v1_orders_resource_usage_metrics_metric_resource_instance = AgencyHostingV1OrdersResourceUsageMetricsMetricResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersResourceUsageMetricsMetricResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_resource_usage_metrics_metric_resource_dict = agency_hosting_v1_orders_resource_usage_metrics_metric_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersResourceUsageMetricsMetricResource from a dict
agency_hosting_v1_orders_resource_usage_metrics_metric_resource_from_dict = AgencyHostingV1OrdersResourceUsageMetricsMetricResource.from_dict(agency_hosting_v1_orders_resource_usage_metrics_metric_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


