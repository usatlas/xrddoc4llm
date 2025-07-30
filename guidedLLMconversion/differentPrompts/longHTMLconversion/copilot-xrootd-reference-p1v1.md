# XRootD Configuration Reference

**Release:** 5.6.1 and above  
**Date:** 15-August-2023  
**Author:** Andrew Hanushevsky  
**License:** GNU Lesser General Public License  
**Produced under contract DE-AC02-76-SFO0515 with the Department of Energy**

---

## Table of Contents

1. Introduction  
   1.1 Security Considerations  
   1.2 Starting the xrootd Daemon  
   1.2.1 Multiple Instances and Automatic Fencing  
   1.2.2 Passing Plug-In Command Line Arguments  
   1.2.3 Log File Plug-Ins  
   1.2.4 Files created by xrootd  
   1.2.4.1 Environmental Information File  
   1.2.5 Exported Environment Variables  
2. Framework Directives by Category  
   2.1 Debugging  
   2.2 Monitoring  
   2.3 Networking  
   2.4 Operational Environment  
   2.5 Protocol support  
   2.6 Security and TLS  
   2.7 Tuning  
3. Common Framework Configuration Directives  
4. Esoteric Framework Configuration Directives  
5. xrootd Directives by Category  
6. Common xrootd Configuration Directives  
7. Esoteric xrootd Configuration Directives  
8. Enabling HTTP Access  
9. Document Change History  

---

## 1. Introduction

This document describes the eXtended Request Daemon (xrd) configuration directives and protocols that can be used with `xrd`: `cmsd`, `HTTP`, and `xrootd`. It also includes the directives for the `xrootd` daemon that can run `xroot` and `HTTP` protocols. The `cmsd`-specific directives are described in a separate reference manual.

The `xrd` is a framework that can dynamically support multiple TCP/IP application service layer protocols. It is designed to provide a high-performance environment for application services.

### Supported Executables

- `cmsd`: Daemon for the CMS server clustering protocol  
- `xrootd`: Daemon for xroot and other related protocols

### Configuration File Prefixes

| Component | Purpose |
|----------|---------|
| `acc`    | Access control (authorization) |
| `cms`    | Cluster Management Services |
| `frm`    | File Residency Manager |
| `ofs`    | Open File System |
| `oss`    | Open Storage System |
| `pfc`    | Proxy File Cache |
| `pss`    | Proxy Storage Service |
| `sec`    | Security authentication |
| `xrd`    | Extended Request Daemon |
| `xrootd` | The xroot protocol implementation |
| `http`   | The HTTP protocol implementation |
| `all`    | Applies the directive to all components |

---

## 1.1 Security Considerations

- The `xrd` framework relies on loaded protocols for strong authentication (e.g., Kerberos, GSI).
- Host-based authentication is available via the `allow` directive.
- Do not run `xrootd` as super-user unless explicitly intended (`-R` option).
- Security is protocol-specific; refer to each protocol's configuration for details.

---

## 1.2 Starting the xrootd Daemon

```bash
xrootd [ options ] [ path [ path ... ] ] [piargs]
```

### Common Options

- `-c fn`: Configuration file name
- `-l [=]fn`: Log file or plugin
- `-k num|sz|sig`: Log rotation
- `-n name`: Instance name
- `-R user`: Run as specified user
- `-s pfn`: PID file
- `-S site`: Site name for monitoring
- `-p port`: TCP port (default 1094)
- `-P protocol`: Default protocol
- `-b`: Run in background
- `-d`: Enable debugging

### Example

```bash
xrootd -c /opt/xrootd/xrootd.cf
```

---

## 1.2.1 Multiple Instances and Automatic Fencing

- Use `-n` to assign a unique instance name.
- Automatically fences log files, admin paths, and working directories.
- Prevents interference between multiple daemons on the same host.

---

## 1.2.2 Passing Plug-In Command Line Arguments

- Use `-+tag args` to pass arguments to plug-ins.
- Arguments are passed via environment variables like `tag.argc` and `tag.argv**`.

