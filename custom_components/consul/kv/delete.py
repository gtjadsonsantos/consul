from homeassistant.core import ServiceCall

from consulate import Consul

def delete(call:ServiceCall) -> bool:

    host = call.data.get("host", "")
    port = call.data.get("port", 8500)
    token = call.data.get("token", "")
    datacenter = call.data.get("datacenter", None)
    item = call.data.get("item", None)
    recurse= call.data.get("recurse", False)
                    
    consul = Consul(host=host,token=token,datacenter=datacenter,port=port)
    
    try:
        consul.kv.delete(item,recurse) 
        return True 
    except : 
        return False

        