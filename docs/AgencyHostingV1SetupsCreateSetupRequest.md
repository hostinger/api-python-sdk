# AgencyHostingV1SetupsCreateSetupRequest

Create a new Agency Plan website setup on the given order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter_code** | **str** | Datacenter code where the website should be provisioned. Available codes depend on live capacity and are not a fixed set. | 
**flavor** | **str** | Setup flavor: a specific WordPress version in the format &#x60;wp-&lt;major&gt;.&lt;minor&gt;&#x60; or &#x60;wp-&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;&#x60; (e.g. &#x60;wp-6.8.2&#x60;), or &#x60;php-fpm&#x60; for a plain PHP stack. Generic versions like &#x60;wp-latest&#x60; are not allowed. | 
**settings** | [**AgencyHostingV1SetupsCreateSetupRequestSettings**](AgencyHostingV1SetupsCreateSetupRequestSettings.md) |  | 
**domain** | **str** | Primary domain to attach to the website. Omit or set to null to get a free auto-generated *.hostingersite.com subdomain instead. | [optional] 
**type** | **str** | Website type | [optional] 
**wordpress** | [**AgencyHostingV1SetupsCreateSetupRequestWordpress**](AgencyHostingV1SetupsCreateSetupRequestWordpress.md) |  | [optional] 
**clone** | [**AgencyHostingV1SetupsCreateSetupRequestClone**](AgencyHostingV1SetupsCreateSetupRequestClone.md) |  | [optional] 
**derive_domain** | [**AgencyHostingV1SetupsCreateSetupRequestDeriveDomain**](AgencyHostingV1SetupsCreateSetupRequestDeriveDomain.md) |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_setups_create_setup_request import AgencyHostingV1SetupsCreateSetupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1SetupsCreateSetupRequest from a JSON string
agency_hosting_v1_setups_create_setup_request_instance = AgencyHostingV1SetupsCreateSetupRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1SetupsCreateSetupRequest.to_json())

# convert the object into a dict
agency_hosting_v1_setups_create_setup_request_dict = agency_hosting_v1_setups_create_setup_request_instance.to_dict()
# create an instance of AgencyHostingV1SetupsCreateSetupRequest from a dict
agency_hosting_v1_setups_create_setup_request_from_dict = AgencyHostingV1SetupsCreateSetupRequest.from_dict(agency_hosting_v1_setups_create_setup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


