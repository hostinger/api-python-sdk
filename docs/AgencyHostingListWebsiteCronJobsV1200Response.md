# AgencyHostingListWebsiteCronJobsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AgencyHostingV1WebsitesCronJobsCronJobResource]**](AgencyHostingV1WebsitesCronJobsCronJobResource.md) | Array of [&#x60;AgencyHosting.V1.Websites.CronJobs.CronJobResource&#x60;](#model/agencyhostingv1websitescronjobscronjobresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_list_website_cron_jobs_v1200_response import AgencyHostingListWebsiteCronJobsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingListWebsiteCronJobsV1200Response from a JSON string
agency_hosting_list_website_cron_jobs_v1200_response_instance = AgencyHostingListWebsiteCronJobsV1200Response.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingListWebsiteCronJobsV1200Response.to_json())

# convert the object into a dict
agency_hosting_list_website_cron_jobs_v1200_response_dict = agency_hosting_list_website_cron_jobs_v1200_response_instance.to_dict()
# create an instance of AgencyHostingListWebsiteCronJobsV1200Response from a dict
agency_hosting_list_website_cron_jobs_v1200_response_from_dict = AgencyHostingListWebsiteCronJobsV1200Response.from_dict(agency_hosting_list_website_cron_jobs_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


