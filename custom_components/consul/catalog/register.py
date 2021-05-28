from homeassistant.core import ServiceCall
from consulate import Consul

def register(call: ServiceCall) -> bool:

    host = call.data.get("host", "")
    port = call.data.get("port", 8500)
    token = call.data.get("token", "")
    datacenter = call.data.get("datacenter", None)
    node = call.data.get("node", "")
    service = call.data.get("service", None)
    check = call.data.get("check", None)

    consul = Consul(host=host, token=token, datacenter=datacenter, port=port)

    return consul.catalog.register(
        node=node,
        address=host,
        datacenter=datacenter,
        service=service,
        check=check)
