### 3.5        tlsca (*required for TLS*)

**xrd.tlsca** **noverify** | {**certdir** | **certfile**} *path* [*options*]

*options*:        [**crlcheck** {**all** | **external** | **last**}]  
                  [**log** {**failure** | **off**}] [[**no**]**proxies**]  
                  [**refresh** *rint*[**h**|**m**|**s**]] [**verdepth** *vdn*]

---

### Function  
Configure client certificate verification for transport layer security (**TLS**).

---

### Parameters  
**noverify**  
Disables client certificate verification. All subsequent parameters are ignored.

**certdir** *path*  
Specifies the absolute path to a directory containing trusted **C**ertificate **A**uthority certificates for verifying client certificates. Each file must contain a single **PEM**-format certificate. Follows **OpenSSL** naming conventions. Directory must be writable only by its owner.

**certfile** *path*  
Specifies the absolute path to a file containing trusted **C**ertificate **A**uthority certificates. Certificates in this file are prioritized over `certdir`. File must be in **PEM** format and writable only by its owner.

**crlcheck**  
Handles certificate revocation lists (**crl**):  
- **all**: Apply **crl** checks to the entire certificate chain  
- **external**: Handle via external plug-in (*default*)  
- **last**: Apply **crl** checks only to the last certificate

**log**  
Controls verification failure logging:  
- **failure**: Log failed verifications (*default*)  
- **off**: Disable logging of failures

**vdn**  
Verification depth (1-256). For certificate chains, verifies up to the last *vdn* certificates. *Default: 9*.

**rint**  
Refresh interval. Suffix with **h** (hours), **m** (minutes), or **s** (seconds). *Default: 8h*.

---

### Defaults  
**xrd.tlsca crlcheck external log failure proxies refresh 8h verdepth 9**

---

### Notes  
1. Both `certdir` and `certfile` can be specified. `certfile` certificates are searched first.  
2. Client certificate verification is unnecessary if all protocols use strong authentication (e.g., **Kerberos**, **GSI**, **SSS**).  
3. Protocols like **HTTPS** require verification. Enable globally to avoid duplicate protocol-specific directives.  
4. Without strong authentication, always verify client certificates. Explicit configuration is required.  
5. Certificates must be in **OpenSSL**-compatible formats.  
6. When using `certdir`, run **OpenSSL**'s `c_rehash` after updates to avoid verification failures during atomic updates.

---

### Example  
**xrd.tlsca certfile /etc/security/xrootd/cacerts.pem**