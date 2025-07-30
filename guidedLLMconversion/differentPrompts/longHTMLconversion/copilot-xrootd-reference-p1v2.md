# XRootD Configuration Reference

**Release Date:** 15-August-2023  
**Version:** 5.6.1 and above  
**Author:** Andrew Hanushevsky  
**License:** GNU Lesser General Public License (LGPL)  
**Produced under contract DE-AC02-76-SFO0515 with the Department of Energy**  
**© 2004–2023 by the Board of Trustees of the Leland Stanford, Jr., University**

---

## Table of Contents

1. [Introduction](#1-introduction)  
   - [1.1 Security Considerations](#11-security-considerations)  
   - [1.2 Starting the xrootd Daemon](#12-starting-the-xrootd-daemon)  
     - [1.2.1 Multiple Instances and Automatic Fencing](#121-multiple-instances-and-automatic-fencing)  
     - [1.2.2 Passing Plug-In Command Line Arguments](#122-passing-plug-in-command-line-arguments)  
     - [1.2.3 Log File Plug-Ins](#123-log-file-plug-ins)  
     - [1.2.4 Files Created by xrootd](#124-files-created-by-xrootd)  
     - [1.2.5 Exported Environment Variables](#125-exported-environment-variables)  
2. [Framework Directives by Category](#2-framework-directives-by-category)  
3. [Common Framework Configuration Directives](#3-common-framework-configuration-directives)  
4. [Esoteric Framework Configuration Directives](#4-esoteric-framework-configuration-directives)  
5. [xrootd Directives by Category](#5-xrootd-directives-by-category)  
6. [Common xrootd Configuration Directives](#6-common-xrootd-configuration-directives)  
7. [Esoteric xrootd Configuration Directives](#7-esoteric-xrootd-configuration-directives)  
8. [Enabling HTTP Access](#8-enabling-http-access)  
9. [Document Change History](#9-document-change-history)

## 1. Introduction

This document describes the **eXtended Request Daemon (xrd)** configuration directives and protocols that can be used with `xrd`: `cmsd`, `HTTP`, and `xrootd`. It also includes the directives for the `xrootd` daemon that can run `xroot` and `HTTP` protocols. The `cmsd`-specific directives are described in a separate reference manual.

The `xrd` is a framework that can dynamically support multiple TCP/IP application service layer protocols. It is designed to provide a high-performance environment for application services.

### Supported Executables

- `cmsd`: Daemon for the CMS server clustering protocol  
- `xrootd`: Daemon for xroot and related protocols

### Configuration File Structure

Directives are prefixed by the component acronym they apply to:

| Component | Purpose |
|-----------|---------|
| `acc`     | Access control (authorization) |
| `cms`     | Cluster Management Services |
| `frm`     | File Residency Manager |
| `ofs`     | Open File System |
| `oss`     | Open Storage System |
| `pfc`     | Proxy File Cache |
| `pss`     | Proxy Storage Service |
| `sec`     | Security authentication |
| `xrd`     | Extended Request Daemon |
| `xrootd`  | The xroot protocol implementation |
| `http`    | The HTTP protocol implementation |
| `all`     | Applies to all components above |

Lines not starting with a recognized identifier (including blank lines and comments starting with `#`) are ignored.

The location of the configuration file is specified on the `xrootd` command line. Refer to the reference manuals for other components on how they locate their respective configuration files.

---

## 1.1 Security Considerations

- The `xrd` framework relies on the loaded protocol(s) for strong authentication (e.g., Kerberos, GSI).
- Host-based authentication is available via the `allow` directive.
- Do **not** run `xrootd` as super-user unless explicitly intended. Use the `-R` option to indicate this.
- Running as root without `-R` will cause the program to exit.

---

## 1.2 Starting the xrootd Daemon

```bash
xrootd [options] [path [path ...]] [piargs]
```

### Options

| Option | Description |
|--------|-------------|
| `-c fn` | Configuration file name |
| `-l fn` | Log file or plugin |
| `-k` | Log rotation control |
| `-n name` | Instance name |
| `-R user` | Run as specified user |
| `-s pfn` | PID file name |
| `-S site` | Site name for monitoring |
| `-w hpath` | Working directory |
| `-d` | Enable debugging |
| `-b` | Run in background |
| `-L protlib` | Shared library for protocol |
| `-p port` | TCP port or service name |
| `-P protocol` | Default protocol name |

### Example

```bash
xrootd -c /opt/xrootd/xrootd.cf
```

---

## 1.2.1 Multiple Instances and Automatic Fencing

You can run multiple instances of `xrootd` on the same physical machine. This is useful when overlaying more than one cluster on top of a file system (e.g., production and test).

### Automatic Fencing Includes:

- Unique admin paths per instance (e.g., `/tmp/test/.xrootd/admin`)
- Unique working directories (e.g., `/home/xrootd/test`)
- Unique log file paths (e.g., `/var/adm/xrootd/test/xrd.log`)

To disable fencing of log files, prefix the log file path with `=`.

---

## 1.2.2 Passing Plug-In Command Line Arguments

Use the `-+` option to pass arguments to plug-ins:

```bash
xrootd [options] [paths] -+mypi arg1 arg2 -+urpi arg3
```

This sets:

- `mypi.argv**` and `mypi.argc`
- `urpi.argv**` and `urpi.argc`

Avoid using tags starting with `xrd` as they are reserved.

---

## 1.2.3 Log File Plug-Ins

Use `@lib` with `-l` to specify a log file plug-in. You can also use:

- `bsz=sz`: Speed matching buffer size
- `cse=0|1|2`: Standard error capture mode
- `logfn=fn`: Additional log file

Avoid infinite loops by not routing plug-in logs to standard error.

---

## 1.2.4 Files Created by xrootd

| File/Directory | Controlled By | Purpose |
|----------------|---------------|---------|
| `<stderr>` | `-l`, `-n` | Logs and errors |
| `/tmp/[name]/.xrootd/` | `-n`, `adminpath` | Server files |
| `<cwd>/<name>/core[.pid]` | `-n` | Core dumps |
| `/tmp/[name]/exec.pid` | `pidpath`, `-n` | PID file |
| `/tmp/exec.name.env` | `adminpath`, `-n` | Environment info |

---

## 1.2.5 Exported Environment Variables

| Variable | Description |
|----------|-------------|
| `XRDADMINPATH` | Admin file directory |
| `XRDCONFIGFN` | Config file path |
| `XRDDEBUG` | Debug mode flag |
| `XRDHOST` | Host DNS name |
| `XRDINSTANCE` | `execname instance@hostname` |
| `XRDLOGDIR` | Log directory |
| `XRDNAME` | Instance name |
| `XRDPROG` | Executable name |
| `XRDSITE` | Site name |

Additional variables are exported depending on the plug-ins used (e.g., CMS, OFS, OSS, XROOTD).

## 2. Framework Directives by Category

This section provides a guide to `xrd` directives by category that is helpful when you need to address a specific requirement.

### 2.1 Debugging

- `xrd.trace` — Specify which framework activities are to be traced.

### 2.2 Monitoring

- `xrd.report` — Specify which execution summary statistics are to be gathered and where they are to be sent.
- `all.sitename` — Specify the name of the site to be used for monitoring purposes.
- `xrd.tcpmonlib` — Specify the plug-in to be used to collect and report specialized TCP connection statistics.

### 2.3 Networking

- `xrd.network` — Specify network parameters such as DNS usage, interfaces, keep-alive characteristics, and routing.

### 2.4 Operational Environment

- `all.adminpath` — Specifies the location of runtime files used for administrative purposes.
- `xrd.homepath` — Specifies the location of the working directory during execution.
- `all.pidpath` — Specifies where the file containing the server’s process ID should be created.

### 2.5 Protocol Support

- `xrd.port` — Specifies the default port number for incoming requests.
- `xrd.protocol` — Load additional protocols such as HTTP.

### 2.6 Security and TLS

- `xrd.allow` — Restricts hosts that can connect to the server.
- `xrd.tls` — Specify the location of the server’s host certificate.
- `xrd.tlsca` — Specify the location of CA certificates and CRLs.
- `xrd.tlsciphers` — Specify allowable TLS ciphers.

### 2.7 Tuning

- `xrd.buffers` — Limit the amount of memory used for data buffers.
- `xrd.maxfd` — Limit the number of file descriptors.
- `xrd.sched` — Specify execution parameters such as core file creation, default stack size, and threading.
- `xrd.timeout` — Specify various connection handling timeout parameters.

---

## 3. Common Framework Configuration Directives

### 3.1 adminpath

```ini
all.adminpath path [group]
```

#### Function

Specify the location of protocol-specific files for administrative purposes.

#### Parameters

- `path`: Absolute path to a directory that holds protocol-specific files.
- `group`: Allows read/write group access to any named sockets created in the path.

#### Default

`/tmp`

#### Notes

1. The `adminpath` directive sets the location for local TCP sockets and protocol-specific directories.
2. Use `-a` or `-A` command-line options to set defaults.
3. If `-n` is specified, a subdirectory for the instance is created.
4. Avoid using `/tmp` if the system deletes idle files automatically.
5. Socket names are limited to 108 characters.
6. The `.xrd` subdirectory is created in `path`, and:
   - `cmsd` creates `.olb`
   - `xrootd` creates `.xrootd`
7. Mode bits are set to `0700` or `0770` if `group` is specified.
8. The `cmsd` can override this with `cms.adminpath`.

#### Example

```ini
all.adminpath /var/adm/xrd group
```

---

### 3.1.1 Administrative Interface

The `adminpath` directive is used to construct the path where local TCP sockets (named sockets) are created. These sockets are used to communicate requests and receive responses via the administrative interface.

#### Steps to Use the Interface

1. Wait for the server to create the socket file (e.g., `/tmp/.xrootd/admin`).
2. Create a stream socket using:
   ```c
   socket(PF_UNIX, SOCK_STREAM, 0)
   ```
3. Fill out the `sockaddr_un` structure with the socket path.
4. Use `connect()` to connect to the socket.
5. Use `write()` and `read()` to communicate.

---

### 3.2 allow

```ini
xrd.allow {host | netgroup} name
```

#### Function

Restrict the hosts that can connect to `xrootd`.

#### Parameters

- `host name`: DNS hostname or IP address allowed to connect. Wildcards (`*`) are allowed.
- `netgroup name`: NIS netgroup allowed to connect.

#### Default

None — if not specified, any host can connect.

#### Notes

1. Multiple `host` and `netgroup` entries can be specified.
2. Hostname-based security depends on DNS integrity and IP spoofing resistance.

#### Example

```ini
xrd.allow host objyana*.slac.stanford.edu
```

---

### 3.3 homepath

```ini
xrd.homepath path [group]
```

#### Function

Specify the location of the current working directory.

#### Parameters

- `path`: Absolute path to be used as the working directory.
- `group`: Allows group read access to the path.

#### Default

The directory at server start-up.

#### Notes

1. Use `-w` or `-W` command-line options to set this.
2. If `-n` is specified, a subdirectory for the instance is created.
3. Ensure the path is suitable for containerized environments.

#### Example

```ini
all.homepath /var/run/xrd group
```

---

### 3.4 tls (required for TLS)

```ini
xrd.tls cpath [kpath] [options]
```

#### Function

Configure transport layer security (TLS).

#### Parameters

- `cpath`: Path to the x509 certificate file (PEM format).
- `kpath`: Path to the private key file (PEM format). Optional if included in `cpath`.
- `detail` / `nodetail`: Enable or suppress detailed TLS tracebacks.
- `to`: TLS handshake timeout (e.g., `30s`, `2m`, `1h`).

#### Default

TLS is not configured unless this directive is specified.

#### Notes

1. A host certificate is recommended.
2. If `tls` is specified, `tlsca` must also be specified.
3. Use `xrd.trace` to enable TLS tracing regardless of `nodetail`.

#### Example

```ini
xrd.tls /etc/security/xrootd/hostcert.pem
```

---

### 3.5 tlsca (required for TLS)

```ini
xrd.tlsca noverify | {certdir | certfile} path [options]
```

#### Function

Configure client certificate verification for TLS.

#### Parameters

- `noverify`: Disable client certificate verification.
- `certdir path`: Directory of trusted CA certificates.
- `certfile path`: File of trusted CA certificates.
- `crlcheck`: CRL handling (`all`, `external`, `last`)
- `log`: Logging (`failure`, `off`)
- `proxies` / `noproxies`: Enable or disable proxy support.
- `refresh rint`: Refresh interval (e.g., `8h`, `30m`)
- `verdepth vdn`: Verification depth (1–256)

#### Default

```ini
xrd.tlsca crlcheck external log failure proxies refresh 8h verdepth 9
```

#### Notes

1. You can specify both `certdir` and `certfile`.
2. Verification is essential unless strong authentication is used.
3. Use `c_rehash` when updating `certdir`.

#### Example

```ini
xrd.tlsca certfile /etc/security/xrootd/cacerts.pem
```

## 4. Esoteric Framework Configuration Directives

---

### 4.1 buffers

```ini
xrd.buffers memsz[k | m | g] [rint[m | s | h]]
```

#### Function

Limits the amount of memory to be used for data buffers.

#### Parameters

- `memsz`: Maximum number of bytes to be used for data buffers.
- `rint`: Interval between buffer pool readjustments.

#### Default

```ini
xrd.buffers memsz 20m
```

#### Notes

- Memory for buffers is independent of other memory allocations.
- The `rint` interval controls how frequently buffer sizes are adjusted.

#### Example

```ini
xrd.buffers 512M
```

---

### 4.2 maxfd

```ini
xrd.maxfd [strict] maxfd[k]
```

#### Function

Limits the number of file descriptors.

#### Parameters

- `strict`: Enforces the limit in all cases.
- `maxfd`: Maximum number of file descriptors (1024–1024k).

#### Default

```ini
xrd.maxfd 256k
```

#### Notes

- With `strict`, the actual limit is `min(hard_limit, maxfd)`.
- Without `strict`, `maxfd` is used only if the hard limit is unlimited.

#### Example

```ini
xrd.maxfd strict 64k
```

---

### 4.3 network

```ini
xrd.network [buffsz blen[k | m | g]] [cache sec]
[[no]dnr] [[no]dyndns]
[kaparms idle[,itvl[,cnt]]] [[no]keepalive]
[routes {split|common|local} [use if1[,if2]]]
[[no]rpipa] [tls]
```

#### Function

Specifies network parameters.

#### Parameters

- `buffsz blen`: Socket buffer size.
- `cache sec`: DNS cache timeout.
- `dnr` / `nodnr`: Enable/disable DNS resolution.
- `dyndns` / `nodyndns`: Enable/disable dynamic DNS.
- `kaparms`: TCP keepalive parameters.
- `keepalive` / `nokeepalive`: Enable/disable OS keepalive.
- `routes`: Dual network routing mode.
- `rpipa` / `norpipa`: Resolve private IPs to hostnames.
- `tls`: Apply settings to TLS port.

#### Default

```ini
xrd.network cache 3h dnr norpipa
```

#### Notes

- Use `buffsz 0` to enable TCP auto-tuning.
- `kaparms` is Linux-specific.
- Avoid using both `keepalive` and `timeout` simultaneously.
- `dyndns` disables caching unless `cache` is explicitly set.

#### Example

```ini
xrd.network nokeepalive nodnr
xrd.network tls buffsz 512k
```

---

### 4.4 pidpath

```ini
all.pidpath path
```

#### Function

Specifies where the PID file is written.

#### Parameters

- `path`: Directory for the PID file.

#### Default

`/tmp`

#### Notes

- If `-n` is used, a subdirectory is created for the instance.
- `-s` can override the filename.

#### Example

```ini
all.pidpath /var/run/scalla
```

---

### 4.5 port

```ini
xrd.port [tls] {pnum | any} [if conds]
```

#### Function

Designates the port number for incoming requests.

#### Parameters

- `tls`: TLS-only port.
- `pnum`: TCP port number or service name.
- `any`: Use any available port.
- `if conds`: Conditional application.

#### Notes

- Default port is determined by:
  - Protocol directive
  - `-p` command line
  - Executable name
  - Fallback to 1094
- TLS-only ports are not supported by all protocols.

#### Example

```ini
xrd.port xrdnew
```

---

### 4.6 protocol

```ini
xrd.protocol [tls] name[:port] {+port | {lib | *} [parms]}
```

#### Function

Configures a protocol for incoming requests.

#### Parameters

- `tls`: TLS-only port.
- `name`: Protocol name.
- `port`: Port number or service name.
- `+port`: Add additional port.
- `lib`: Shared library path.
- `parms`: Load-time parameters.

#### Notes

- Built-in protocol is based on executable name.
- Up to 8 protocols and 8 ports per protocol.
- TLS-only ports not supported by `xroot`.

#### Example

```ini
xrd.protocol http:8000 libXrdHttp.so
xrd.protocol http:8080 +port
```

---

### 4.7 report

```ini
xrd.report dest1[,dest2] [every rsec] [-]option
```

#### Function

Specifies execution tracing options.

#### Parameters

- `dest1`: Primary destination (host:port or local socket).
- `dest2`: Secondary destination.
- `every rsec`: Reporting interval.
- `option`: Reporting level (e.g., `all`, `buff`, `link`, `sched`).

#### Notes

- Reports are sent as single UDP messages in XML format.
- Use `sync` for accurate data, `syncwp` for best-effort accuracy.

#### Example

```ini
xrd.report myhost:1234 every 15m all -poll
```

---

### 4.8 sched

```ini
xrd.sched parms
```

#### Parameters

- `avlt`: Always-available threads.
- `core`: Core dump policy (`asis`, `max`, `off`).
- `idle`: Idle thread check interval.
- `maxt`: Max threads.
- `mint`: Min threads.
- `stksz`: Thread stack size.

#### Default

```ini
xrd.sched mint 8 maxt 2048 avlt 512 idle 780
```

#### Notes

- Avoid changing unless necessary.
- Stack size is OS-dependent.

#### Example

```ini
xrd.sched mint 10 maxt 100 avlt 20
```

---

### 4.9 sitename

```ini
all.sitename sname
```

#### Function

Specifies the site name for monitoring.

#### Parameters

- `sname`: 1–63 character name (letters, digits, `_-:.`)

#### Notes

- `-S` command line overrides this.
- First directive takes precedence.

#### Example

```ini
all.sitename slac
```

---

### 4.10 tcpmonlib

```ini
xrd.tcpmonlib [++] path [parms]
```

#### Function

Specifies the TCP connection monitoring plug-in.

#### Parameters

- `++`: Stack on top of existing plug-in.
- `path`: Shared library path.
- `parms`: Optional parameters.

#### Notes

- Plug-in interface defined in `XrdTcpMonPin.hh`.
- Must enable `tcpmon` in `xrootd.monitor`.

#### Example

```ini
xrd.tcpmonlib /opt/xrootd/lib/libTcpMon.so
```

---

### 4.11 timeout

```ini
xrd.timeout [hail hlto] [idle idto] [kill klto] [read rdto]
```

#### Function

Specifies timeout parameters.

#### Parameters

- `hail`: Timeout for initial data after connection.
- `idle`: Idle connection timeout.
- `kill`: Timeout for session termination.
- `read`: Read timeout.

#### Default

```ini
xrd.timeout hail 30 idle 0 kill 3 read 5
```

#### Notes

- Idle timeout prevents dead connections.
- Avoid short idle timeouts (<2 min).

#### Example

```ini
xrd.timeout idle 120m read 10
```

---

### 4.12 tlsciphers

```ini
xrd.tlsciphers ciphers
```

#### Function

Specifies allowed TLS ciphers.

#### Parameters

- `ciphers`: Colon-separated list of ciphers.

#### Default

Mozilla-recommended ciphers (OpenSSL > 1.0.2)

#### Example

```ini
xrd.tlsciphers ALL:!LOW:!EXP:!MD5:!MD2
```

---

### 4.13 trace

```ini
xrd.trace [-]option
```

#### Function

Specifies execution tracing options.

#### Parameters

- `option`: Trace level (`all`, `conn`, `debug`, `mem`, `net`, `poll`, `protocol`, `sched`, `tls`, `tlsctx`, `tlsio`, `tlssok`, `none`, `off`)

#### Notes

- All tracing is enabled with `-d`.
- `none` or `off` disables all tracing.

#### Example

```ini
xrd.trace all -debug
```


## 5. xrootd Directives by Category

This section categorizes the `xrootd`-specific configuration directives.

---

### 5.1 Data Access

- `all.export` — Specify the file system paths that may be accessed.
- `xrootd.fslib` — Specify the file system plug-in to be used for data access.
- `xrootd.redirect` — Specify client redirection by type of request, access path, and possible errors during access.

---

### 5.2 Data Integrity

- `xrootd.chksum` — Enable file checksum calculation.

---

### 5.3 Debugging

- `xrootd.diglib` — Enable interactive remote debugging.
- `xrootd.trace` — Specify execution tracing options.

---

### 5.4 Monitoring

- `xrootd.mongstream` — Specify custom g-stream parameters.
- `xrootd.monitor` — Specify which statistics are to be collected and where they are to be sent.
- `xrootd.pmark` — Specify packet marking firefly parameters.

---

### 5.5 Prepare Processing

- `xrootd.prep` — Specify how prepare requests tracking should be handled.

---

### 5.6 Security

- `xrootd.seclib` — Specify the location of the security interface layer.
- `xrootd.log` — Specify which events are to be logged.
- `xrootd.tls` — Specify TLS requirements by request category.

---

### 5.7 Tuning

- `xrootd.async` — Specify asynchronous data processing features and limits.
- `xrootd.bindif` — Specify alternate interfaces that should be used for data.
- `xrootd.fsoverload` — Specify how file system overloads are to be handled.
- `xrootd.tlsreuse` — Specify TLS session cache characteristics.

## 6. Common xrootd Configuration Directives

---

### 6.1 export

```ini
all.export {path | *[?]} [[no]lock] [oss_options]
```

#### Function

Specify a valid path prefix for file requests.

#### Parameters

- `path`: An absolute path prefix for valid file requests.
- `*`: Allow arbitrary object identifiers (names not starting with `/`).
- `*?`: Same as `*`, but inspects for CGI information.
- `lock`: Use standard xroot protection against multiple writers (default).
- `nolock`: Disable write protection.
- `oss_options`: Optional OSS options for storage system and cluster service.

#### Default

```ini
xrootd.export /tmp lock
```

#### Notes

1. Only files in `/tmp` are accessible unless overridden.
2. Do not prefix `path` with the `oss.localroot` directive.
3. `nolock` disables default write protection.
4. `[no]lock` must appear before any `oss_options`.
5. Object identifiers require compatible plug-ins.
6. Used for object store plug-ins like Ceph.

#### Example

```ini
xrootd.export /store
```

---

### 6.2 seclib

```ini
xrootd.seclib {default | path}
```

#### Function

Specify the location of the security interface layer.

#### Parameters

- `default`: Use the default security plug-in.
- `path`: Absolute path to the shared library implementing the `sec` interface.

#### Default

Strong authentication is disabled unless `seclib` is specified.

#### Notes

1. The `sec` interface allows custom authentication (e.g., Kerberos, GSI).
2. Requires compatible libraries on both server and client.
3. Refer to `XrdSecEntity.hh` and `XrdSecInterface.hh` for implementation.
4. The `ofs` implementation can use authentication for access control.
5. The default `sfs` implementation does not enforce access control.

#### Example

```ini
xrootd.seclib /opt/xrootd/lib/libosec.so
```

## 7. Esoteric xrootd Configuration Directives

---

### 7.1 async

```ini
xrootd.async [force] [limit aiorpc] [maxsegs smax]
[maxstalls mstall] [maxtot slim]
[minsize reqsz[k|m|g]] [minsfsz sfsz[k|m|g]]
[nocache] [nosf] [off] [segsize segsz[k|m|g]]
[syncw] [timeout tmo]
```

#### Function

Configure asynchronous I/O behavior.

#### Default

```ini
xrootd.async limit 8 maxsegs 8 maxstalls 4 maxtot 4096
minsize 98304 minsfsz 8k segsize 64k timeout 45
```

#### Notes

- Enables overlapping I/O for performance.
- `nocache`: disables async I/O for caching servers.
- `nosf`: disables `sendfile()` usage.
- `off`: disables async I/O entirely.

#### Example

```ini
xrootd.async minsize 1M
```

---

### 7.2 bindif

```ini
xrootd.bindif target
```

#### Function

Specify endpoints for additional data paths.

#### Parameters

- `target`: `host[:port][%host[:port]]`

#### Notes

- Used for dual-homed systems.
- `%` separates public/private endpoints.

#### Example

```ini
xrootd.bindif foo.proxy.edu:1094
```

---

### 7.3 chksum

```ini
xrootd.chksum [chkcgi] [max num] digest [path [args]]
```

#### Function

Configure checksum calculation.

#### Parameters

- `digest`: e.g., `md5`, `crc32c`, `adler32`
- `path`: external checksum program
- `max`: max concurrent checksum jobs

#### Notes

- Native digests: `adler32`, `crc32`, `crc32c`, `md5`
- External programs must return checksum on stdout.

#### Example

```ini
xrootd.chksum max 2 crc32c
```

---

### 7.4 diglib

```ini
xrootd.diglib * authpath
```

#### Function

Enable remote debugging via digFS.

#### Parameters

- `authpath`: path to authorization file

#### Notes

- digFS provides a virtual read-only file system.
- Authorization file controls access.

#### Example

```ini
xrootd.diglib * /etc/xrootd/digauth.cf
```

---

### 7.4.1 Authorizing digFS Access

Authorization file format:

```text
info allow aprot ident
```

- `info`: `all`, `conf`, `core`, `logs`, `proc`
- `aprot`: `gsi`, `krb5`, `pwd`, `unix`, etc.
- `ident`: `g=group`, `h=host`, `n=name`, etc.

#### Example

```text
all -core allow krb5 h=test.org n=xtestor
conf logs allow gsi g=atlas n=theuser
```

---

### 7.4.2 Optional digFS Directives

#### addconf

```ini
dig.addconf path [fname]
```

Adds a config file to digFS.

#### log

```ini
dig.log [deny] [grant] [none]
```

Controls digFS access logging.

#### Example

```ini
dig.log deny
```

---

### 7.5 fslib

```ini
xrootd.fslib [++] [throttle | path]
```

#### Function

Specify file system plug-in.

#### Parameters

- `++`: stack plug-in
- `throttle`: wrap with libXrdThrottle.so
- `path`: shared library path

#### Default

```ini
xrootd.fslib default
```

#### Example

```ini
xrootd.fslib /opt/xrootd/lib/libofs.so
```

---

### 7.6 fsoverload

```ini
xrootd.fsoverload [[no]bypass] [redirect target] [stall sec]
```

#### Function

Handle file system overloads.

#### Parameters

- `bypass`: allow client-specified forwarding
- `redirect`: host:port[%host:port]
- `stall`: delay before retry

#### Default

```ini
xrootd.fsoverload nobypass stall 33
```

#### Example

```ini
xrootd.fsoverload bypass redirect foo.proxy.edu:1094
```

---

### 7.7 log

```ini
xrootd.log [-]levent [ [-]levent ... ]
```

#### Function

Control event logging.

#### Events

- `all` (default)
- `disc`: disconnects
- `login`: logins

#### Example

```ini
xrootd.log all -login
```

---

### 7.8 mongstream

```ini
xrootd.mongstream events use parms
```

#### Function

Configure g-stream monitoring.

#### Events

- `ccm`, `pfc`, `tcpmon`, `tpc`, `all`

#### Parameters

- `flush intvl`
- `maxlen size`
- `send fmt host:port`

#### Example

```ini
xrootd.mongstream all use send json datacoll:1234
```

---

### 7.9 monitor

```ini
xrootd.monitor [...] [options] [dest dest [dest dest]]
```

#### Function

Configure monitoring.

#### Options

- `all`, `auth`, `flush`, `fstat`, `ident`, `fbuff`, `gbuff`, `mbuff`, `rbuff`, `rnums`, `window`

#### Events

- `files`, `fstat`, `io`, `iov`, `info`, `redir`, `tcpmon`, `tpc`, `user`

#### Example

```ini
xrootd.monitor all fstat 5m dest fstat datacoll:5050
```

---

### 7.10 pmark

```ini
xrootd.pmark parms
```

#### Function

Configure packet marking (firefly).

#### Parameters

- `defsfile`, `domain`, `ffdest`, `map2act`, `map2exp`, `use`, `trace`

#### Example

```ini
xrootd.pmark defsfile curl https://api.scitags.org/api.json
xrootd.pmark ffdest firefly.esnet.net:1234
xrootd.pmark map2exp path /data/atlas atlas
xrootd.pmark map2act atlas role prod production
```

---

### 7.11 prep

```ini
xrootd.prep [keep ksec] [scrub time] [logdir ldir]
```

#### Function

Track prepare requests.

#### Default

Disabled unless `logdir` is specified.

#### Example

```ini
xrootd.prep keep 12H logdir /nfs/xrootd/preplog
```

---

### 7.12 redirect

```ini
xrootd.redirect target {client domlist | byfunc}
```

#### Function

Configure request redirection.

#### Parameters

- `target`: host:port[%host:port]
- `domlist`: `local`, `private`, `.domain`
- `byfunc`: `foper`, `path`, `? path`

#### Example

```ini
xrootd.redirect all -prepare
```

---

### 7.13 tls

```ini
xrootd.tls [capable] req
```

#### Function

Specify TLS requirements.

#### Requests

- `all`, `data`, `login`, `session`, `tpc`, `none`, `off`

#### Notes

- `capable`: apply only to TLS-capable clients

#### Example

```ini
xrootd.tls tpc
xrootd.tls capable session
```

---

### 7.14 trace

```ini
xrootd.trace [-]option [ [-]option ... ]
```

#### Function

Enable tracing.

#### Options

- `all`, `auth`, `debug`, `emsg`, `fs`, `fsaio`, `fsio`, `login`, `mem`, `off`, `pgcserr`, `redirect`, `request`, `response`, `stall`

#### Example

```ini
xrootd.trace all -debug
```

## 8. Enabling HTTP Access

XRootD supports HTTP access via a protocol plug-in. The HTTP protocol can run alongside the standard XRootD protocol without interference.

### Configuration

```ini
if exec xrootd
xrd.protocol http[:port] path/libXrdHttp.so [cfgfile]
fi
```

#### Parameters

- `port`: Port number for HTTP (default is 1094).
- `path`: Path to `libXrdHttp.so`.
- `cfgfile`: Optional external configuration file for HTTP.

#### Notes

1. Use `if-fi` to avoid issues when using a shared config file with `cmsd`.
2. HTTP access is subject to all `xrd.` and `xrootd.` restrictions.
3. HTTP requests are monitored like XRootD requests.
4. Consider using port 8080 for HTTP clarity.
5. All servers in a cluster must have HTTP enabled.
6. WebDAV is supported.
7. Not all HTTP clients support all features.

---

## 8.1 Enabling HTTPS

When HTTPS is configured:

- Clients are authenticated via certificates.
- All traffic is encrypted, increasing CPU and latency.
- HTTPS-to-HTTP conversion is supported for performance.

### HTTPS-to-HTTP Conversion

- Client connects via HTTPS.
- Server extracts credentials and issues a secure token.
- Client reconnects via HTTP using the token.

### Cluster Scenarios

| Redirector Accepts | Server Accepts | Configuration | Notes |
|--------------------|----------------|---------------|-------|
| HTTP               | HTTP           | Default       | No security |
| HTTPS              | HTTP + token   | `xrd.tls`, `xrd.tlsca`, `http.secretkey` | Central auth, fast data |
| HTTP               | HTTPS          | `xrd.tls`, `xrd.tlsca`, `http.desthttps` | Distributed auth, encrypted data |
| HTTP               | HTTPS → HTTP   | `xrd.tls`, `xrd.tlsca`, `http.selfhttps2http`, `http.secretkey` | Fastest |
| HTTPS              | HTTPS          | `xrd.tls`, `xrd.tlsca` | Fully secure, high overhead |

---

## 8.1.1 Backward Compatibility and Overrides

Use the `http.httpsmode` directive to control compatibility and override warnings.

---

## 8.2 Directives to Enhance HTTPS Access

These directives improve HTTPS handling.

---

### 8.2.1 desthttps

```ini
http.desthttps {no | yes}
```

#### Function

Redirect clients using HTTPS.

#### Default

```ini
http.desthttps no
```

#### Example

```ini
http.desthttps yes
```

---

### 8.2.2 gridmap

```ini
http.gridmap [required] [compatNameGeneration] path
```

#### Function

Map x509 DNs to usernames.

#### Parameters

- `required`: Treat errors as fatal.
- `compatNameGeneration`: Use GSI-style names.
- `path`: Path to grid map file.

#### Example

```ini
http.gridmap /etc/grid-security/mapfile
```

---

### 8.2.3 httpsmode

```ini
http.httpsmode {auto | disable | manual}
```

#### Function

Control HTTPS enablement.

#### Default

```ini
http.httpsmode auto
```

#### Example

```ini
http.httpsmode manual
```

---

### 8.2.4 secretkey

```ini
http.secretkey {path | token}
```

#### Function

Set encryption key for HTTPS-to-HTTP tokens.

#### Notes

- All nodes in a cluster must use the same key.

#### Example

```ini
http.secretkey /admin/thekey
```

---

### 8.2.5 selfhttps2http

```ini
http.selfhttps2http {no | yes}
```

#### Function

Redirect HTTPS to HTTP on the same server.

#### Default

```ini
http.selfhttps2http no
```

#### Example

```ini
http.selfhttps2http yes
```

---

### 8.2.6 secxtractor

```ini
http.secxtractor path [parms]
```

#### Function

Load a plug-in to extract extended certificate info.

#### Notes

- Useful for extracting VO info (e.g., VOMS).

#### Example

```ini
http.secxtractor /usr/lib64/libXrdSecgsiVOMS.so
```

---

### 8.2.7 tlsreuse

```ini
http.tlsreuse {off | on}
```

#### Function

Enable TLS session reuse.

#### Default

```ini
http.tlsreuse off
```

---

## 8.2.8 Deprecated HTTPS Directives

These are replaced by `xrd.tls` and `xrd.tlsca`.

---

### 8.2.8.1 cadir

```ini
http.cadir path
```

#### Example

```ini
http.cadir /etc/grid-security/certificates
```

---

### 8.2.8.2 cafile

```ini
http.cafile path
```

#### Example

```ini
http.cafile /etc/myCA.pem
```

---

### 8.2.8.3 cert

```ini
http.cert path
```

#### Example

```ini
http.cert /etc/grid-security/hostcert.pem
```

---

### 8.2.8.4 cipherfilter

```ini
http.cipherfilter ciphers
```

#### Example

```ini
http.cipherfilter ALL:!LOW:!EXP:!MD5:!MD2
```

---

### 8.2.8.5 key

```ini
http.key path
```

#### Example

```ini
http.key /etc/grid-security/hostkey.pem
```

---

## 8.3 Common Directives

---

### 8.3.1 embeddedstatic

```ini
http.embeddedstatic {no | yes}
```

#### Default

```ini
http.embeddedstatic yes
```

#### Example

```ini
http.embeddedstatic yes
```

---

### 8.3.2 exthandler

```ini
http.exthandler name path [token]
```

#### Example

```ini
http.exthandler mhandler17 /opt/http/lib/libExtHndlr.so
```

---

### 8.3.3 header2cgi

```ini
http.header2cgi hdrkey cgikey
```

#### Example

```ini
http.header2cgi auth authz
```

---

### 8.3.4 listingdeny

```ini
http.listingdeny {no | yes}
```

#### Example

```ini
http.listingdeny yes
```

---

### 8.3.5 listingredir

```ini
http.listingredir desturl
```

#### Example

```ini
http.listingredir http://hostwhichprovideslistings:80/
```

---

### 8.3.6 staticpreload

```ini
http.staticpreload url path
```

#### Example

```ini
http.staticpreload http://static/mycss.css /etc/mycss
```

---

### 8.3.7 staticredir

```ini
http.staticredir newurl
```

#### Example

```ini
http.staticredir http://althost/
```

---

### 8.3.8 trace

```ini
http.trace [-]option [ [-]option ... ]
```

#### Options

- `all`, `debug`, `none`, `off`, `request`, `response`

#### Example

```ini
http.trace all -debug
```

## 9. Document Change History

---

### 14 March 2005

- Removed documentation on local redirection mode.
- Removed documentation of `–s` command line option.
- Added `-t` option to the StartXRD documentation.
- Significantly changed the `port` directive, adding `port any` and `if`.
- Discussed using `port any` mode.

---

### 26 April 2005

- Further clarified the `xrootd.monitor flush` parameter.

---

### 1 June 2005

- Added description of conditional directives (`if-fi`).
- Added description of the `–n` command line option.
- Fully explained which run-time files are created.
- Deprecated `–r`, `–t`, and `–y` command line options.
- Deprecated the `XRDMODE` variable and removed the description of the `XRDTYPE` variable in the StartXRD.cf script.
- Removed extraneous options from the StartXRD script.

---

### 1 August 2005

- Documented administrative interface portal socket.
- Added file size to open monitor record.

---

### 16 August 2005

- Added authentication mapping (a-record) to monitoring data.

---

### 6 January 2006

- Documented the `-b` and `-R` command line options.
- Documented how to independently bind different port numbers to available protocols.

---

### 25 January 2006

- Added `max` option to `chksum` directive.

---

### 22 March 2006

- Added `exec` condition to `if/else/fi`.

---

### 28 February 2007

- Cleaned up documentation relative to `role` directive and `all` prefix modifier.
- Documented the `xrootd.redirect` directive.
- Removed the `xrd.connections` directive.
- Placed most `xrd` directives in esoteric status.

---

### 28 March 2007

- Moved conditional directives to a separate manual.
- Indicated the `adminpath` is now configured via the `all` prefix.
- Documented the `xrd wan network` and `protocol` directive option.
- Indicated that the `xrootd export` directive is configured via the `all` prefix and accepts `oss` options.

---

### 1 October 2007

- Documented the `locate` option of the `redirect` directive.

---

### 1 January 2008

- Removed references to `olbd`.

---

### 1 February 2008

- General clean-up.

---

### 11 April 2008

- Documented staging (`s`) monitor record.

---

### 29 May 2008

- Documented the `xrootd.async nosf` option.

---

### 21 July 2008

- Documented the `xrd.network [no]dnr` option.
- Documented the `xrd.async minsfsz` option.

---

### 6 March 2009

- Documented the `xrootd.monitor stage` option.

---

### 22 June 2009

- Documented the `xrd.report` directive.

---

### 7 July 2009

- Documented the `mpxstats` command for monitoring.
- Documented the summary variables.

---

### 17 March 2010

- Documented the `timeout hail` and `kill` options.
- Documented the `pid` file creation and the `pidpath` directive.

---

### 8 March 2011

- Documented the `–s` command line option.
- Minor editorial changes.

---

### 24 May 2011

- Documented the `auth` option in the `xrootd.monitor` directive.

---

### 31 May 2011

- Changed the `xrootd.chksum` directive to support native checksums.
- Added explanation for native checksums.

---

### 29 June 2011

- Documented the `rbuff` and `redir` options on the `xrootd.monitor` directive to support redirection monitoring.

---

### 27 September 2011

- Documented the `io flush` option on the `xrootd.monitor` directive.

---

### 10 October 2011 — Release 3.1.0

- Documented the `iov`, `migr`, and `purge` options on the `xrootd.monitor` directive.

---

### 2 November 2011

- Updated documentation on the `xrootd.redirect` directive.
- Added support for additional file operations and `ENOENT` targets.

---

### 3 December 2011

- Removed the `migr`, `purge`, and `stage` options from the `xrootd.monitor` directive.
- Moved them to the `frm.all.monitor` directive.
- Documented the new `ident` option on the `xrootd.monitor` directive.

---

### 12 December 2011

- Documented the `rnums` option for the `xrootd.monitor` directive.

---

### 21 September 2012 — Release 3.2.4

- Documented the `fstat` option for the `xrootd.monitor` directive.
- Removed the `rootd` configuration section.

---

### 22 October 2012 — Release 3.2.5

- Documented the `-S` command line option and the `all.sitename` directive.

---

### 15 December 2012 — Release 3.2.7

- Changed the `fstat sdv` option to `fstat ssq` in the `xrootd.monitor` directive.

---

### 11 February 2013

- Enhanced the `fslib` directive to allow wrapping one library with another.

---

### 23 February 2013

- Documented the `–I` command line option.
- Documented the `cache` option in the `xrd.network` directive.

---

### 12 August 2013

- Documented extended `–k`, `–l`, and `–z` command line options.
- Documented exported environment variables.
- Documented the environment information file contents.
- General clean-up and better explanations.

---

### 2 December 2013

- Documented the `xrootd.diglib` directive.

---

### 8 January 2014

- Documented the `routes` option on the `xrd.network` directive.
- Documented enhanced `xrootd.redirect` directive for public/private IPs.

---

### 18 February 2014

- Restricted `routes` option to avoid auto-discovery of interface addresses.

---

### 27 March 2014

- Documented how to enable HTTP and HTTPS protocols.
- Redesigned the `routes` option on the `xrd.network` directive.

---

### 6 August 2014

- Documented the `core` option in the `xrd.sched` directive.
- Documented how to export object identifier names via the `all.export` directive.

---

### 8 September 2014

- Documented that TCP keepalive is now the default.
- Added `nokeepalive` and `kaparms` options to the `xrd.network` directive.
- Indicated `use` option in `xrd.network` accepts one or two interface names.
- Minor corrections to HTTP section.
- Documented `http.mapfile`, `http.staticredir`, `http.staticpreload`, and `http.trace` directives.

---

### 27 September 2014

- Documented multiple checksum support via the `xrootd.chksum` directive.
- Documented the `default` option on the `xrootd.seclib` directive.
- Documented the `–L` command line option.

---

### 26 November 2014

- Documented the `version` option in the `xrootd.fslib` directive.

---

### 10 February 2015

- Documented how to pass command line arguments to plug-ins.
- Documented how to enable `digFS` but prevent its use until needed.

---

### 25 November 2015

- Explained the side-effects of the `–s` command line option on the placement of the environmental file.

---

### 15 April 2016

- Documented log file plug-ins.

---

### 20 June 2016

- Documented the `cse` parameter for logging plug-ins.
- Documented the `xrd.network [no]rpipa` option.

---

### 10 March 2017

- Corrected `http.mapfile` directive (renamed to `http.gridmap`).

---

### 20 May 2017

- Documented the `xrootd.fsoverload` directive.

---

### 27 October 2017

- Documented the `http.header2cgi` directive.

---

### 19 December 2018

- Documented the `xrd.tls` and `xrootd.tls` directives.

---

### 31 May 2019

- Documented the `xrd.tlsca` directive.

---

### 21 June 2019

- Documented the `dyndns` option in the `xrd.network` directive.
- Removed all references to the `wan` option.
- Documented the `xrd tls network`, `port`, and `protocol` directive option.
- Corrected spelling of `xrootd.async segsize` option (was `segsz`).

---

### 18 October 2019

- Documented the preferred version of the `xrootd.fslib` directive.

---

### 21 December 2019

- Documented the interaction between the `dyndns` and `cache` options of the `xrd.network` directive.

---

### 31 March 2020

- Documented the `xrd.tlsciphers` directive.

---

### 11 April 2020

- General cleanup with better descriptions.
- Documented the `ccm`, `pfc`, and `tcpmon` options of the `xrootd.monitor` directive.
- Documented the `xrd.tcpmonlib` directive.
- Documented the `http.cipherfilter` and `http.exthandler` directives.

---

### 14 April 2020

- Documented the `-a` and `-A` command line options.
- Documented the `xrd.homepath` and `xrd.tcpmonlib` directives.

---

### 24 April 2020

- Documented the `xrd.trace` directive’s `tls`, `tlsctx`, `tlsio`, and `tlssok` options.
- Documented the `xrd.tlsca refresh` option.
- Documented the `detail` and `cache` options of the `xrd.tls` directive.
- Documented the `http.httpsmode` directive.

---

### 28 April 2020

- Removed the `xrd.tls` directive’s `cache` option.
- Documented the `xrd.tlsca` directive’s `crlcheck` and `[no]proxies` options.
- Documented changes in the `http.httpsmode` directive where `enable` changed to `manual`.
- Refactored the HTTP protocol section and described deprecated directives.
- Documented that the TLS session cache is disabled by default.
- Documented the `xrootd.tlsreuse` directive.

---

### 5 May 2020

- Added directives by category for `xrd` and `xrootd` sections.
- Cleaned up HTTP section.

---

### 23 July 2020

- Removed documentation of the `xrootd.tlsreuse` directive.
- Added documentation for the `http.tlsreuse` directive.

---

### 20 August 2020

- Documented the `xrootd.monitor` directive’s `...`, `fbuff`, and `gbuff` parameters.
- Documented that the `xrootd.monitor` directive `dest` parameter is now optional.
- Added documentation for the `xrootd.mongstream` directive.

---

### 29 December 2020

- Documented the `+port` option of the `xrd.protocol` directive.

---

### 6 January 2021

- Added admonition that using an external checksum agent via the `xrootd.chksum` directive disables returning checksums in a directory listing.

---

### 16 March 2021

- Documented the `pgcserrs`, `pgread`, and `pgwrite` options of the `xrootd.trace` directive.

---

### 13 June 2021

- Documented the `auth`, `fsaio`, and `fsio` options of the `xrootd.trace` directive.
- Removed the `pgread` and `pgwrite` options of the `xrootd.trace` directive.
- Corrected `minsz` (should be `minsize`) option of the `xrootd.trace` directive.

---

### 30 July 2021

- Documented that `crc32c` is a natively supported checksum.

---

### 2 August 2021

- Documented the `xrootd.bindif` directive.

---

### 22 November 2021

- Documented the `xrootd.pmark` directive.
- Documented the `xrootd.redirect` directive’s `client` option.

---

### 9 December 2021

- Documented the `nocache` option of the `xrootd.async` directive.

---

### 10 March 2022

- Documented the `required` and `compatNameGeneration` options of the `http.gridmap` directive.

---

### 20 March 2022

- Documented the `tpc` monitoring option on the `xrootd.mongstream` and `xrootd.monitor` directives.

---

### 22 May 2023

- Documented the `xrd.maxfd` directive.

---

### 15 August 2023

- Corrected defaults for the `xrootd.pmark` directive.
- Clarified that enabling firefly packets always sends packets to the connecting client using port 10514.

---
