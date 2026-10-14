# HostingV1HeadlessStoreAgentReportRequestConsent

Upload status of the report, as written by the headless skill

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **bool** |  | 
**note** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_headless_store_agent_report_request_consent import HostingV1HeadlessStoreAgentReportRequestConsent

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1HeadlessStoreAgentReportRequestConsent from a JSON string
hosting_v1_headless_store_agent_report_request_consent_instance = HostingV1HeadlessStoreAgentReportRequestConsent.from_json(json)
# print the JSON string representation of the object
print(HostingV1HeadlessStoreAgentReportRequestConsent.to_json())

# convert the object into a dict
hosting_v1_headless_store_agent_report_request_consent_dict = hosting_v1_headless_store_agent_report_request_consent_instance.to_dict()
# create an instance of HostingV1HeadlessStoreAgentReportRequestConsent from a dict
hosting_v1_headless_store_agent_report_request_consent_from_dict = HostingV1HeadlessStoreAgentReportRequestConsent.from_dict(hosting_v1_headless_store_agent_report_request_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


