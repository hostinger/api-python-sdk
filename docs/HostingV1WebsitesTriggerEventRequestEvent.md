# HostingV1WebsitesTriggerEventRequestEvent

Event to trigger; `name` decides which `params` it takes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event: - &#x60;headless_onboarding.tool.connected&#x60;: an AI coding tool started building this website   with the Hostinger headless skill. Takes &#x60;params.tool&#x60;. | 
**params** | [**HostingV1WebsitesTriggerEventRequestEventParams**](HostingV1WebsitesTriggerEventRequestEventParams.md) |  | 

## Example

```python
from hostinger_api.models.hosting_v1_websites_trigger_event_request_event import HostingV1WebsitesTriggerEventRequestEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WebsitesTriggerEventRequestEvent from a JSON string
hosting_v1_websites_trigger_event_request_event_instance = HostingV1WebsitesTriggerEventRequestEvent.from_json(json)
# print the JSON string representation of the object
print(HostingV1WebsitesTriggerEventRequestEvent.to_json())

# convert the object into a dict
hosting_v1_websites_trigger_event_request_event_dict = hosting_v1_websites_trigger_event_request_event_instance.to_dict()
# create an instance of HostingV1WebsitesTriggerEventRequestEvent from a dict
hosting_v1_websites_trigger_event_request_event_from_dict = HostingV1WebsitesTriggerEventRequestEvent.from_dict(hosting_v1_websites_trigger_event_request_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


