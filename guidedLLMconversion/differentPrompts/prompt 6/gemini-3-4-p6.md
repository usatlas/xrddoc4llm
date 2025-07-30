---
## 3.4 TLS Configuration (Required)
---

xrd.tls 


### Function
Configures Transport Layer Security (**TLS**) for secure communication.

### Parameters

* **`cpath`** (string, required)
    Specifies the absolute path to the **X.509** certificate file to use for **TLS**. The certificate **must** be in **PEM** format. This file must only be writable by the owner.

* **`kpath`** (string, optional)
    Specifies the absolute path to the certificate's **X.509** private key file to use for **TLS**. The key **must** be in **PEM** format. This file must only be readable and writable by the owner. If `kpath` is not specified, the certificate file (`cpath`) must contain the key.

* **`[no]detail`** (boolean, default: `nodetail`)
    When `detail` is enabled, detailed **TLS** traceback messages are printed alongside explanatory messages. The `nodetail` option suppresses these traceback messages. This is primarily for debugging; see the notes for further explanation.

* **`to`** (time duration, no default)
    Specifies the maximum duration a **TLS** handshake is allowed to take before the connection is closed. The `to` value can be suffixed by `h` for hours, `m` for minutes, or `s` for seconds. If no suffix is provided, the value defaults to seconds.

---
### Defaults
---
**TLS** is not configured by default and cannot be used until explicitly enabled. Refer to individual parameter descriptions for their default values when **TLS** is configured.

---
### Important Notes
---
1.  **Host Validation:** We strongly recommend using a host certificate. This allows clients to validate that they are connecting to the intended server, preventing "man-in-the-middle" attacks.
2.  **`tlsca` Directive:** If you enable the `tls` directive, you **must also** specify the `tlsca` directive. This is crucial for establishing a complete and trusted **TLS** chain.
3.  **Traceback Messages (`[no]detail`):** Most **TLS** traceback messages (`detail`) offer little additional information beyond their companion explanatory messages and are primarily useful for debugging complex issues. Therefore, `nodetail` is the default to avoid unnecessary log clutter. However, if you enable general **TLS** tracing via the `xrd.trace` directive, `detail` will automatically be enabled regardless of this setting.

---
### Usage Example
---
To enable **TLS** using a certificate and key stored in `/etc/security/xrootd/hostcert.pem`:

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
In this example, the certificate file hostcert.pem is assumed to contain both the certificate and its private key. If the key were in a separate file, say /etc/security/xrootd/hostkey.pem, the command would be:

Bash

xrd.tls /etc/security/xrootd/hostcert.pem /etc/security/xrootd/hostkey.pem