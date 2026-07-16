# HostingV1NodeJsPatchVulnerabilitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vulnerability_ids** | **List[str]** | List of vulnerability IDs to patch, as returned by the list vulnerabilities endpoint. | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_patch_vulnerabilities_request import HostingV1NodeJsPatchVulnerabilitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsPatchVulnerabilitiesRequest from a JSON string
hosting_v1_node_js_patch_vulnerabilities_request_instance = HostingV1NodeJsPatchVulnerabilitiesRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsPatchVulnerabilitiesRequest.to_json())

# convert the object into a dict
hosting_v1_node_js_patch_vulnerabilities_request_dict = hosting_v1_node_js_patch_vulnerabilities_request_instance.to_dict()
# create an instance of HostingV1NodeJsPatchVulnerabilitiesRequest from a dict
hosting_v1_node_js_patch_vulnerabilities_request_from_dict = HostingV1NodeJsPatchVulnerabilitiesRequest.from_dict(hosting_v1_node_js_patch_vulnerabilities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


