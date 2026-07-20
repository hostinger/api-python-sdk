# AgencyHostingV1WebsitesCronJobsCronJobResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier of the cron job. Use it to delete the cron job. | [optional] 
**time** | **str** | Cron schedule expression. | [optional] 
**command** | **str** | Command executed on the configured schedule. | [optional] 
**created_at** | **datetime** | Cron job creation timestamp. | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_cron_jobs_cron_job_resource import AgencyHostingV1WebsitesCronJobsCronJobResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesCronJobsCronJobResource from a JSON string
agency_hosting_v1_websites_cron_jobs_cron_job_resource_instance = AgencyHostingV1WebsitesCronJobsCronJobResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesCronJobsCronJobResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_cron_jobs_cron_job_resource_dict = agency_hosting_v1_websites_cron_jobs_cron_job_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesCronJobsCronJobResource from a dict
agency_hosting_v1_websites_cron_jobs_cron_job_resource_from_dict = AgencyHostingV1WebsitesCronJobsCronJobResource.from_dict(agency_hosting_v1_websites_cron_jobs_cron_job_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


