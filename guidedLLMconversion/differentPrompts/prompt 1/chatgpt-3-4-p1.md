## 3.4 tls *(required for TLS)*

xrd.tls cpath [kpath] [options]

**options**:  
- `[[no]detail]`  
- `hsto to{h|m|s}`

### Function

Configure transport layer security (**TLS**).

### Parameters

- **`cpath`**  
  Specifies the absolute path to the **x509** certificate file to use for **TLS**.  
  - The certificate must be in **PEM** format.  
  - The file may only be written by the owner.

- **`kpath`**  
  Specifies the absolute path to the certificate’s **x509** private key file.  
  - The key must be in **PEM** format.  
  - The file must be owner-readable and writable only.  
  - If `kpath` is not specified, the certificate file must include the key.

- **`[no]detail`**  
  - When `detail` is specified, detailed **TLS** trace messages are printed with explanations.  
  - `nodetail` suppresses these messages.  
  - Default: `nodetail`.  
  - See notes below for more.

- **`to`**  
  Specifies the maximum time a **TLS** handshake can take before closing the connection.  
  - The value may be suffixed by:
    - `h` for hours  
    - `m` for minutes  
    - `s` for seconds  
  - If no suffix is given, seconds are assumed.  
  - Default: no time limit.

### Defaults

**TLS** is not configured and cannot be used unless explicitly enabled.  
Refer to the options for their individual defaults when configuring **TLS**.

### Notes

1. Normally, a host certificate should be used so clients can verify they connected to the intended host.  
2. If you specify the `tls` directive, you **must** also specify the `tlsca` directive.  
3. Most **TLS** trace messages offer little additional value beyond the explanatory messages.  
   - As such, `nodetail` is the default.  
   - If you enable TLS tracing via the `xrd.trace` directive, `detail` is enabled regardless of your setting.

### Example

```bash
xrd.tls /etc/security/xrootd/hostcert.pem