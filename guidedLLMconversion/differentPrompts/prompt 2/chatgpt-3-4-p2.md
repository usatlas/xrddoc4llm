## 3.4 `tls` *(required for TLS)*

### Syntax

```bash
xrd.tls <cpath> [<kpath>] [options]
```

**Options:**

- `[no]detail`
- `hsto <to>{h|m|s}`

---

### Purpose

Configure **Transport Layer Security (TLS)** for secure communication.

---

### Parameters

- **`cpath`**  
  Absolute path to the `x509` certificate file (in **PEM** format).  
  Must be owner-writable only.

- **`kpath`** *(optional)*  
  Absolute path to the certificate’s `x509` private key file (in **PEM** format).  
  Must be owner-readable/writable only.  
  If omitted, the key must be embedded in the certificate file.

- **`[no]detail`**  
  Enables verbose TLS trace output when `detail` is used.  
  `nodetail` suppresses traceback (default).  
  Useful for debugging only.

- **`to`**  
  Max time allowed for TLS handshake.  
  Units:  
  - `h` = hours  
  - `m` = minutes  
  - `s` = seconds  
  Default unit: seconds.  
  No timeout by default.

---

### Defaults

TLS is **disabled by default**.  
Refer to each option for its default behavior when TLS is enabled.

---

### Notes

1. Use a **host certificate** so clients can verify they are connecting to the correct server.  
2. If you use the `tls` directive, you **must also** configure the `tlsca` directive.  
3. Most TLS trace messages are redundant unless debugging.  
   The `xrd.trace` directive will force-enable `detail` regardless of this setting.

---

### Example

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```
