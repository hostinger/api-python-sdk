# HostingV1CronJobsCreateCronJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** | Cron schedule expression (for example \&quot;0 2 * * *\&quot; runs daily at 02:00). | 
**command** | **str** | Command to execute on the schedule. | 

## Example

```python
from hostinger_api.models.hosting_v1_cron_jobs_create_cron_job_request import HostingV1CronJobsCreateCronJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1CronJobsCreateCronJobRequest from a JSON string
hosting_v1_cron_jobs_create_cron_job_request_instance = HostingV1CronJobsCreateCronJobRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1CronJobsCreateCronJobRequest.to_json())

# convert the object into a dict
hosting_v1_cron_jobs_create_cron_job_request_dict = hosting_v1_cron_jobs_create_cron_job_request_instance.to_dict()
# create an instance of HostingV1CronJobsCreateCronJobRequest from a dict
hosting_v1_cron_jobs_create_cron_job_request_from_dict = HostingV1CronJobsCreateCronJobRequest.from_dict(hosting_v1_cron_jobs_create_cron_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


