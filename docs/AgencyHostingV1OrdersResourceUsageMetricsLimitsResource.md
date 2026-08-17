# AgencyHostingV1OrdersResourceUsageMetricsLimitsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_bytes** | **int** | Memory usage quota in bytes | [optional] 
**cpu_percent** | **int** | CPU usage quota in percent | [optional] 
**processes** | **int** | Process usage quota | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_resource_usage_metrics_limits_resource import AgencyHostingV1OrdersResourceUsageMetricsLimitsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersResourceUsageMetricsLimitsResource from a JSON string
agency_hosting_v1_orders_resource_usage_metrics_limits_resource_instance = AgencyHostingV1OrdersResourceUsageMetricsLimitsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersResourceUsageMetricsLimitsResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_resource_usage_metrics_limits_resource_dict = agency_hosting_v1_orders_resource_usage_metrics_limits_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersResourceUsageMetricsLimitsResource from a dict
agency_hosting_v1_orders_resource_usage_metrics_limits_resource_from_dict = AgencyHostingV1OrdersResourceUsageMetricsLimitsResource.from_dict(agency_hosting_v1_orders_resource_usage_metrics_limits_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


