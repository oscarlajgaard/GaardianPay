# Gateway Service

#Usage

**Our service will create a session with an id. The id will be bound to the product and payment**  
Here's an example.

```json
{
    "session_id":"679ca7ed18df4c70a33020e199c8111f",
    "amount":"700",
    "currency":"DKK",
    "redirect":"https://youtube.com/"
}
``` 

**When we've got a pending payment with a valid session_id, we can recieve a post with some card details.**  
Here's an example of what that will look like. No, these are not real credentials!
```json
{
    "session_id":"679ca7ed18df4c70a33020e199c8111f",
    "cardnumber":"4571000000000001",
    "expiration[month]":"01",
    "expiration[year]":"24",
    "cvd":"222"
}
```


*If the payment is accepted, this is what it will look like*
```json
{
    "message": "Payment complete!",
    "data": 1
}
```
