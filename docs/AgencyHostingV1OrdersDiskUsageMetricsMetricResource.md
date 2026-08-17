# AgencyHostingV1OrdersDiskUsageMetricsMetricResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_bytes** | **int** | Disk usage in bytes at this sample | [optional] 
**inodes** | **int** | Number of inodes used at this sample | [optional] 
**timestamp** | **int** | Unix timestamp of the sample | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_disk_usage_metrics_metric_resource import AgencyHostingV1OrdersDiskUsageMetricsMetricResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersDiskUsageMetricsMetricResource from a JSON string
agency_hosting_v1_orders_disk_usage_metrics_metric_resource_instance = AgencyHostingV1OrdersDiskUsageMetricsMetricResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersDiskUsageMetricsMetricResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_disk_usage_metrics_metric_resource_dict = agency_hosting_v1_orders_disk_usage_metrics_metric_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersDiskUsageMetricsMetricResource from a dict
agency_hosting_v1_orders_disk_usage_metrics_metric_resource_from_dict = AgencyHostingV1OrdersDiskUsageMetricsMetricResource.from_dict(agency_hosting_v1_orders_disk_usage_metrics_metric_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


