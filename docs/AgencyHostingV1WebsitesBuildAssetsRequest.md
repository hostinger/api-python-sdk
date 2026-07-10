# AgencyHostingV1WebsitesBuildAssetsRequest

Build Node.js assets from an already-uploaded archive

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_path** | **str** | Directory, relative to the website document root, where the uploaded site archive currently lives. Most commonly this is simply &#x60;public_html&#x60;. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_build_assets_request import AgencyHostingV1WebsitesBuildAssetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesBuildAssetsRequest from a JSON string
agency_hosting_v1_websites_build_assets_request_instance = AgencyHostingV1WebsitesBuildAssetsRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesBuildAssetsRequest.to_json())

# convert the object into a dict
agency_hosting_v1_websites_build_assets_request_dict = agency_hosting_v1_websites_build_assets_request_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesBuildAssetsRequest from a dict
agency_hosting_v1_websites_build_assets_request_from_dict = AgencyHostingV1WebsitesBuildAssetsRequest.from_dict(agency_hosting_v1_websites_build_assets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


