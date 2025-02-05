#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Load environment variables from .env file
set -o allexport
source .env
set -o allexport

# Create resource group
echo "Creating resource group..."
az group create --name ${RESOURCE_GROUP} --location ${LOCATION}

# Create storage account
echo "Creating storage account..."
az storage account create \
  --name ${STORAGE_ACCOUNT_NAME} \
  --location ${LOCATION} \
  --resource-group ${RESOURCE_GROUP} \
  --sku Standard_LRS

# Create function app
echo "Creating function app..."
az functionapp create \
  --resource-group ${RESOURCE_GROUP} \
  --consumption-plan-location ${LOCATION} \
  --name ${APP_NAME} \
  --runtime python \
  --runtime-version 3.10 \
  --functions-version 4 \
  --storage-account ${STORAGE_ACCOUNT_NAME} \
  --os-type Linux

# Wait for the function app to be fully created
echo "Waiting for the function app to be fully created..."
sleep 30

# Publish the function app with a retry mechanism
echo "Publishing the function app..."
for i in {1..3}; do
    if func azure functionapp publish ${APP_NAME} --build remote --verbose; then
        echo "Function app published successfully"
        break
    else
        echo "Failed to publish function app. Retrying in 10 seconds..."
        sleep 10
    fi
done

# Retrieve the Function App URL
FUNCTION_APP_URL=$(az functionapp show --name ${APP_NAME} --resource-group ${RESOURCE_GROUP} --query "defaultHostName" --output tsv)
echo "Function App URL: https://${FUNCTION_APP_URL}"
