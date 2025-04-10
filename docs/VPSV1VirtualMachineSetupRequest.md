# VPSV1VirtualMachineSetupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Template ID | 
**data_center_id** | **int** | Data center ID | 
**post_install_script_id** | **int** | Post-install script ID | [optional] 
**password** | **str** | Password for the virtual machine. If not provided, random password will be generated. Password will not be shown in the response. | [optional] 
**hostname** | **str** | Override default hostname of the virtual machine | [optional] 
**install_monarx** | **bool** | Install Monarx malware scanner (if supported) | [optional] [default to False]
**enable_backups** | **bool** | Enable weekly backup schedule | [optional] [default to True]
**ns1** | **str** |  | [optional] 
**ns2** | **str** |  | [optional] 
**public_key** | [**VPSV1VirtualMachineSetupRequestPublicKey**](VPSV1VirtualMachineSetupRequestPublicKey.md) |  | [optional] 

## Example

```python
from @hostinger/api.models.vpsv1_virtual_machine_setup_request import VPSV1VirtualMachineSetupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineSetupRequest from a JSON string
vpsv1_virtual_machine_setup_request_instance = VPSV1VirtualMachineSetupRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineSetupRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_setup_request_dict = vpsv1_virtual_machine_setup_request_instance.to_dict()
# create an instance of VPSV1VirtualMachineSetupRequest from a dict
vpsv1_virtual_machine_setup_request_from_dict = VPSV1VirtualMachineSetupRequest.from_dict(vpsv1_virtual_machine_setup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


