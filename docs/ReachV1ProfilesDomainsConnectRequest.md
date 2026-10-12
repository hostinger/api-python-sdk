# ReachV1ProfilesDomainsConnectRequest

Sending domain to connect to the profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 

## Example

```python
from hostinger_api.models.reach_v1_profiles_domains_connect_request import ReachV1ProfilesDomainsConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesDomainsConnectRequest from a JSON string
reach_v1_profiles_domains_connect_request_instance = ReachV1ProfilesDomainsConnectRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesDomainsConnectRequest.to_json())

# convert the object into a dict
reach_v1_profiles_domains_connect_request_dict = reach_v1_profiles_domains_connect_request_instance.to_dict()
# create an instance of ReachV1ProfilesDomainsConnectRequest from a dict
reach_v1_profiles_domains_connect_request_from_dict = ReachV1ProfilesDomainsConnectRequest.from_dict(reach_v1_profiles_domains_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


