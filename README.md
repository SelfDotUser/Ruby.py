<img src="./.github/ruby-banner.png">

# Ruby.py
Thank you for using the Ruby API. I don’t personally like using raw APIs, so I designed Ruby.py for personal ease. 
Welcome to the Python side of Ruby.

# Requirements
This project uses:
```
requests==2.25.1
```

# Examples
## Authentication + Get Weight Example
Ruby uses Basic HTTP authentication. To access a user’s weight data, you need to authenticate using their username and 
passcode.

Here’s an example:
```python
import Ruby

# Authentication
user = Ruby.User("some_user_id", "123456")

# Getting weight data. See below to learn how to use it.
data = user.get_weight("2021-12")
```


## Using Weight Data
When you use `User.get_weight()` or `User.update_weight()`, you’re given WeightData. WeightData has two attributes: 
`weight` and `message`. It’s good practice to check `message` for any errors. Error messages can be found in the 
[Ruby API documentation](https://github.com/SelfDotUser/Ruby-Server).

When you use the `weight` attribute, you get a dictionary response similar to:
```json
{
    "2021-12-05": 197.0,
    "2021-12-10": 197.0
}
```

## Creating a new user
If you’d like to create a new user for the Ruby API, you need to use the Client class.

Here’s an example:
```python
import Ruby

message = Ruby.Client.new_user("username", "passcode")
print(message)
```
The message should print "SUCCESS" or an error message.

# API Documentation
Below you will find classes/methods available in Ruby.py.

## User
### Methods
|Method|Return Type|Description|
|---|---|---|
|`get_weight(month)`|WeightData|Returns a user's weight data.|
|`update_weight(weight)`|WeightData|Updates a user's weight and returns their updated weight data.|

## Client
### Methods
|Method|Return Type|Description|
|---|---|---|
|`new_user(user_id, passcode)`|String|Creates a new user, returns a status message.|

## WeightData
### Attributes
|Attribute|Return Type|Description|
|---|---|---|
|`weight`|dict|Returns a dictionary of a user's weight data.|
|`message`|String|Returns either "SUCCESS" or an error message. Refer to the [Ruby API documentation](https://github.com/SelfDotUser/Ruby-Server) for error message support. It should be standard practice to inspect `message` for any errors.|