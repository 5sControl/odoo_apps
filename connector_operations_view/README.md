# API Documentation
`GET /fives/ping`
__Description:__ A simple endpoint to check if the server is up and running.

__Response:__

```json
{
  "success": true
}
```

`GET /fives/operations`
__Description:__ Retrieve a list of operations within the specified time interval.

__Parameters:__
* ###### from_time: (string) Start of the time interval in ISO format (e.g., "2023-07-20T00:00:00").
* ###### to_time: (string) End of the time interval in ISO format (e.g., "2023-07-21T00:00:00").

__Response:__

```json
[
    {
        "oprtTypeID": 4,
        "oprtName": "Workplace Name",
        "oprs": [
            {
                "id": 8,
                "orId": 34,
                "name": "Order Name",
                "sTime": 1111111111,
                "eTime": 1111111111
            },
            {
                "id": 9,
                "orId": 34,
                "name": "Order Name",
                "sTime": 1111111111,
                "eTime": 1111111111
            }
        ]
    }
    
]
```

`GET /fives/orders`
__Description:__ Retrieve a list of orders with operations within the specified time interval.

__Query Parameters:__

* ###### from_time: (string) Start of the time interval in ISO format (e.g., "2023-07-20T00:00:00").
* ###### to_time: (string) End of the time interval in ISO format (e.g., "2023-07-21T00:00:00").
Response:

```json
[
  {
    "orderId": "1001",
    "orderName": "Order ABC"
  },
  {
    "orderId": "1002",
    "orderName": "Order XYZ"
  }
  
]
```