# HostingV1NodeJsPatchResultResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pr_url** | **str** | URL to the created GitHub pull request | [optional] 
**pr_number** | **int** | GitHub pull request number | [optional] 
**head_branch** | **str** | The branch created with the fix | [optional] 
**patched_vulnerability_ids** | **List[str]** | List of vulnerability IDs that were patched in the pull request | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_patch_result_resource import HostingV1NodeJsPatchResultResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsPatchResultResource from a JSON string
hosting_v1_node_js_patch_result_resource_instance = HostingV1NodeJsPatchResultResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsPatchResultResource.to_json())

# convert the object into a dict
hosting_v1_node_js_patch_result_resource_dict = hosting_v1_node_js_patch_result_resource_instance.to_dict()
# create an instance of HostingV1NodeJsPatchResultResource from a dict
hosting_v1_node_js_patch_result_resource_from_dict = HostingV1NodeJsPatchResultResource.from_dict(hosting_v1_node_js_patch_result_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


