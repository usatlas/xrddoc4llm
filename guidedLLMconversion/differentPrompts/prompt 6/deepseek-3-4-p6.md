# 3.4 TLS Configuration (required for TLS)

```toc
- [Command Syntax](#command-syntax)
- [Parameters](#parameters)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)
```

---

## Command Syntax

```bash
xrd.tls <cert-path> [<key-path>] [options]
```

**Options:**

```bash
[[no]detail] [hsto <timeout>{h|m|s}]
```

---

## Parameters

### Required

`<cert-path>`  
Path to PEM-format x509 certificate file  
**Permissions:** Owner write-only (`600`)  
**Example:** `/etc/security/xrootd/hostcert.pem`

### Optional

`<key-path>`  
Path to PEM-format private key (if separate from cert)  
**Permissions:** Owner read/write-only (`600`)

### Options

`[no]detail`  
- `detail`: Enable verbose TLS debugging  
- `nodetail`: Default (quieter operation)

`hsto <timeout>`  
Set handshake timeout  
**Units:**  
- `h` = hours  
- `m` = minutes  
- `s` = seconds  
**Default:** No timeout

---

## Examples

### Basic Configuration

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```

### Advanced Configuration

```bash
xrd.tls /etc/certs/server.pem /etc/keys/server.key \
  detail hsto 30s
```

---

## Troubleshooting

### Common Issues

1. **Permission Errors**  
   Verify permissions:

   ```bash
   ls -l /etc/security/xrootd/hostcert.pem
   ```

   Should show: `-rw-------`

2. **Certificate Validation**  
   Test with:

   ```bash
   openssl x509 -in /path/to/cert.pem -text -noout
   ```

3. **Timeout Issues**  
   Increase handshake timeout:

   ```bash
   xrd.tls /path/to/cert.pem hsto 2m
   ```

### Debugging

Enable detailed logging:

```bash
xrd.tls /path/to/cert.pem detail
```

---

## Best Practices

- Use Let's Encrypt or a trusted CA for certificates
- Set strict file permissions (`600`)
- Monitor handshake times for latency issues
- Rotate certificates regularly
- Always pair `xrd.tls` with `xrd.tlsca` for proper validation

---

## Feedback

**Feedback Welcome**  
Found an issue? [Open a ticket](https://github.com/xrootd/xrootd/issues)
