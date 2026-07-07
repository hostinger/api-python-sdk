# VPSV1PostInstallScriptListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VPSV1PostInstallScriptPostInstallScriptResource]**](VPSV1PostInstallScriptPostInstallScriptResource.md) | Array of [&#x60;VPS.V1.PostInstallScript.PostInstallScriptResource&#x60;](#model/vpsv1postinstallscriptpostinstallscriptresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_post_install_script_list_response import VPSV1PostInstallScriptListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1PostInstallScriptListResponse from a JSON string
vpsv1_post_install_script_list_response_instance = VPSV1PostInstallScriptListResponse.from_json(json)
# print the JSON string representation of the object
print(VPSV1PostInstallScriptListResponse.to_json())

# convert the object into a dict
vpsv1_post_install_script_list_response_dict = vpsv1_post_install_script_list_response_instance.to_dict()
# create an instance of VPSV1PostInstallScriptListResponse from a dict
vpsv1_post_install_script_list_response_from_dict = VPSV1PostInstallScriptListResponse.from_dict(vpsv1_post_install_script_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


