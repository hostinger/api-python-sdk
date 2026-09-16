# HostingV1NodeJsSourceOptionsResource

Which keys carry values depends on the parent source_type; the others are null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_path** | **str** | Present if sourceType is \&quot;archive\&quot; | [optional] 
**owner** | **str** | Repository owner login (present if source_type is \&quot;git\&quot;) | 
**repository** | **str** | Repository name without the .git suffix (present if source_type is \&quot;git\&quot;) | 
**branch** | **str** | Branch that was built (present if source_type is \&quot;git\&quot;) | 
**installation_uuid** | **str** | Git installation used to access the repository (present if source_type is \&quot;git\&quot;) | 
**commit** | [**HostingV1GitGitCommitResource**](HostingV1GitGitCommitResource.md) |  | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_source_options_resource import HostingV1NodeJsSourceOptionsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsSourceOptionsResource from a JSON string
hosting_v1_node_js_source_options_resource_instance = HostingV1NodeJsSourceOptionsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsSourceOptionsResource.to_json())

# convert the object into a dict
hosting_v1_node_js_source_options_resource_dict = hosting_v1_node_js_source_options_resource_instance.to_dict()
# create an instance of HostingV1NodeJsSourceOptionsResource from a dict
hosting_v1_node_js_source_options_resource_from_dict = HostingV1NodeJsSourceOptionsResource.from_dict(hosting_v1_node_js_source_options_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


