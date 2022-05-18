INGREDIENTS
==========================

### General Information

1. Search ingredients
   - Description: Get list of ingredient suggestions
   - endpoint_url:
      - ```https://2vppg4p6b0.execute-api.us-east-1.amazonaws.com/search/<OWNER_ID>?name=<NAME>```
   - HTTP Verb:
       - **GET**
       
   Curl request example:
    ```commandline

   curl --location --request GET 'https://2vppg4p6b0.execute-api.us-east-1.amazonaws.com/search/8183?name=S'
   
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

### How would you build this API to scale?
First I'd add security with  token auth in the endpoint with Cognito and secret manager. 
I would have an other endpoint to generate the token. About the database there are several thing to scale like:
Reserve instances, create alarms, optimize queries, use Elastic cache and sqs messages

### What would you do to make each API call as quick as possible always (so its a seamless experience for the users)?
First use elastic cache in the query. Second I would focus directly in the data 
for sample add validations to return information with searches of at least 3 letters and return segments of 50 ingredients. 
The idea is that user received useful information and reduce the time of query in the case our tables hundreds of thousands of records

### If you look at the database raw data itself, any flaws or potential improvements that come to mind?
I think the big problem with table is mixing the system ingredients and user ingredients. That is a big problem because 
reduce the performance sample
If you want to serch an ingredient in the user records and systems you need to
use a DISTINCT or GROUP BY. Because the records are in the same, its not possible to
get directly. The problem with those commands, they are the lastest step to run in the query 
with that db need to more time to remove the duplicates of response. 

My suggestion is create two tables. The first for system ingredients and other for user ingredients with that we win several advantages:
* It's possible to match information with joins and increase the performance.
* We can remove fields like 'system' or remove NULL of index field like owner_id
* Create foraign key and relations one to much or one to one between the table.
* It's possible to add additional field for each table.
* Generate statistics and reports more easily

### Would you do anything to improve the current system ingredient interaction logic (the process described in the “general info” section above)?
* It is related to my previous answer. With two table it's possible to delete any 'flag' field like system 
and delete NULL in owner_id.
* Also improve the query and reduce the use DISTINCT, GROUP BY or subqueries

