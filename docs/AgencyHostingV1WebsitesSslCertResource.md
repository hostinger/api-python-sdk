# AgencyHostingV1WebsitesSslCertResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | SSL cert names | [optional] 
**expires_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_ssl_cert_resource import AgencyHostingV1WebsitesSslCertResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesSslCertResource from a JSON string
agency_hosting_v1_websites_ssl_cert_resource_instance = AgencyHostingV1WebsitesSslCertResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesSslCertResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_ssl_cert_resource_dict = agency_hosting_v1_websites_ssl_cert_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesSslCertResource from a dict
agency_hosting_v1_websites_ssl_cert_resource_from_dict = AgencyHostingV1WebsitesSslCertResource.from_dict(agency_hosting_v1_websites_ssl_cert_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


