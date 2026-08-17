# AgencyHostingV1OrdersDiskUsageMetricsLimitsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_bytes** | **int** | Disk usage quota in bytes | [optional] 
**inodes** | **int** | Inodes quota | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_disk_usage_metrics_limits_resource import AgencyHostingV1OrdersDiskUsageMetricsLimitsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersDiskUsageMetricsLimitsResource from a JSON string
agency_hosting_v1_orders_disk_usage_metrics_limits_resource_instance = AgencyHostingV1OrdersDiskUsageMetricsLimitsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersDiskUsageMetricsLimitsResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_disk_usage_metrics_limits_resource_dict = agency_hosting_v1_orders_disk_usage_metrics_limits_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersDiskUsageMetricsLimitsResource from a dict
agency_hosting_v1_orders_disk_usage_metrics_limits_resource_from_dict = AgencyHostingV1OrdersDiskUsageMetricsLimitsResource.from_dict(agency_hosting_v1_orders_disk_usage_metrics_limits_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


