from homeassistant.core import ServiceCall
from requests import put
import json
import logging

_LOGGER = logging.Logger(__name__)


def service_register(call: ServiceCall) -> bool:

    host = call.data.get("host", None)
    protocol = call.data.get("protocol", "http")
    host_port = call.data.get("host_port", 8500)
    token = call.data.get("token", None)

    datacenter = call.data.get("datacenter", None)
    node_id = call.data.get("id", None)
    node = call.data.get("node", None)
    address = call.data.get("address", None)
    taggedaddresses = call.data.get("taggedaddresses", None)
    node_meta = call.data.get("node_meta", None)
    service = call.data.get("service", None)
    check = call.data.get("check", None)

    payload = {}
    headers = {}

    if datacenter:
        payload['datacenter'] = datacenter
    if node_id:
        payload['id'] = node_id
    if node:
        payload['node'] = node
    if address:
        payload['address'] = address
    if taggedaddresses:
        payload['taggedaddresses'] = taggedaddresses
    if node_meta:
        payload['nodemeta'] = node_meta
    if service:
        payload['service'] = service
    if check:
        payload['check'] = check
    if token:
        headers['X-Consul-Token'] = token
    try:
        response = put("{protocol}://{host}:{host_port}/v1/catalog/register".format(protocol=protocol, host=host, host_port=host_port),
                       data=json.dumps(payload),
                       headers=headers)
        return response.__bool__()
    except IOError as e:
        _LOGGER.exception(e)
        return False


def service_deregister(call: ServiceCall) -> bool:

    host = call.data.get("host", None)
    protocol = call.data.get("protocol", "http")
    host_port = call.data.get("host_port", 8500)
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
        response = put("{protocol}://{host}:{host_port}/v1/catalog/deregister".format(protocol=protocol, host=host, host_port=host_port),
                       data=json.dumps(payload),
                       headers=headers)
        return response.__bool__()
    except IOError as e:
        _LOGGER.exception(e)
        return False
