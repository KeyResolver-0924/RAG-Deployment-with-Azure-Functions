"""
The module contains the Azure Function App HTTP trigger that processes a request
to generate a response based on the query provided in the JSON body.

"""

import logging
import os

import azure.functions as func

from rag_app import rag_retrieve_and_generate

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="HttpTrigger")
@app.route(route="req")
def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP trigger function that processes a request to generate a response based on the query provided in the JSON body.

    Args:
    ----
        req (func.HttpRequest): The HTTP request object.

    Returns:
    -------
        func.HttpResponse: The HTTP response containing the result or an error message.

    """
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid request body. Please provide a valid JSON with the 'query' key.",
            status_code=400
        )

    query = req_body.get('query')
    if not query:
        return func.HttpResponse(
            "Please provide a 'query' in the request body.",
            status_code=400
        )

    collection_name = os.getenv('COLLECTION_NAME')  # Ensure this environment variable is set in your Azure Function App settings
    if not collection_name:
        return func.HttpResponse(
            "Collection name not found in environment variables.",
            status_code=500
        )

    try:
        response = rag_retrieve_and_generate(query, collection_name)
        return func.HttpResponse(response, status_code=200)
    except Exception as e:
        logging.error(f"Error processing query: {e}")
        return func.HttpResponse(
            f"An error occurred: {str(e)}",
            status_code=500
        )

