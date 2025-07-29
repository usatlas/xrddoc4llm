---
## 3.4 TLS (Required for TLS)

---

xrd.tls cpath [ kpath ] [ options ]


**Options:** `[[no]detail] [hsto to{h|m|s}]`

---

### Function

Configure Transport Layer Security (**TLS**).

---

### Parameters

* **`cpath`**
    Specifies the absolute path to the **x509** certificate file to use for **TLS**. The certificate must be in **PEM** format. The file may only be written by the owner.

* **`kpath`**
    Specifies the absolute path to the certificate’s **x509** private key file to use for **TLS**. The key must be in **PEM** format. The file may only be read and written by the owner. If `kpath` is not specified, the certificate file must contain the key.

* **`[no]detail`**
    When `detail` is specified, detailed **TLS** trace back messages are printed along with explanatory messages. The `nodetail` option suppresses **TLS** trace back messages. The default is `nodetail`. Refer to the notes for further explanation.

* **`to`**
    Specifies the maximum amount of time a **TLS** handshake is allowed before the connection closes. The `to` value may be suffixed by **h** for hours, **m** for minutes, or **s** for seconds; otherwise, it defaults to seconds. There is no default time limit for the **TLS** handshake.

---

### Defaults

**TLS** is not configured and cannot be used by default. Refer to individual options for their defaults if you configure **TLS**.

---

### Notes

1.  Normally, a host certificate should be used, as it allows the client to validate that it connected to the intended host.
2.  If you specify the `tls` directive, you must also specify the `tlsca` directive.
3.  Most **TLS** trace back messages offer no more information than their companion explanatory messages and are primarily useful for debugging. This is why `nodetail` is the default. However, if you enable **TLS** tracing using the `xrd.trace` directive, `detail` is enabled regardless of other specifications.

---

### Example

xrd.tls /etc/security/xrootd/hostcert.pem