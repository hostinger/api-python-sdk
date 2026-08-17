# AgencyHostingV1OrdersDiskUsageMetricsMetricsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**AgencyHostingV1OrdersDiskUsageMetricsLimitsResource**](AgencyHostingV1OrdersDiskUsageMetricsLimitsResource.md) |  | [optional] 
**metrics** | [**List[AgencyHostingV1OrdersDiskUsageMetricsMetricResource]**](AgencyHostingV1OrdersDiskUsageMetricsMetricResource.md) | Array of [&#x60;AgencyHosting.V1.Orders.DiskUsageMetrics.MetricResource&#x60;](#model/agencyhostingv1ordersdiskusagemetricsmetricresource) | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_disk_usage_metrics_metrics_resource import AgencyHostingV1OrdersDiskUsageMetricsMetricsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersDiskUsageMetricsMetricsResource from a JSON string
agency_hosting_v1_orders_disk_usage_metrics_metrics_resource_instance = AgencyHostingV1OrdersDiskUsageMetricsMetricsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersDiskUsageMetricsMetricsResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_disk_usage_metrics_metrics_resource_dict = agency_hosting_v1_orders_disk_usage_metrics_metrics_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersDiskUsageMetricsMetricsResource from a dict
agency_hosting_v1_orders_disk_usage_metrics_metrics_resource_from_dict = AgencyHostingV1OrdersDiskUsageMetricsMetricsResource.from_dict(agency_hosting_v1_orders_disk_usage_metrics_metrics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


