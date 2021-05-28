from homeassistant.core import ServiceCall
import logging

from consulate import Consul
from consulate.exceptions import (Forbidden,NotFound)

_LOGGER = logging.Logger(__name__)


def update(call:ServiceCall) -> bool:

    host = call.data.get("host", "")
    port = call.data.get("port", 8500)
    token = call.data.get("token", "")
    datacenter = call.data.get("datacenter", None)
    acl_id = call.data.get("acl_id", None)
    name = call.data.get("name", None)
    acl_type = call.data.get("acl_type", "client")
    rules = call.data.get("rules", None)
                    
    consul = Consul(host=host,token=token,datacenter=datacenter,port=port)
    
    try:
        consul.acl.update(acl_id=acl_id,acl_type=acl_type,name=name,rules=rules)
    except Forbidden as e :
        _LOGGER.exception(e,e.args)

        



    