---

## 1.2.3 Log File Plug-Ins

- Use `-l @lib` to specify a logging plug-in.
- Optional parameters:
  - `bsz=sz`: Buffer size
  - `cse=0|1|2`: Standard error capture
  - `logfn=fn`: Additional log file

---

## 1.2.4 Files Created by xrootd

| File/Directory | Description |
|----------------|-------------|
| `<stderr>` | Log output (default) |
| `/tmp/[name]/.xrootd/` | Admin files |
| `<cwd>/[name]/core[.pid]` | Core dumps |
| `/tmp/[name]/exec.pid` | PID file |
| `/tmp/exec.name.env` | Environment info |

---

## 1.2.4.1 Environmental Information File

Format:
```
pid=pid&host=host&inst=inst&ver=ver&home=hpath&cfgfn=cfgfn&cwd=cwd&logfn=logfn
```

---

## 1.2.5 Exported Environment Variables

| Variable | Description |
|----------|-------------|
| `XRDADMINPATH` | Admin path |
| `XRDCONFIGFN` | Config file |
| `XRDDEBUG` | Debug flag |
| `XRDHOST` | Hostname |
| `XRDINSTANCE` | Instance string |
| `XRDLOGDIR` | Log directory |
| `XRDNAME` | Instance name |
| `XRDPROG` | Executable name |
| `XRDSITE` | Site name |

---

## 2. Framework Directives by Category

- `xrd.trace`: Debugging
- `xrd.report`: Monitoring
- `xrd.network`: Networking
- `all.adminpath`: Admin files
- `xrd.homepath`: Working directory
- `xrd.port`: Port number
- `xrd.protocol`: Protocols
- `xrd.allow`: Host restrictions
- `xrd.tls`: TLS certificate
- `xrd.tlsca`: TLS CA
- `xrd.buffers`: Memory buffers
- `xrd.maxfd`: File descriptors
- `xrd.sched`: Threading
- `xrd.timeout`: Timeouts

---

## 3. Common Framework Configuration Directives

- `all.adminpath path [group]`
- `xrd.allow host|netgroup name`
- `xrd.homepath path [group]`
- `xrd.tls cert.pem [key.pem]`
- `xrd.tlsca certfile|certdir [options]`

---

## 4. Esoteric Framework Configuration Directives

- `xrd.buffers memsz [rint]`
- `xrd.maxfd [strict] maxfd`
- `xrd.network [options]`
- `xrd.pidpath path`
- `xrd.port [tls] port`
- `xrd.protocol [tls] name[:port]`
- `xrd.report dest [options]`
- `xrd.sched [params]`
- `xrd.sitename name`
- `xrd.tcpmonlib path`
- `xrd.timeout [params]`
- `xrd.tlsciphers ciphers`
- `xrd.trace [-]option`

---

## 5. xrootd Directives by Category

- Data Access: `all.export`, `xrootd.fslib`, `xrootd.redirect`
- Data Integrity: `xrootd.chksum`
- Debugging: `xrootd.diglib`, `xrootd.trace`
- Monitoring: `xrootd.mongstream`, `xrootd.monitor`, `xrootd.pmark`
- Prepare Processing: `xrootd.prep`
- Security: `xrootd.seclib`, `xrootd.log`, `xrootd.tls`
- Tuning: `xrootd.async`, `xrootd.bindif`, `xrootd.fsoverload`, `xrootd.tlsreuse`

---

## 6. Common xrootd Configuration Directives

- `all.export path [nolock]`
- `xrootd.seclib path`

---

## 7. Esoteric xrootd Configuration Directives

- `xrootd.async [params]`
- `xrootd.bindif host[:port]`
- `xrootd.chksum [params]`
- `xrootd.diglib * authpath`
- `xrootd.fslib path`
- `xrootd.fsoverload [params]`
- `xrootd.log [-]event`
- `xrootd.mongstream events use [params]`
- `xrootd.monitor [params]`
- `xrootd.pmark [params]`
- `xrootd.prep [params]`
- `x