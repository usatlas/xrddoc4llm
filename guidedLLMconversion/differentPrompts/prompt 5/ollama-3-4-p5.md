# Transport Layer Security (TLS)
## Configuration Options
### Overview

Configure transport layer security (TLS) for secure connections.

### Defaults

* TLS is not configured and cannot be used. See individual options for the 
defaults should you configure TLS.

### Notes

1. Normally, a host certificate should be used because the client can use 
it to validate that it connected to the intended host.
2. If you specify the `tls` directive then you must specify the `tlsca` 
directive as well.
3. Most TLS trace back messages do not provide any more information than 
the companion explanatory messages and, as such, is only useful for 
debugging purposes.

## Parameters

### cpath

Specifies the absolute path to the `x509` certificate file to use for TLS. 
The certificate must be in PEM format. The file may only be written by the 
owner of the file.

### kpath

Specifies the absolute path to the certificate’s `x509` private key file 
to use for TLS. The key must be in PEM format. The file may only be read 
and written by the owner of the file. If `kpath` is not specified then the 
certificate file must contain the key.

## Function

Configure transport layer security (TLS) for secure connections.

### Usage

```bash
xrd.tls [options] cpath [kpath]
```
where:

* `cpath` specifies the absolute path to the `x509` certificate file to 
use for TLS.
* `kpath` specifies the absolute path to the certificate’s `x509` private 
key file to use for TLS.

### Examples

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```
specifies the absolute path to the `x509` certificate file to use for TLS, 
and leaves the private key at its default location.

```bash
xrd.tls /etc/security/xrootd/hostcert.pem 
kpath=/etc/security/xrootd/hostkey.pem
```
specifies both the absolute path to the `x509` certificate file to use for 
TLS and the absolute path to the certificate’s `x509` private key file to 
use for TLS.

```bash
xrd.tls cpath=/etc/security/xrootd/hostcert.pem kpath=
```
specifies only the absolute path to the `x509` certificate file to use for 
TLS, and leaves the private key at its default location.

### Tips

* Normally, a host certificate should be used because the client can use 
it to validate that it connected to the intended host.
* If you specify the `tls` directive then you must specify the `tlsca` 
directive as well.
* Most TLS trace back messages do not provide any more information than 
the companion explanatory messages and, as such, is only useful for 
debugging purposes.

### See Also

* [xrd.tls](#xrd.tls)
* [xrd.trace](#xrd.trace)

## Options

* `options`: Specifies the options to use with TLS.
	+ `[no]detail`: Specifies whether detailed TLS trace back messages are 
printed along with explanatory messages.
	+ `[hsto {h|m|s}]`: Specifies the maximum amount of time a TLS handshake 
is allowed to take before the connection is closed.

## Defaults

* `TLS` is not configured and cannot be used. See individual options for 
the defaults should you configure `TLS`.

## Notes

1. Normally, a host certificate should be used because the client can use 
it to validate that it connected to the intended host.
2. If you specify the `tls` directive then you must specify the `tlsca` 
directive as well.
3. Most TLS trace back messages do not provide any more information than 
the companion explanatory messages and, as such, is only useful for 
debugging purposes.

## Troubleshooting

1. If you encounter issues with TLS, check that your certificate file is 
in PEM format and that the private key file is readable by the owner of 
the file.
2. If you still encounter issues, try specifying the `tls` directive along 
with the `tlsca` directive to ensure that the client can validate the 
connection.

## Related Topics

* [xrd.tls](#xrd.tls)
* [xrd.trace](#xrd.trace)