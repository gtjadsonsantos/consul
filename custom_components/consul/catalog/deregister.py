from homeassistant.core import ServiceCall

from consulate import Consul

def deregister(call:ServiceCall) -> bool:

    host = call.data.get("host", "")
    port = call.data.get("port", 8500)
    token = call.data.get("token", "")
    node = call.data.get("node", "")
    datacenter = call.data.get("datacenter", None)
    service_id = call.data.get("service_id", None)
    check_id = call.data.get("check_id", None)
                    
    consul = Consul(host=host,token=token,datacenter=datacenter,port=port)
    
    return consul.catalog.deregister(
        node=node,
        check_id=check_id,
        datacenter=datacenter,
        service_id=service_id
    )
    
    





