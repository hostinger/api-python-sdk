# VPSV1PostInstallScriptStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the script | 
**content** | **str** | Content of the script | 

## Example

```python
from hostinger_api.models.vpsv1_post_install_script_store_request import VPSV1PostInstallScriptStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1PostInstallScriptStoreRequest from a JSON string
vpsv1_post_install_script_store_request_instance = VPSV1PostInstallScriptStoreRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1PostInstallScriptStoreRequest.to_json())

# convert the object into a dict
vpsv1_post_install_script_store_request_dict = vpsv1_post_install_script_store_request_instance.to_dict()
# create an instance of VPSV1PostInstallScriptStoreRequest from a dict
vpsv1_post_install_script_store_request_from_dict = VPSV1PostInstallScriptStoreRequest.from_dict(vpsv1_post_install_script_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


