## flyawesome-python
Used to provide some extra information about system or geo info to awesomewm via DBus.


### Signals
| name | arguments |   provider   |
|  --- |    ---    |   ---        |
|fly::geoinfo::update| latitude and longitude| GeoClue2 |


### Usage examples
#### geo info
In your awesome config:
```lua
awesome.connect_signal("fly::geoinfo::update",function(latitude,longitude) 
    print(latitude,longitude)
end)
```
If the geo info can be updated from geoclue2, this signal will be emitted.
