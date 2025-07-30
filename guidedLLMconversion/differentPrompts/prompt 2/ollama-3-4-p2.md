### Transport Layer Security (TLS)
#### Configuration Options

Configure transport layer security (TLS) for secure connections.

**Parameters**
cpath Specifies the absolute path to the `x509` certificate file to use 
for TLS. The certificate must be in PEM format. The file may only be 
written by the owner of the file.
kpath Specifies the absolute path to the certificate's `x509` private key 
file to use for TLS. The key must be in PEM format. The file may only be 
read and written by the owner of the file. If kpath is not specified, the 
certificate file must contain the key.
options: [[no]detail]
[ hsto {h|m|s} ]

#### Function
### Configure Transport Layer Security (TLS)
Configure transport layer security (TLS) for secure connections.

#### Defaults
* TLS is not configured and cannot be used. See individual options for the 
defaults should you configure TLS.

#### Notes

1. Normally, a host certificate should be used because the client can use 
it to validate that it connected to the intended host.
2. If you specify the tls directive then you must specify the tlsca 
directive as well.
3. Most TLS trace back messages do not provide any more information than 
the companion explanatory messages and, as such, is only useful for 
debugging purposes.

#### Example
```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```
