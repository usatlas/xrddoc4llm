# Transport Layer Security (TLS)

## Configuration Options

This section describes how to configure transport layer security (TLS) for 
secure connections.

### Defaults

By default, TLS is not configured and cannot be used. If you wish to 
enable TLS, please consult the documentation for individual options that 
provide defaults.

## Parameters

The following parameters can be used to configure transport layer 
security:

### cpath

Specifies the absolute path to the `x509` certificate file to use for TLS. 
The certificate must be in PEM format. The file may only be written by the 
owner of the file.

#### Syntax
```bash
cpath=PATH
```
where:
* `PATH` specifies the absolute path to the `x509` certificate file to use 

for TLS.

#### Description
The `cpath` parameter specifies the location of the certificate file. The 
certificate must be in PEM format, and the file can only be written by the 
owner of the file.

### kpath

Specifies the absolute path to the certificate’s `x509` private key file 
to use for TLS. The key must be in PEM format. The file may only be read 
and written by the owner of the file. If `kpath` is not specified then the 
certificate file must contain the key.

#### Syntax
```bash
kpath=PATH
```
where:
* `PATH` specifies the absolute path to the certificate’s `x509` private 
key file to use for TLS.

#### Description
The `kpath` parameter specifies the location of the private key file. The 
key must be in PEM format, and the file can only be read and written by 
the owner of the file. If the `kpath` is not specified, the certificate 
file must contain the private key.

## Function

Configure transport layer security (TLS).

### Usage

```bash
xrd.tls [options] cpath [kpath]
```
where:

* `[options]` specifies additional options, such as `detail`, `hsto`, and 
`nodetail`.
* `cpath` specifies the absolute path to the `x509` certificate file to 
use for TLS.
* `kpath` specifies the absolute path to the certificate’s `x509` private 
key file to use for TLS.

### Examples

#### Example 1: Using cpath

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```
specifies the absolute path to the `x509` certificate file to use for TLS, 
and leaves the private key at its default location.

#### Example 2: Using kpath

```bash
xrd.tls /etc/security/xrootd/hostcert.pem 
kpath=/etc/security/xrootd/hostkey.pem
```
specifies both the absolute path to the `x509` certificate file to use for 
TLS and the absolute path to the certificate’s `x509` private key file to 
use for TLS.

#### Example 3: Using cpath only

```bash
xrd.tls cpath=/etc/security/xrootd/hostcert.pem kpath=
```
specifies only the absolute path to the `x509` certificate file to use for 
TLS, and leaves the private key at its default location.