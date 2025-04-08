# VPSV1PostInstallScriptPostInstallScriptResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Post-install script ID | [optional] 
**name** | **str** | Name of the script | [optional] 
**content** | **str** | Content of the script | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_post_install_script_post_install_script_resource import VPSV1PostInstallScriptPostInstallScriptResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1PostInstallScriptPostInstallScriptResource from a JSON string
vpsv1_post_install_script_post_install_script_resource_instance = VPSV1PostInstallScriptPostInstallScriptResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1PostInstallScriptPostInstallScriptResource.to_json())

# convert the object into a dict
vpsv1_post_install_script_post_install_script_resource_dict = vpsv1_post_install_script_post_install_script_resource_instance.to_dict()
# create an instance of VPSV1PostInstallScriptPostInstallScriptResource from a dict
vpsv1_post_install_script_post_install_script_resource_from_dict = VPSV1PostInstallScriptPostInstallScriptResource.from_dict(vpsv1_post_install_script_post_install_script_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


