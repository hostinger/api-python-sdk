# HostingV1WebsitesTriggerEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HostingV1WebsitesTriggerEventRequestEvent**](HostingV1WebsitesTriggerEventRequestEvent.md) |  | 

## Example

```python
from hostinger_api.models.hosting_v1_websites_trigger_event_request import HostingV1WebsitesTriggerEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WebsitesTriggerEventRequest from a JSON string
hosting_v1_websites_trigger_event_request_instance = HostingV1WebsitesTriggerEventRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1WebsitesTriggerEventRequest.to_json())

# convert the object into a dict
hosting_v1_websites_trigger_event_request_dict = hosting_v1_websites_trigger_event_request_instance.to_dict()
# create an instance of HostingV1WebsitesTriggerEventRequest from a dict
hosting_v1_websites_trigger_event_request_from_dict = HostingV1WebsitesTriggerEventRequest.from_dict(hosting_v1_websites_trigger_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


