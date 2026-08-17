# AgencyHostingV1OrdersResourceUsageMetricsMetricsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**AgencyHostingV1OrdersResourceUsageMetricsLimitsResource**](AgencyHostingV1OrdersResourceUsageMetricsLimitsResource.md) |  | [optional] 
**metrics** | [**List[AgencyHostingV1OrdersResourceUsageMetricsMetricResource]**](AgencyHostingV1OrdersResourceUsageMetricsMetricResource.md) | Array of [&#x60;AgencyHosting.V1.Orders.ResourceUsageMetrics.MetricResource&#x60;](#model/agencyhostingv1ordersresourceusagemetricsmetricresource) | [optional] 
**websites** | [**List[AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource]**](AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource.md) | Array of [&#x60;AgencyHosting.V1.Orders.ResourceUsageMetrics.WebsiteResource&#x60;](#model/agencyhostingv1ordersresourceusagemetricswebsiteresource) | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_resource_usage_metrics_metrics_resource import AgencyHostingV1OrdersResourceUsageMetricsMetricsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersResourceUsageMetricsMetricsResource from a JSON string
agency_hosting_v1_orders_resource_usage_metrics_metrics_resource_instance = AgencyHostingV1OrdersResourceUsageMetricsMetricsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersResourceUsageMetricsMetricsResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_resource_usage_metrics_metrics_resource_dict = agency_hosting_v1_orders_resource_usage_metrics_metrics_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersResourceUsageMetricsMetricsResource from a dict
agency_hosting_v1_orders_resource_usage_metrics_metrics_resource_from_dict = AgencyHostingV1OrdersResourceUsageMetricsMetricsResource.from_dict(agency_hosting_v1_orders_resource_usage_metrics_metrics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


