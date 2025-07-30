# 3.4 TLS  
(*required* for TLS)

---

## Table of Contents

- [Function](#function)  
- [Parameters](#parameters)  
- [Options](#options)  
- [Defaults](#defaults)  
- [Notes](#notes)  
- [Example](#example)  

---

## Function

Configure transport layer security (**TLS**).

---

## Parameters

**cpath**  
Specifies the absolute path to the **x509** certificate file to use for **TLS**. The certificate **must** be in **PEM** format. The file **may only be written by the owner** of the file.

**kpath**  
Specifies the absolute path to the certificate’s **x509** private key file to use for **TLS**. The key **must** be in **PEM** format. The file **may only be read and written by the owner** of the file.  
If *kpath* is not specified then the certificate file **must contain the key**.

---

## Options

```plaintext
[ [ no ] detail ]     # Enable or suppress detailed TLS trace back messages
[ hsto to{h|m|s} ]    # Set handshake timeout: suffix h=hours, m=minutes, s=seconds (default is seconds)
```

| Option         | Description                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------|
| `detail`       | Prints detailed TLS trace back messages along with explanatory messages.                                  |
| `nodetail`     | Suppresses TLS trace back messages (default).                                                             |
| `hsto to`      | Specifies the maximum allowed time for a TLS handshake before the connection is closed.                   |
| `to` suffixes  | `h` = hours, `m` = minutes, `s` = seconds (default if no suffix).                                          |

---

## Defaults

TLS is **not** configured by default and cannot be used. See individual options above for default behaviors if you configure TLS.

---

## Notes

> ⚠️ **Security Warning:**  
>  
> - Always ensure your certificate and key files have strict file permissions (read/write only by the owner).  
> - Misconfigurations can lead to security vulnerabilities or connection failures.  

1. Normally, a host certificate should be used because the client can use it to validate it connected to the intended host.

2. If you specify the **tls** directive, you **must** specify the **tlsca** directive as well.

3. Most TLS trace back messages do not provide more info than the companion explanatory messages and are mainly useful for debugging. This is why `nodetail` is the default.  
   However, if TLS tracing is enabled using the **xrd.trace** directive, `detail` is enabled regardless of this setting.

---

## Example

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```

---
