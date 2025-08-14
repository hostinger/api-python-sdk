# hostinger_api.VPSDockerManagerApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_project_v1**](VPSDockerManagerApi.md#create_new_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker | Create new project
[**delete_project_v1**](VPSDockerManagerApi.md#delete_project_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/down | Delete project
[**get_project_containers_v1**](VPSDockerManagerApi.md#get_project_containers_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/containers | Get project containers
[**get_project_contents_v1**](VPSDockerManagerApi.md#get_project_contents_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName} | Get project contents
[**get_project_list_v1**](VPSDockerManagerApi.md#get_project_list_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/docker | Get project list
[**get_project_logs_v1**](VPSDockerManagerApi.md#get_project_logs_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/logs | Get project logs
[**restart_project_v1**](VPSDockerManagerApi.md#restart_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/restart | Restart project
[**start_project_v1**](VPSDockerManagerApi.md#start_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/start | Start project
[**stop_project_v1**](VPSDockerManagerApi.md#stop_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/stop | Stop project
[**update_project_v1**](VPSDockerManagerApi.md#update_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/update | Update project


# **create_new_project_v1**
> VPSV1ActionActionResource create_new_project_v1(virtual_machine_id, vpsv1_virtual_machine_docker_manager_up_request)

Create new project

Deploy new project from docker-compose.yaml contents or download contents from URL. 

URL can be Github repository url in format https://github.com/[user]/[repo] and it will be automatically resolved to 
docker-compose.yaml file in master branch. Any other URL provided must return docker-compose.yaml file contents.

If project already exists, it will be replaced.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_virtual_machine_docker_manager_up_request import VPSV1VirtualMachineDockerManagerUpRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_virtual_machine_docker_manager_up_request = hostinger_api.VPSV1VirtualMachineDockerManagerUpRequest() # VPSV1VirtualMachineDockerManagerUpRequest | 

    try:
        # Create new project
        api_response = api_instance.create_new_project_v1(virtual_machine_id, vpsv1_virtual_machine_docker_manager_up_request)
        print("The response of VPSDockerManagerApi->create_new_project_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->create_new_project_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_virtual_machine_docker_manager_up_request** | [**VPSV1VirtualMachineDockerManagerUpRequest**](VPSV1VirtualMachineDockerManagerUpRequest.md)|  | 

### Return type

[**VPSV1ActionActionResource**](VPSV1ActionActionResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_v1**
> VPSV1ActionActionResource delete_project_v1(virtual_machine_id, project_name)

Delete project

Completely removes a Docker Compose project from the virtual machine, stopping all containers and cleaning up 
associated resources including networks, volumes, and images. 

This operation is irreversible and will delete all project data. 

Use this when you want to permanently remove a project and free up system resources.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    project_name = 'my-docker-project' # str | Docker Compose project name using alphanumeric characters, dashes, and underscores only

    try:
        # Delete project
        api_response = api_instance.delete_project_v1(virtual_machine_id, project_name)
        print("The response of VPSDockerManagerApi->delete_project_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->delete_project_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **project_name** | **str**| Docker Compose project name using alphanumeric characters, dashes, and underscores only | 

### Return type

[**VPSV1ActionActionResource**](VPSV1ActionActionResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_containers_v1**
> List[VPSV1DockerManagerContainerResource] get_project_containers_v1(virtual_machine_id, project_name)

Get project containers

Retrieves a list of all containers belonging to a specific Docker Compose project on the virtual machine. 

This endpoint returns detailed information about each container including their current status, port mappings, and runtime configuration. 

Use this to monitor the health and state of all services within your Docker Compose project.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_docker_manager_container_resource import VPSV1DockerManagerContainerResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    project_name = 'my-docker-project' # str | Docker Compose project name using alphanumeric characters, dashes, and underscores only

    try:
        # Get project containers
        api_response = api_instance.get_project_containers_v1(virtual_machine_id, project_name)
        print("The response of VPSDockerManagerApi->get_project_containers_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->get_project_containers_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **project_name** | **str**| Docker Compose project name using alphanumeric characters, dashes, and underscores only | 

### Return type

[**List[VPSV1DockerManagerContainerResource]**](VPSV1DockerManagerContainerResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_contents_v1**
> VPSV1DockerManagerContentResource get_project_contents_v1(virtual_machine_id, project_name)

Get project contents

Retrieves the complete project information including the docker-compose.yml file contents, project metadata, and current deployment status. 

This endpoint provides the full configuration and state details of a specific Docker Compose project. 

Use this to inspect project settings, review the compose file, or check the overall project health.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_docker_manager_content_resource import VPSV1DockerManagerContentResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    project_name = 'my-docker-project' # str | Docker Compose project name using alphanumeric characters, dashes, and underscores only

    try:
        # Get project contents
        api_response = api_instance.get_project_contents_v1(virtual_machine_id, project_name)
        print("The response of VPSDockerManagerApi->get_project_contents_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->get_project_contents_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **project_name** | **str**| Docker Compose project name using alphanumeric characters, dashes, and underscores only | 

### Return type

[**VPSV1DockerManagerContentResource**](VPSV1DockerManagerContentResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list_v1**
> List[VPSV1DockerManagerProjectResource] get_project_list_v1(virtual_machine_id)

Get project list

Retrieves a list of all Docker Compose projects currently deployed on the virtual machine. 

This endpoint returns basic information about each project including name, status, and file path. 

Use this to get an overview of all Docker projects on your VPS instance.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_docker_manager_project_resource import VPSV1DockerManagerProjectResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Get project list
        api_response = api_instance.get_project_list_v1(virtual_machine_id)
        print("The response of VPSDockerManagerApi->get_project_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->get_project_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 

### Return type

[**List[VPSV1DockerManagerProjectResource]**](VPSV1DockerManagerProjectResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_logs_v1**
> List[VPSV1DockerManagerLogsResource] get_project_logs_v1(virtual_machine_id, project_name)

Get project logs

Retrieves aggregated log entries from all services within a Docker Compose project. 

This endpoint returns recent log output from each container, organized by service name with timestamps. 
The response contains the last 300 log entries across all services. 

Use this for debugging, monitoring application behavior, and troubleshooting issues across your entire project stack.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_docker_manager_logs_resource import VPSV1DockerManagerLogsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    project_name = 'my-docker-project' # str | Docker Compose project name using alphanumeric characters, dashes, and underscores only

    try:
        # Get project logs
        api_response = api_instance.get_project_logs_v1(virtual_machine_id, project_name)
        print("The response of VPSDockerManagerApi->get_project_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->get_project_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **project_name** | **str**| Docker Compose project name using alphanumeric characters, dashes, and underscores only | 

### Return type

[**List[VPSV1DockerManagerLogsResource]**](VPSV1DockerManagerLogsResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_project_v1**
> VPSV1ActionActionResource restart_project_v1(virtual_machine_id, project_name)

Restart project

Restarts all services in a Docker Compose project by stopping and starting containers in the correct dependency order. 

This operation preserves data volumes and network configurations while refreshing the running containers. 

Use this to apply configuration changes or recover from service failures.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    project_name = 'my-docker-project' # str | Docker Compose project name using alphanumeric characters, dashes, and underscores only

    try:
        # Restart project
        api_response = api_instance.restart_project_v1(virtual_machine_id, project_name)
        print("The response of VPSDockerManagerApi->restart_project_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->restart_project_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **project_name** | **str**| Docker Compose project name using alphanumeric characters, dashes, and underscores only | 

### Return type

[**VPSV1ActionActionResource**](VPSV1ActionActionResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_project_v1**
> VPSV1ActionActionResource start_project_v1(virtual_machine_id, project_name)

Start project

Starts all services in a Docker Compose project that are currently stopped. 

This operation brings up containers in the correct dependency order as defined in the compose file. 

Use this to resume a project that was previously stopped or to start services after a system reboot.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    project_name = 'my-docker-project' # str | Docker Compose project name using alphanumeric characters, dashes, and underscores only

    try:
        # Start project
        api_response = api_instance.start_project_v1(virtual_machine_id, project_name)
        print("The response of VPSDockerManagerApi->start_project_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->start_project_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **project_name** | **str**| Docker Compose project name using alphanumeric characters, dashes, and underscores only | 

### Return type

[**VPSV1ActionActionResource**](VPSV1ActionActionResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_project_v1**
> VPSV1ActionActionResource stop_project_v1(virtual_machine_id, project_name)

Stop project

Stops all running services in a Docker Compose project while preserving container configurations and data volumes. 

This operation gracefully shuts down containers in reverse dependency order. 

Use this to temporarily halt a project without removing data or configurations.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    project_name = 'my-docker-project' # str | Docker Compose project name using alphanumeric characters, dashes, and underscores only

    try:
        # Stop project
        api_response = api_instance.stop_project_v1(virtual_machine_id, project_name)
        print("The response of VPSDockerManagerApi->stop_project_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->stop_project_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **project_name** | **str**| Docker Compose project name using alphanumeric characters, dashes, and underscores only | 

### Return type

[**VPSV1ActionActionResource**](VPSV1ActionActionResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_v1**
> VPSV1ActionActionResource update_project_v1(virtual_machine_id, project_name)

Update project

Updates a Docker Compose project by pulling the latest image versions and recreating containers with new configurations. 

This operation preserves data volumes while applying changes from the compose file. 

Use this to deploy application updates, apply configuration changes, or refresh container images to their latest versions.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDockerManagerApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    project_name = 'my-docker-project' # str | Docker Compose project name using alphanumeric characters, dashes, and underscores only

    try:
        # Update project
        api_response = api_instance.update_project_v1(virtual_machine_id, project_name)
        print("The response of VPSDockerManagerApi->update_project_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDockerManagerApi->update_project_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **project_name** | **str**| Docker Compose project name using alphanumeric characters, dashes, and underscores only | 

### Return type

[**VPSV1ActionActionResource**](VPSV1ActionActionResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

