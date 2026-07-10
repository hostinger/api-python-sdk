# AgencyHostingV1WebsitesCustomSslCertResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_expired** | **bool** | Is the SSL certificate expired | [optional] 
**expires_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_custom_ssl_cert_resource import AgencyHostingV1WebsitesCustomSslCertResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesCustomSslCertResource from a JSON string
agency_hosting_v1_websites_custom_ssl_cert_resource_instance = AgencyHostingV1WebsitesCustomSslCertResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesCustomSslCertResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_custom_ssl_cert_resource_dict = agency_hosting_v1_websites_custom_ssl_cert_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesCustomSslCertResource from a dict
agency_hosting_v1_websites_custom_ssl_cert_resource_from_dict = AgencyHostingV1WebsitesCustomSslCertResource.from_dict(agency_hosting_v1_websites_custom_ssl_cert_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


