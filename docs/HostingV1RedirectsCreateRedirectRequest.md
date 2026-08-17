# HostingV1RedirectsCreateRedirectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Source URL on the selected website | 
**to** | **str** | Destination URL or IP address | 

## Example

```python
from hostinger_api.models.hosting_v1_redirects_create_redirect_request import HostingV1RedirectsCreateRedirectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1RedirectsCreateRedirectRequest from a JSON string
hosting_v1_redirects_create_redirect_request_instance = HostingV1RedirectsCreateRedirectRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1RedirectsCreateRedirectRequest.to_json())

# convert the object into a dict
hosting_v1_redirects_create_redirect_request_dict = hosting_v1_redirects_create_redirect_request_instance.to_dict()
# create an instance of HostingV1RedirectsCreateRedirectRequest from a dict
hosting_v1_redirects_create_redirect_request_from_dict = HostingV1RedirectsCreateRedirectRequest.from_dict(hosting_v1_redirects_create_redirect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


