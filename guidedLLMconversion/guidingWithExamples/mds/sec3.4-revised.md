## 3.4        tls (*required for TLS*)

**xrd.tls** *cpath* [ *kpath* ] [ *options* ]


*options:*  [[**no**]**detail**] [**hsto** to{**h**|**m**|**s**]



### Function
Configure transport layer security (**TLS**).



### Parameters

*cpath*  
Specifies the absolute path to the **x509** certificate file to use for **TLS**. The certificate  must be in **PEM** format. The file may only be written by the owner of the file.

*kpath*  
Specifies the absolute path to the certificate’s **x509** private key file to use for **TLS**. The key must be in **PEM** format. The file may only be read and written by the owner of the file. If *kpath* is not specified then the certificate file must contain the key.

[**no**]**detail**  
When **detail** is specified, detailed **TLS** trace back messages are printed along with explanatory messages. The **nodetail** option suppresses the **TLS** trace back messages. The default is **nodetail**. See the notes for why this is so.

*to*  
Specifies the maximum amount of time a **TLS** handshake is allowed to take before the connection is closed. The *to* value may be suffixed by **h** (hours), **m** (minutes), or **s** (seconds); otherwise, *to* defaults to seconds. There is no default time limit for the **TLS** handshake.



### Defaults
**TLS** is not configured and cannot be used. See individual options for the defaults should you configure **TLS**.



### Notes
1. Normally, a host certificate should be used because the client can use it to validate that it connected to the intended host.  
2. If you specify the **tls** directive then you must specify the **tlsca** directive as well.  
3. Most **TLS** trace back messages do not provide any more information than the companion explanatory messages and, as such, are only useful for debugging purposes. This is why **nodetail** is the default. However, if you enable **TLS** tracing using the **xrd.trace** directive, **detail** is enabled regardless of what is specified.



### Example
**xrd.tls /etc/security/xrootd/hostcert.pem**
