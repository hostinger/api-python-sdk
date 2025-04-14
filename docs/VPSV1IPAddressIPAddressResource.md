# VPSV1IPAddressIPAddressResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | IP address ID | [optional] 
**address** | **str** | IP address: IPv4 or IPv6 | [optional] 
**ptr** | **str** | IP address PTR record | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_ip_address_ip_address_resource import VPSV1IPAddressIPAddressResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1IPAddressIPAddressResource from a JSON string
vpsv1_ip_address_ip_address_resource_instance = VPSV1IPAddressIPAddressResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1IPAddressIPAddressResource.to_json())

# convert the object into a dict
vpsv1_ip_address_ip_address_resource_dict = vpsv1_ip_address_ip_address_resource_instance.to_dict()
# create an instance of VPSV1IPAddressIPAddressResource from a dict
vpsv1_ip_address_ip_address_resource_from_dict = VPSV1IPAddressIPAddressResource.from_dict(vpsv1_ip_address_ip_address_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


