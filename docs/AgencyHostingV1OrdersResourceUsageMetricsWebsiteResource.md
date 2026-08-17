# AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Website UID | [optional] 
**domains** | **List[str]** | Domains associated with the website | [optional] 
**metrics** | [**List[AgencyHostingV1OrdersResourceUsageMetricsMetricResource]**](AgencyHostingV1OrdersResourceUsageMetricsMetricResource.md) | Array of [&#x60;AgencyHosting.V1.Orders.ResourceUsageMetrics.MetricResource&#x60;](#model/agencyhostingv1ordersresourceusagemetricsmetricresource) | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_resource_usage_metrics_website_resource import AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource from a JSON string
agency_hosting_v1_orders_resource_usage_metrics_website_resource_instance = AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_resource_usage_metrics_website_resource_dict = agency_hosting_v1_orders_resource_usage_metrics_website_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource from a dict
agency_hosting_v1_orders_resource_usage_metrics_website_resource_from_dict = AgencyHostingV1OrdersResourceUsageMetricsWebsiteResource.from_dict(agency_hosting_v1_orders_resource_usage_metrics_website_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


