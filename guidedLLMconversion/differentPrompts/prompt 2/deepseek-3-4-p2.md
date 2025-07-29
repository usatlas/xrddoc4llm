# 3.4 TLS Configuration
xrd.tls <cert_path> [<key_path>] [options]

## Required Parameters
| Parameter | Description |
|-----------|-------------|
| `cert_path` | Path to X.509 certificate (PEM format) |
| `key_path` | Path to private key (PEM format, optional if key included in cert) |

## Configuration Options
| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `[no]detail` | `detail`/`nodetail` | `nodetail` | TLS debug logging |
| `hsto` | `<num>h`/`<num>m`/`<num>s` | none | Handshake timeout |

## Example Configurations

# Basic configuration
```ini
xrd.tls /etc/xrootd/tls/cert.pem
```
# Full configuration
```ini
xrd.tls /etc/xrootd/tls/cert.pem /etc/xrootd/tls/key.pem hsto 30s detail
```

## Implementation Notes
1. **Security Requirements**:
   - Files must be owned by service account
   - Recommended permissions:
     ```
     chmod 600 /etc/xrootd/tls/{cert,key}.pem
     chown xrootd:xrootd /etc/xrootd/tls/{cert,key}.pem
     ```

2. **Dependencies**:
   - Requires `tlsca` directive for CA bundle
   - Certificate should match server hostname

3. **Troubleshooting**:
   - Verify certificate chain:
     ```
     openssl verify -CAfile ca_bundle.pem cert.pem
     ```
   - Check handshake:
     ```
     openssl s_client -connect host:port -showcerts
     ```

## Best Practices
- Use separate files for cert and key
- Set reasonable timeout (30-120 seconds)
- Monitor TLS handshake metrics
- Rotate certificates regularly