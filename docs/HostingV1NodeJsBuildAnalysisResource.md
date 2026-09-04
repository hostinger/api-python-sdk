# HostingV1NodeJsBuildAnalysisResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | **str** | Why the build failed. null when no analysis could be produced. | 
**solution** | **str** | Suggested fix for the build failure. null when no analysis could be produced. | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_build_analysis_resource import HostingV1NodeJsBuildAnalysisResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsBuildAnalysisResource from a JSON string
hosting_v1_node_js_build_analysis_resource_instance = HostingV1NodeJsBuildAnalysisResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsBuildAnalysisResource.to_json())

# convert the object into a dict
hosting_v1_node_js_build_analysis_resource_dict = hosting_v1_node_js_build_analysis_resource_instance.to_dict()
# create an instance of HostingV1NodeJsBuildAnalysisResource from a dict
hosting_v1_node_js_build_analysis_resource_from_dict = HostingV1NodeJsBuildAnalysisResource.from_dict(hosting_v1_node_js_build_analysis_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


