# AgencyHostingV1SetupsCreateSetupRequestDeriveDomain

Derive the domain from an existing vhost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_vhost** | [**AgencyHostingV1SetupsCreateSetupRequestDeriveDomainFromVhost**](AgencyHostingV1SetupsCreateSetupRequestDeriveDomainFromVhost.md) |  | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_setups_create_setup_request_derive_domain import AgencyHostingV1SetupsCreateSetupRequestDeriveDomain

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1SetupsCreateSetupRequestDeriveDomain from a JSON string
agency_hosting_v1_setups_create_setup_request_derive_domain_instance = AgencyHostingV1SetupsCreateSetupRequestDeriveDomain.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1SetupsCreateSetupRequestDeriveDomain.to_json())

# convert the object into a dict
agency_hosting_v1_setups_create_setup_request_derive_domain_dict = agency_hosting_v1_setups_create_setup_request_derive_domain_instance.to_dict()
# create an instance of AgencyHostingV1SetupsCreateSetupRequestDeriveDomain from a dict
agency_hosting_v1_setups_create_setup_request_derive_domain_from_dict = AgencyHostingV1SetupsCreateSetupRequestDeriveDomain.from_dict(agency_hosting_v1_setups_create_setup_request_derive_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


