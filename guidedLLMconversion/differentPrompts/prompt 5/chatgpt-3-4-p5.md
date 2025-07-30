## 3.4 `tls` (required for TLS)

### Command Syntax

```bash
xrd.tls <cpath> [<kpath>] [<options>]
```

**Options:**

```bash
[[no]detail] [hsto to{h|m|s}]
```

---

### Function

Configure Transport Layer Security (**TLS**) for secure communication between clients and servers.

---

### Parameters

#### `cpath`

Path to the **x509 certificate** file to be used for TLS.

- Must be in **PEM format**
- File must be **writable only by the owner**

#### `kpath`

Path to the **x509 private key** file to be used with the certificate.

- Must also be in **PEM format**
- File must be **readable and writable only by the owner**
- If not provided, the key must be embedded within the `cpath` file

#### `[no]detail`

Controls whether detailed TLS traceback messages are printed.

- `detail`: enables verbose messages
- `nodetail`: suppresses them (**default**)
- Useful for debugging and protocol traceability

#### `hsto to{h|m|s}`

Sets the **maximum allowed time** for the TLS handshake to complete.

- `to` can be suffixed with `h`, `m`, or `s` for **hours**, **minutes**, or **seconds**
- If no suffix is provided, it defaults to **seconds**
- **No default time limit** is enforced if not set

---

### Defaults

TLS is **not configured by default** and must be explicitly enabled.  
Refer to each parameter above for their specific default behavior.

---

### Notes

1. **Host Certificates Recommended**  
   Clients can use host certificates to validate that they are communicating with the correct server.

2. **TLS Requires `tlsca` Directive**  
   The `tls` directive must be paired with the `tlsca` directive to define the Certificate Authority.

3. **Tracebacks Are for Debugging**  
   Most TLS trace back messages do not provide additional information beyond standard error output.  
   The default is `nodetail`, but if you enable tracing via `xrd.trace`, the `detail` flag is automatically activated regardless of explicit configuration.

---

### Example

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```
