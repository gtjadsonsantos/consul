from homeassistant.core import ServiceCall
import logging

from consulate import Consul
from consulate.exceptions import Forbidden

_LOGGER = logging.Logger(__name__)


def create(call:ServiceCall) -> bool:

    host = call.data.get("host", "")
    port = call.data.get("port", 8500)
    token = call.data.get("token", "")
    name = call.data.get("name", "")
    datacenter = call.data.get("datacenter", None)
    rules = call.data.get("rules", "")
    acl_type = call.data.get("acl_type", "client")
                    
    consul = Consul(host=host,token=token,datacenter=datacenter,port=port)
    
    try:
        consul.acl.create(
           acl_type=acl_type,
           name=name,
           rules=rules
        )
    except Forbidden as e :
        _LOGGER.exception(e,e.args)


    
    





