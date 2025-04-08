# VPSGetFirewallListV1200ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from hostinger-api.models.vps_get_firewall_list_v1200_response_meta import VPSGetFirewallListV1200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of VPSGetFirewallListV1200ResponseMeta from a JSON string
vps_get_firewall_list_v1200_response_meta_instance = VPSGetFirewallListV1200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(VPSGetFirewallListV1200ResponseMeta.to_json())

# convert the object into a dict
vps_get_firewall_list_v1200_response_meta_dict = vps_get_firewall_list_v1200_response_meta_instance.to_dict()
# create an instance of VPSGetFirewallListV1200ResponseMeta from a dict
vps_get_firewall_list_v1200_response_meta_from_dict = VPSGetFirewallListV1200ResponseMeta.from_dict(vps_get_firewall_list_v1200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


