# AgencyHostingV1WebsitesCronJobsCreateCronJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** | Cron schedule expression (standard 5-field crontab syntax). | 
**command** | **str** | Command to run on the schedule. Must not contain pipe (|) or redirection (&lt;, &gt;) characters. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_cron_jobs_create_cron_job_request import AgencyHostingV1WebsitesCronJobsCreateCronJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesCronJobsCreateCronJobRequest from a JSON string
agency_hosting_v1_websites_cron_jobs_create_cron_job_request_instance = AgencyHostingV1WebsitesCronJobsCreateCronJobRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesCronJobsCreateCronJobRequest.to_json())

# convert the object into a dict
agency_hosting_v1_websites_cron_jobs_create_cron_job_request_dict = agency_hosting_v1_websites_cron_jobs_create_cron_job_request_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesCronJobsCreateCronJobRequest from a dict
agency_hosting_v1_websites_cron_jobs_create_cron_job_request_from_dict = AgencyHostingV1WebsitesCronJobsCreateCronJobRequest.from_dict(agency_hosting_v1_websites_cron_jobs_create_cron_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


