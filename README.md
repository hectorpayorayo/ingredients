INGREDIENTS
==========================

### General Information

1. Search ingredients
   - Description: Get list of ingredient suggestions
   - endpoint_url:
      - ```https://2vppg4p6b0.execute-api.us-east-1.amazonaws.com/search?owner_id=<OWNER_ID>&name=<NAME>```
   - HTTP Verb:
       - **GET**
       
   Curl request example:
    ```commandline

   curl --location --request GET 'https://2vppg4p6b0.execute-api.us-east-1.amazonaws.com/search?owner_id=8183&name=S'
   
    ```
   **response example:**
    ```json
    {
    "ingredients": [
        {
            "id": 14282,
            "name": "Red Kuri Squash",
            "owner_id": null
        },
        {
            "id": 14286,
            "name": "Salsify",
            "owner_id": null
        },
        {
            "id": 223922,
            "name": "Seasoned Rice Vinegar",
            "owner_id": 8183
        },
        {
            "id": 223928,
            "name": "Shelled Edamame",
            "owner_id": 8183
        },
        {
            "id": 223923,
            "name": "Sous Vide Pork Belly",
            "owner_id": 8183
        },
        {
            "id": 14291,
            "name": "Spaghetti Squash",
            "owner_id": null
        },
        {
            "id": 14292,
            "name": "Spinach",
            "owner_id": null
        },
        {
            "id": 223920,
            "name": "Sushi Rice",
            "owner_id": 8183
        },
        {
            "id": 14293,
            "name": "Sweet Potato",
            "owner_id": null
        }
    ]
    }
    ```
   <br>