from homeassistant.core import ServiceCall

from consulate import Consul

def setOne(call:ServiceCall) -> bool:

    host = call.data.get("host", "")
    port = call.data.get("port", 8500)
    token = call.data.get("token", "")
    datacenter = call.data.get("datacenter", None)
    data = call.data.get("data", {"item": None, "value": None})
                    
    consul = Consul(host=host,token=token,datacenter=datacenter,port=port)
    
    try:
        consul.kv.set(data["item"],data["value"])
        return True 
    except : 
        return False
    
    
def setMany(call:ServiceCall) -> bool:

    host = call.data.get("host", "")
    port = call.data.get("port", 8500)
    token = call.data.get("token", "")
    datacenter = call.data.get("datacenter", None)
    datas = call.data.get("datas", [])
                    
    consul = Consul(host=host,token=token,datacenter=datacenter,port=port)
    
    try:
        for item in datas:
            consul.kv.set(item["item"],item["value"])
        return True 
    except : 
        return False




