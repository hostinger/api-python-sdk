# HostingV1CronJobsCronJobOutputResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** | Output captured from the last cron job execution. Empty when the cron job has not run yet. | 

## Example

```python
from hostinger_api.models.hosting_v1_cron_jobs_cron_job_output_resource import HostingV1CronJobsCronJobOutputResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1CronJobsCronJobOutputResource from a JSON string
hosting_v1_cron_jobs_cron_job_output_resource_instance = HostingV1CronJobsCronJobOutputResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1CronJobsCronJobOutputResource.to_json())

# convert the object into a dict
hosting_v1_cron_jobs_cron_job_output_resource_dict = hosting_v1_cron_jobs_cron_job_output_resource_instance.to_dict()
# create an instance of HostingV1CronJobsCronJobOutputResource from a dict
hosting_v1_cron_jobs_cron_job_output_resource_from_dict = HostingV1CronJobsCronJobOutputResource.from_dict(hosting_v1_cron_jobs_cron_job_output_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


