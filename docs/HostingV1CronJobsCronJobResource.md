# HostingV1CronJobsCronJobResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier of the cron job. Use it to delete the cron job or fetch its output. | [optional] 
**username** | **str** | Username of the account that owns the cron job. | [optional] 
**time** | **str** | Cron schedule expression. | [optional] 
**command** | **str** | Command executed on the schedule. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_cron_jobs_cron_job_resource import HostingV1CronJobsCronJobResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1CronJobsCronJobResource from a JSON string
hosting_v1_cron_jobs_cron_job_resource_instance = HostingV1CronJobsCronJobResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1CronJobsCronJobResource.to_json())

# convert the object into a dict
hosting_v1_cron_jobs_cron_job_resource_dict = hosting_v1_cron_jobs_cron_job_resource_instance.to_dict()
# create an instance of HostingV1CronJobsCronJobResource from a dict
hosting_v1_cron_jobs_cron_job_resource_from_dict = HostingV1CronJobsCronJobResource.from_dict(hosting_v1_cron_jobs_cron_job_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


