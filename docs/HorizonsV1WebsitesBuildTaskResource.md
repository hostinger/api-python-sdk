# HorizonsV1WebsitesBuildTaskResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The build task ID, used with the &#x60;Get website build task&#x60; tool | 
**state** | **str** | The build state. &#x60;TASK_STATE_SUBMITTED&#x60; and &#x60;TASK_STATE_WORKING&#x60; mean the build is still running. &#x60;TASK_STATE_COMPLETED&#x60; means it finished. &#x60;TASK_STATE_FAILED&#x60; means it broke, and &#x60;TASK_STATE_REJECTED&#x60; means it never started: the website does not contain the requested changes. &#x60;TASK_STATE_CANCELED&#x60; means the user stopped it; changes made before that may be kept. | 
**updated_at** | **datetime** | When the build last changed state | [optional] 
**reason_code** | **str** | Why the build stopped, or null. &#x60;insufficient_credits&#x60;: the user has no credits left; &#x60;execution_error&#x60; or &#x60;missing_result&#x60;: the build broke; &#x60;iteration_limit&#x60;: the build stopped early and kept the work done so far. | [optional] 
**message** | **str** | Guidance to tell the user about the build outcome, or null | [optional] 
**summary** | **str** | An internal changelog entry describing what the build changed, or null until the build ends. Rewrite it in plain language before showing it to the user. | [optional] 

## Example

```python
from hostinger_api.models.horizons_v1_websites_build_task_resource import HorizonsV1WebsitesBuildTaskResource

# TODO update the JSON string below
json = "{}"
# create an instance of HorizonsV1WebsitesBuildTaskResource from a JSON string
horizons_v1_websites_build_task_resource_instance = HorizonsV1WebsitesBuildTaskResource.from_json(json)
# print the JSON string representation of the object
print(HorizonsV1WebsitesBuildTaskResource.to_json())

# convert the object into a dict
horizons_v1_websites_build_task_resource_dict = horizons_v1_websites_build_task_resource_instance.to_dict()
# create an instance of HorizonsV1WebsitesBuildTaskResource from a dict
horizons_v1_websites_build_task_resource_from_dict = HorizonsV1WebsitesBuildTaskResource.from_dict(horizons_v1_websites_build_task_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


