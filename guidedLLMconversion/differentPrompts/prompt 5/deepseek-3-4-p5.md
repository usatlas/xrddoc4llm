# 3.4 TLS Configuration (required for TLS)

## Command Syntax
xrd.tls cpath [kpath] [options]

text

**Options:**
[[no]detail] [hsto to{h|m|s}]

text

## Function

Configure Transport Layer Security (TLS).

## Parameters

### `cpath`
- **Type**: Absolute path (string)
- **Format**: PEM format
- **Permissions**: Writable only by owner
- **Description**:  
  Specifies the path to the x509 certificate file for TLS

### `kpath` (optional)
- **Type**: Absolute path (string)
- **Format**: PEM format
- **Permissions**: Readable/writable only by owner
- **Description**:  
  Specifies the path to the private key file. If omitted, the certificate file must contain the key.

### Options

#### `[no]detail`
- **Default**: `nodetail`
- **Behavior**:
  - `detail`: Enables detailed TLS trace messages
  - `nodetail`: Suppresses trace messages (default)

#### `hsto to{h|m|s}`
- **Purpose**: Sets maximum TLS handshake time
- **Units**:
  - `h`: Hours
  - `m`: Minutes
  - `s`: Seconds (default)
- **Note**: No default time limit

## Defaults

- TLS is **disabled** by default
- Must be explicitly configured

## Notes

1. **Host Certificates Recommended**  
   Ensures clients can validate server identity

2. **Requires `tlsca` Directive**  
   Must specify Certificate Authority when enabling TLS

3. **Debugging Considerations**:
   - Trace messages primarily useful for:
     - Protocol troubleshooting
     - Connection issues
     - Security audits
   - `nodetail` is default to avoid exposing sensitive info
   - Overridden by `xrd.trace` directive

## Example

Basic configuration:
xrd.tls /etc/security/xrootd/hostcert.pem

text

With private key:
xrd.tls /etc/security/certs/server.pem /etc/security/keys/server.key

text

Verbose mode with timeout:
xrd.tls /path/to/cert.pem detail hsto 30s

text

## File Structure Recommendations
/etc/security/
├── xrootd/
│ └── hostcert.pem
├── certs/
│ └── server.pem
└── keys/
└── server.key

text

## Best Practices

1. Set strict file permissions:
chmod 600 /etc/security/keys/server.key
chmod 644 /etc/security/certs/server.pem

text

2. Use Let's Encrypt for certificates:
certbot certonly --standalone -d yourdomain.com

text

3. Test configuration:
openssl s_client -connect yourhost:port -showcerts