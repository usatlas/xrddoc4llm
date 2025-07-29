# 3.4 `tls` — Required for TLS

> Configure secure communication using Transport Layer Security (TLS) in XRootD.

---

## 📘 Overview

The `xrd.tls` directive enables TLS support for secure client-server communication. It specifies the certificate and key files and allows optional tuning for trace verbosity and handshake timeouts.

---

## 🔧 Syntax

```bash
xrd.tls <cpath> [<kpath>] [options]
```

### Options

- `[no]detail`  
  Enables or disables detailed TLS trace messages. Default is `nodetail`.

- `hsto <to>{h|m|s}`  
  Sets the maximum time allowed for a TLS handshake.  
  Units:
  - `h` = hours  
  - `m` = minutes  
  - `s` = seconds  
  If no unit is specified, seconds are assumed.

---

## 🛠️ Function

Defines how the server uses TLS to secure client connections.

---

## 📌 Parameters

| Parameter | Description |
|----------|-------------|
| `cpath`  | Absolute path to the X.509 certificate file in PEM format. Must be writable only by the file owner. |
| `kpath` *(optional)* | Absolute path to the X.509 private key file in PEM format. Must be readable and writable only by the file owner. If omitted, the key must be embedded in the certificate file. |
| `[no]detail` | Enables (`detail`) or disables (`nodetail`) verbose TLS tracebacks. Useful for debugging. |
| `to` | Maximum time allowed for a TLS handshake before the connection is closed. Accepts `h`, `m`, or `s` suffixes. No default timeout. |

---

## ⚙️ Defaults

TLS is not configured by default and cannot be used unless explicitly enabled.  
Each option has its own default behavior:

- `detail`: default is `nodetail`
- `to`: no default timeout

---

## 📝 Notes

1. A host certificate is recommended so clients can verify the server identity.
2. If you use `xrd.tls`, you must also configure `xrd.tlsca`.
3. Most TLS tracebacks are redundant with standard logs. Use `detail` only for debugging.
4. If `xrd.trace` is enabled, `detail` is automatically turned on regardless of this setting.

---

## ✅ Example

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```

---

## 💡 Tip

Use the following checklist when enabling TLS:

- [ ] Ensure the certificate file is in PEM format and has correct permissions.
- [ ] If using a separate key file, confirm it is also PEM and secure.
- [ ] Add the `xrd.tlsca` directive to specify trusted certificate authorities.
- [ ] Use `xrd.trace` with care—verbose output can impact performance.

---

## 🔗 Related Directives

- [`xrd.tlsca`](#) — Specifies the CA certificates used to verify clients.
- [`xrd.trace`](#) — Enables detailed tracing, including TLS internals.

---

## 🧪 Try It Yourself

Paste this into your config file and restart the daemon:

```bash
xrd.tls /etc/xrootd/certs/server.pem /etc/xrootd/certs/server.key detail hsto 10s
```

Then test with:

```bash
openssl s_client -connect yourserver:1094
```

---

## 📂 Resources

- [XRootD TLS Documentation](https://xrootd.slac.stanford.edu/)
- [OpenSSL PEM Format Guide](https://www.openssl.org/docs/manmaster/man1/openssl-pem.html)

```