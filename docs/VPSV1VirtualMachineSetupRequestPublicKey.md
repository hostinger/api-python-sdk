# VPSV1VirtualMachineSetupRequestPublicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the SSH key | [optional] 
**key** | **str** | SSH public key | [optional] 

## Example

```python
from @hostinger/api.models.vpsv1_virtual_machine_setup_request_public_key import VPSV1VirtualMachineSetupRequestPublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineSetupRequestPublicKey from a JSON string
vpsv1_virtual_machine_setup_request_public_key_instance = VPSV1VirtualMachineSetupRequestPublicKey.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineSetupRequestPublicKey.to_json())

# convert the object into a dict
vpsv1_virtual_machine_setup_request_public_key_dict = vpsv1_virtual_machine_setup_request_public_key_instance.to_dict()
# create an instance of VPSV1VirtualMachineSetupRequestPublicKey from a dict
vpsv1_virtual_machine_setup_request_public_key_from_dict = VPSV1VirtualMachineSetupRequestPublicKey.from_dict(vpsv1_virtual_machine_setup_request_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


