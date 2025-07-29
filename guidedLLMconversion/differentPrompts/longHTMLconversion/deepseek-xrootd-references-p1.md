# XRootD Configuration Reference

15-August-2023  
Release 5.6.1 and above  
Andrew Hanushevsky  

©2004-2023 by the Board of Trustees of the Leland Stanford, Jr., University  
All Rights Reserved  
Produced under contract DE-AC02-76-SFO0515 with the Department of Energy  
This code is open-sourced under a GNU Lesser General Public license.  
For LGPL terms and conditions see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/)

## Table of Contents

1. [Introduction](#1-introduction)  
   1.1 [Security Considerations](#11-security-considerations)  
   1.2 [Starting the xrootd Daemon](#12-starting-the-xrootd-daemon)  
     1.2.1 [Multiple Instances and Automatic Fencing](#121-multiple-instances-and-automatic-fencing)  
     1.2.2 [Passing Plug-In Command Line Arguments](#122-passing-plug-in-command-line-arguments)  
     1.2.3 [Log File Plug-Ins](#123-log-file-plug-ins)  
     1.2.4 [Files created by xrootd](#124-files-created-by-xrootd)  
       1.2.4.1 [Environmental Information File](#1241-environmental-information-file)  
     1.2.5 [Exported Environment Variables](#125-exported-environment-variables)  

2. [Framework Directives by Category](#2-framework-directives-by-category)  
   2.1 [Debugging](#21-debugging)  
   2.2 [Monitoring](#22-monitoring)  
   2.3 [Networking](#23-networking)  
   2.4 [Operational Environment](#24-operational-environment)  
   2.5 [Protocol support](#25-protocol-support)  
   2.6 [Security and TLS](#26-security-and-tls)  
   2.7 [Tuning](#27-tuning)  

3. [Common Framework Configuration Directives](#3-common-framework-configuration-directives)  
   3.1 [adminpath](#31-adminpath)  
     3.1.1 [Administrative Interface](#311-administrative-interface)  
   3.2 [allow](#32-allow)  
   3.3 [homepath](#33-homepath)  
   3.4 [tls (required for TLS)](#34-tls-required-for-tls)  
   3.5 [tlsca (required for TLS)](#35-tlsca-required-for-tls)  

[...continues with full TOC...]

## 1. Introduction

This document describes the eXtended Request Daemon (xrd) configuration directives protocols that can be used with xrd: cmsd, HTTP, and xrootd. It also includes the directives for the xrootd daemon that can run xroot and HTTP protocols.

The xrd is a framework that can dynamically support multiple TCP/IP application service layer protocols. It is designed to provide a high performance environment for application services.

### Component Prefixes

| Component | Purpose |
|-----------|---------|
| `acc` | Access control (i.e., authorization) |
| `cms` | Cluster Management Services |
| `frm` | File Residency Manager |
| `ofs` | Open File System |
| `oss` | Open Storage System (i.e., file system implementation) |
| `pfc` | Proxy File Cache |
| `pss` | Proxy Storage Service |
| `sec` | Security authentication |
| `xrd` | Extended Request Daemon |
| `xrootd` | The xroot protocol implementation |
| `http` | The HTTP protocol implementation |
| `all` | Applies the directive to all components |

*Records that do not start with a recognized identifier are ignored.*

## 1.1 Security Considerations

The xrd framework relies on the loaded protocol(s) for strong authentication (e.g., Kerberos, GSI, etc.). 

Key points:
- The xroot protocol provides strong authentication
- xrd provides host-based authentication via the `allow` directive
- Should not run xrootd as super-user (Unix root) without the `-R` option

## 1.2 Starting the xrootd Daemon

Command syntax:
xrootd [ options ] [ path [ path [ ... ] ] [piargs]


### Options

| Option | Description |
|--------|-------------|
| `-c fn` | Name of configuration file |
| `-l [=]fn` | Message handling: <br>- `fn`: Directs messages to file <br>- `=fn`: Same but unqualified by instance name <br>- `@lib`: Directs messages to plug-in |
| `-k {num | sz{k|m|g} | sig}` |  |
| `-a/-A apath` |  |
| `-b` |  |
| `-d` |  |
| `-h` |  |
| `-I {v4 | v6}` |  |
| `-n name` |  |
| `-R user` | Run as specified user |
| `-s pfn` |  |
| `-S site` |  |
| `-w/-W hpath` |  |
| `-z` |  |
| `-L protlib` |  |
| `-p {port | any}` |  |
| `-P protocol` |  |

### Log File Plug-In Parameters

For `@lib` option:
- `bsz=sz`: Size of speed matching buffer (default 64K)
- `cse={0|1|2}`: Standard error handling:
  - `0`: Don't capture (default)
  - `1`: Capture only if starts with time stamp
  - `2`: Capture all
- `logfn=[=]fn`: Log file destination

### Signal Options

`sig` can be one of:
- `fifo`
- `hup` 
- `rtmin`
- `rtmin+1`
- `rtmin+2` 
- `ttou`
- `winch`
- `xfsz`

[...continues with full content...]