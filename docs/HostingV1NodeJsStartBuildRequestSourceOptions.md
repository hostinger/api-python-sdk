# HostingV1NodeJsStartBuildRequestSourceOptions

Source-specific options. For `archive` send `archive_path` and a `message` describing the change. For `git` send `owner`, `repository`, `branch` and `installation_uuid`, taken from `List Git installations` and `List Git installation repositories`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_path** | **str** | The path to the archive file relative to the document root of the vhost (required if source is \&quot;archive\&quot;) | [optional] 
**message** | **str** | Short summary of what this deployment changes, shown in the website&#39;s deployment history the way a commit message is for git deployments. Without it the history only shows the archive file name, so always send one: keep the first line under 72 characters and describe the change, not the upload. Only used if source is \&quot;archive\&quot;. | [optional] 
**owner** | **str** | Repository owner login (required if source is \&quot;git\&quot;). GitLab group paths use slashes. | [optional] 
**repository** | **str** | Repository name without the .git suffix (required if source is \&quot;git\&quot;) | [optional] 
**branch** | **str** | Branch to build (required if source is \&quot;git\&quot;) | [optional] 
**installation_uuid** | **str** | Git installation used to access the repository (required if source is \&quot;git\&quot;) | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_start_build_request_source_options import HostingV1NodeJsStartBuildRequestSourceOptions

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsStartBuildRequestSourceOptions from a JSON string
hosting_v1_node_js_start_build_request_source_options_instance = HostingV1NodeJsStartBuildRequestSourceOptions.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsStartBuildRequestSourceOptions.to_json())

# convert the object into a dict
hosting_v1_node_js_start_build_request_source_options_dict = hosting_v1_node_js_start_build_request_source_options_instance.to_dict()
# create an instance of HostingV1NodeJsStartBuildRequestSourceOptions from a dict
hosting_v1_node_js_start_build_request_source_options_from_dict = HostingV1NodeJsStartBuildRequestSourceOptions.from_dict(hosting_v1_node_js_start_build_request_source_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


