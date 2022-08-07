# Getting started

## Prerequisites
- Install the [Azure Function Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools)
- Python 3.9.0
- Azure Subscription (optional)

## Start the function 
```
func start --python
```

> In order to start the Azure Function via the Azure Function Core Tools (CLI) a activated virtual environment is required.

After starting Azure Functions you can access the documentation via this link:
```
http://localhost:7071/docs
```

## Deploy to Azure:
> This step requires an Azure Account. In case you do not have an Azure Account you can go ahead and create an account for free [here](https://azure.microsoft.com/en-us/free/).

Deploy ARM template to a existing resource group:
```
az deployment group create --resource-group <resource-group> --template-file .\az-func-template.json --parameters appName='<your_app_name>' storageAcctName='<your_storage_account_name>' hostingPlanName='<your_hosting_plan_name>'

func azure functionapp publish <your_function_app_name>
```
## Deploy to Azure using VScode:
https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python


## Redeploy to Azure:
https://docs.microsoft.com/en-us/azure/developer/javascript/how-to/with-web-app/azure-function-resource-group-management/add-delete-functions-redeploy


## Configuration
https://iotespresso.com/azure-function-to-fastapi-app-service/