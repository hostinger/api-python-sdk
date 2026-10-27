# HostingV1WebsitesTriggerEventRequestEventParams

Fields of the event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool** | **str** | Lowercase slug of the AI coding tool. Known slugs: &#x60;claude&#x60; (Claude Code), &#x60;cursor&#x60; (Cursor), &#x60;codex&#x60; (Codex), &#x60;vscode&#x60; (VS Code), &#x60;antigravity&#x60; (Antigravity) and &#x60;devin&#x60; (Devin). For any other tool, send its own slug. | 

## Example

```python
from hostinger_api.models.hosting_v1_websites_trigger_event_request_event_params import HostingV1WebsitesTriggerEventRequestEventParams

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WebsitesTriggerEventRequestEventParams from a JSON string
hosting_v1_websites_trigger_event_request_event_params_instance = HostingV1WebsitesTriggerEventRequestEventParams.from_json(json)
# print the JSON string representation of the object
print(HostingV1WebsitesTriggerEventRequestEventParams.to_json())

# convert the object into a dict
hosting_v1_websites_trigger_event_request_event_params_dict = hosting_v1_websites_trigger_event_request_event_params_instance.to_dict()
# create an instance of HostingV1WebsitesTriggerEventRequestEventParams from a dict
hosting_v1_websites_trigger_event_request_event_params_from_dict = HostingV1WebsitesTriggerEventRequestEventParams.from_dict(hosting_v1_websites_trigger_event_request_event_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


