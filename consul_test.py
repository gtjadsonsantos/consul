from custom_components.consul.const import DOMAIN
from homeassistant.core import Context, ServiceCall
from custom_components import consul

PAYLOAD_CATALOG_REGISTER = {
    "host": "192.168.0.21",
    "host_port": 8500,
    "token": "57c5d69a-5f19-469b-0543-12a487eecc66",
    "datacenter": "dc1",
    "node": "jadson",
    "address": "192.168.0.21",
    "service": {
        "id": "jadson",
        "service": "jadson",
        "address": "192.168.0.21",
        "tags": [
            "master",
            "v1"
        ],
        "port": 8123
    },
    "check": {
        "node": "jadson",
        "checkid": "service:jadson",
        "name": "Redis health check",
        "notes": "Script based health check",
        "status": "passing",
        "definition": {
            "tcp": "192.168.0.21:8123",
            "interval": "5s",
            "timeout": "1s",
            "deregistercriticalserviceafter": "30s"
        },
        "serviceid": "jadson"
    }
}

PAYLOAD_CATALOG_DEREGISTER = {
    "host": PAYLOAD_CATALOG_REGISTER["host"],
    "host_port": PAYLOAD_CATALOG_REGISTER["host_port"],
    "token": PAYLOAD_CATALOG_REGISTER["token"],
    "node": PAYLOAD_CATALOG_REGISTER["node"],
    "datacenter": PAYLOAD_CATALOG_REGISTER["datacenter"],
    "service_id": PAYLOAD_CATALOG_REGISTER["service"]["id"],
    "check_id": PAYLOAD_CATALOG_REGISTER["check"]["checkid"]
}

PAYLOAD_KV_CREATE_OR_UPDATE = {
    "host": PAYLOAD_CATALOG_REGISTER["host"],
    "host_port": PAYLOAD_CATALOG_REGISTER["host_port"],
    "token": PAYLOAD_CATALOG_REGISTER["token"],
    "key": "jadson179",
    "value": "https://github.com/jadson179",
}

PAYLOAD_KV_DELETE = {
    "host": PAYLOAD_CATALOG_REGISTER["host"],
    "host_port": PAYLOAD_CATALOG_REGISTER["host_port"],
    "token": PAYLOAD_CATALOG_REGISTER["token"],
    "key": PAYLOAD_KV_CREATE_OR_UPDATE["key"]
}

PAYLOAD_AGENT_SERVICE_REGISTER = {
    "host": PAYLOAD_CATALOG_REGISTER["host"],
    "host_port": PAYLOAD_CATALOG_REGISTER["host_port"],
    "token": PAYLOAD_CATALOG_REGISTER["token"],
    "id": "redis1",
    "name": "redis",
    "tags": ["primary", "v1"],
    "address": "127.0.0.1",
    "port": 8000,
    "meta": {
        "redis_version": "4.0"
    },
    "enabletagoverride": False,
    "weights": {
        "passing": 10,
        "warning": 1
    }
}

PAYLOAD_AGENT_SERVICE_DEREGISTER = {
    "host": PAYLOAD_CATALOG_REGISTER["host"],
    "host_port": PAYLOAD_CATALOG_REGISTER["host_port"],
    "token": PAYLOAD_CATALOG_REGISTER["token"],
    "service_id": PAYLOAD_AGENT_SERVICE_REGISTER["id"]
    
}






def test_catalog_register():

    serviceCall = ServiceCall(
        domain=DOMAIN, service="catalog_register", data=PAYLOAD_CATALOG_REGISTER, context=Context())

    assert consul.catalog.service_register(call=serviceCall) == True


def test_catalog_deregister():
    serviceCall = ServiceCall(
        domain=DOMAIN, service="catalog_deregister", data=PAYLOAD_CATALOG_DEREGISTER, context=Context())

    assert consul.catalog.service_deregister(call=serviceCall) == True


def test_kv_create_or_update():
    serviceCall = ServiceCall(
        domain=DOMAIN, service="kv_create_or_update", data=PAYLOAD_KV_CREATE_OR_UPDATE, context=Context())

    assert consul.kv.create_or_update(call=serviceCall) == True


def test_kv_delete():
    serviceCall = ServiceCall(
        domain=DOMAIN, service="kv_delete", data=PAYLOAD_KV_DELETE, context=Context())

    assert consul.kv.delete(call=serviceCall) == True


def test_agent_service_register():
    serviceCall = ServiceCall(
        domain=DOMAIN, service="agent_service_register", data=PAYLOAD_AGENT_SERVICE_REGISTER, context=Context())

    assert consul.agent.service_register(call=serviceCall) == True

def test_agent_service_deregister():
    serviceCall = ServiceCall(
        domain=DOMAIN, service="agent_service_deregister", data=PAYLOAD_AGENT_SERVICE_DEREGISTER, context=Context())

    assert consul.agent.service_deregister(call=serviceCall) == True
