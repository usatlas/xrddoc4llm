## 3.4 `tls` (required for TLS)

### 🔧 Syntax

```bash
xrd.tls <cpath> [<kpath>] [options]
```

**Options:**

- `[no]detail` — Enables or disables detailed TLS trace messages. Default is `nodetail`.
- `hsto <to>{h|m|s}` — Sets the maximum time allowed for a TLS handshake. Units: hours (`h`), minutes (`m`), or seconds (`s`). Defaults to seconds if no unit is specified.

---

### 🛠️ Function

Configure Transport Layer Security (TLS) for the server.

---

### 📌 Parameters

- **`cpath`**  
  Absolute path to the X.509 certificate file in PEM format. Must be writable only by the file owner.

- **`kpath`** *(optional)*  
  Absolute path to the X.509 private key file in PEM format. Must be readable and writable only by the file owner. If omitted, the key must be included in the certificate file.

- **`[no]detail`**  
  When `detail` is specified, detailed TLS trace messages are printed. `nodetail` suppresses them (default). Useful for debugging.

- **`to`**  
  Maximum time allowed for a TLS handshake before the connection is closed. Accepts suffixes:  
  - `h` = hours  
  - `m` = minutes  
  - `s` = seconds  
  If no suffix is provided, seconds are assumed. There is no default timeout.

---

### ⚙️ Defaults

TLS is not configured by default and cannot be used unless explicitly enabled.  
See individual options for their respective defaults.

---

### 📝 Notes

1. It's recommended to use a host certificate so clients can validate the server identity.
2. If you use `xrd.tls`, you must also configure `xrd.tlsca`.
3. Most TLS trace messages are redundant with explanatory logs. Use `detail` only for debugging.  
   If `xrd.trace` is enabled, `detail` is automatically turned on regardless of this setting.

---

### ✅ Example

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```
