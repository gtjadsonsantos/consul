# CONSUL

This custom integration permits Home Assistant to communicate with `consul` through  http requests.

## GETTING STARTED

Paste this property `consul:` in your configuration file

## Services

### consul.catalog_register

A a low level mechanism for directly registering or updating entries in the catalog.


```yaml
service: consul.catalog_register
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: prod
  node: raspberry
  service:
    id: redis1
    service: redis
    tags:
      - master
      - v1
    port: 8000
  check:
    node: foobar
    checkid: 'service:redis1'
    name: Redis health check
    notes: Script based health check
    status: passing
    serviceid: redis1

```


### consul.catalog_deregister

Directly remove entries in the catalog.

```yaml
service: consul.catalog_deregister
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  node: raspberry
  datacenter: prod
  service_id: freepbx
  check_id: 'service:freepbx'

```

## LICENSE 📝

This project use license MIT - see file [LICENSE](LICENSE) for more details
## AUTOR

<table>
  <tr>
    <td align="center"><a href="https://github.com/jadson179"><img src="https://avatars0.githubusercontent.com/u/42282908?s=460&u=79ce909209ebf14da91a2d2517c9b0f9e378a4e1&v=4" width="100px;" alt=""/><br /><sub><b>Jadson Santos</b></sub></a><br /><a href="https://github.com/jadson179/controlid/commits?author=jadson179" title="Code">💻</a> <a href="https://github.com/jadson179" title="Design">🎨</a></td>
</table>





 

