from homeassistant.core import ServiceCall
from requests import put
import json
import logging
_LOGGER = logging.Logger(__name__)

def deregister(call:ServiceCall) -> bool:

    host = call.data.get("host", None)
    protocol = call.data.get("protocol", "http")
    port = call.data.get("port", 8500)
    token = call.data.get("token", None)
    
    node = call.data.get("node", "")
    datacenter = call.data.get("datacenter", None)
    service_id = call.data.get("service_id", None)
    check_id = call.data.get("check_id", None)
    ns = call.data.get("ns", None)

    payload = {}
    headers = {}  

    if datacenter:
        payload['datacenter'] = datacenter
    if node:
        payload['node'] = node
    if check_id:
        payload['checkid'] = check_id
    if service_id:
        payload['serviceid'] = service_id
    if ns:
        payload['ns'] = ns
    if token:
        headers['X-Consul-Token'] = token
    
    try:
        put("{protocol}://{host}:{port}/v1/catalog/deregister".format(protocol=protocol,host=host,port=port),
        data=json.dumps(payload),
        headers=headers)
        return True
    except IOError as e :
        _LOGGER.exception(e)
        return False
    





