# HostingListNodeJSBuildsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HostingV1NodeJsBuildResource]**](HostingV1NodeJsBuildResource.md) | Array of [&#x60;Hosting.V1.NodeJs.BuildResource&#x60;](#model/hostingv1nodejsbuildresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.hosting_list_node_js_builds_v1200_response import HostingListNodeJSBuildsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HostingListNodeJSBuildsV1200Response from a JSON string
hosting_list_node_js_builds_v1200_response_instance = HostingListNodeJSBuildsV1200Response.from_json(json)
# print the JSON string representation of the object
print(HostingListNodeJSBuildsV1200Response.to_json())

# convert the object into a dict
hosting_list_node_js_builds_v1200_response_dict = hosting_list_node_js_builds_v1200_response_instance.to_dict()
# create an instance of HostingListNodeJSBuildsV1200Response from a dict
hosting_list_node_js_builds_v1200_response_from_dict = HostingListNodeJSBuildsV1200Response.from_dict(hosting_list_node_js_builds_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


