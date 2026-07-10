# AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters

Plan parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_quota_bytes** | **int** | Disk quota in bytes | [optional] 
**inode_quota** | **int** | Inode quota | [optional] 
**cpu_cores** | **int** | CPU cores | [optional] 
**memory_quota_bytes** | **int** | Memory quota in bytes | [optional] 
**disk_iops_quota** | **int** | Disk IOPs quota | [optional] 
**process_quota** | **int** | Process quota | [optional] 
**website_quota** | **int** | Website quota | [optional] 
**max_databases_per_website** | **int** | Maximum number of databases per website | [optional] 
**is_cdn_available** | **bool** | Is CDN available | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_order_plan_resource_parameters import AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters from a JSON string
agency_hosting_v1_websites_website_order_plan_resource_parameters_instance = AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_order_plan_resource_parameters_dict = agency_hosting_v1_websites_website_order_plan_resource_parameters_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters from a dict
agency_hosting_v1_websites_website_order_plan_resource_parameters_from_dict = AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters.from_dict(agency_hosting_v1_websites_website_order_plan_resource_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


