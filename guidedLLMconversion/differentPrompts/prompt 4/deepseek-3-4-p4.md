# TLS Configuration Guide {#tls-config}

```toc
- [Command Syntax](#command-syntax)
- [Function](#function)
- [Parameters](#parameters)
- [Defaults](#defaults)
- [Notes](#notes)
- [Examples](#examples)
- [Try It](#try-it)
- [FAQ](#faq)
```

## Command Syntax {#command-syntax}

```bash
xrd.tls cpath [kpath] [options]
```

**Options:**
```bash
[[no]detail] [hsto to{h|m|s}]
```

<div class="interactive-box">
<button class="copy-btn" onclick="copyToClipboard('xrd.tls cpath [kpath] [options]')">Copy Command</button>
<button class="explain-btn" data-target="syntax-explanation">Explain Syntax</button>
</div>

<div id="syntax-explanation" class="explanation-box" style="display:none">
- `cpath`: Path to certificate file (required)
- `kpath`: Path to private key file (optional)
- `options`: Additional configuration flags
</div>

## Function {#function}

Configure transport layer security (TLS) for secure communications.

<div class="info-box">
ℹ️ TLS provides encryption, authentication, and data integrity for network connections.
</div>

## Parameters {#parameters}

### `cpath` 
```path
Absolute path to x509 certificate file (PEM format)
```
- File must be writable only by owner
- Typically stored in `/etc/security/` directory

### `kpath` 
```path
Absolute path to private key file (PEM format)
```
- File must be readable/writable only by owner
- Optional if key is included in certificate file

### Options

#### `[no]detail`
```toggle
[✔️] detail   [ ] nodetail (default)
```
Controls TLS trace message verbosity:
- `detail`: Show traceback messages
- `nodetail`: Suppress traceback messages

#### `hsto`
```time-input
Timeout: [____] [h|m|s]
```
- Sets maximum TLS handshake duration
- Default units: seconds
- Example: `hsto 5m` for 5 minute timeout

## Defaults {#defaults}

```warning
⚠️ TLS is disabled by default - must be explicitly configured
```

## Notes {#notes}

1. **Host Certificates Recommended**  
   Validates server identity to clients

2. **Requires `tlsca` Directive**  
   Must specify Certificate Authority when enabling TLS

3. **Debugging Considerations**  
   Trace messages are primarily useful for:
   - Protocol troubleshooting
   - Connection issues
   - Security audits

## Examples {#examples}

### Basic Configuration
```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```

### With Private Key
```bash
xrd.tls /etc/security/certs/server.pem /etc/security/keys/server.key
```

### Verbose Mode
```bash
xrd.tls /path/to/cert.pem detail hsto 30s
```

<div class="example-buttons">
<button class="try-btn" data-example="basic">Try Basic Example</button>
<button class="try-btn" data-example="with-key">Try With Key</button>
<button class="try-btn" data-example="verbose">Try Verbose</button>
</div>

## Try It {#try-it}

```interactive-sandbox
# TLS Configuration Simulator
Certificate Path: [_________________________] 📁
Private Key Path: [_________________________] 📁 (optional)

Options:
[ ] Enable detail mode
Timeout: [__] [h|m|s]

<button class="test-btn">Test Configuration</button>
<button class="reset-btn">Reset</button>

Output:
-----------------------------------------
> Ready to configure TLS...
```

## FAQ {#faq}

<details>
<summary>What certificate formats are supported?</summary>
Only PEM format is currently supported for both certificates and private keys.
</details>

<details>
<summary>How do I generate a certificate?</summary>
Use OpenSSL:  
`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365`
</details>

<details>
<summary>Why is nodetail the default?</summary>
Trace messages provide minimal additional value for normal operations and may expose sensitive protocol information.
</details>

## CSS Styling

```css
/* Professional color scheme */
:root {
  --primary: #2c3e50;
  --secondary: #1a73e8;
  --accent: #34a853;
  --code-bg: #f6f8fa;
  --warning: #fbbc05;
  --text: #333333;
}

/* Interactive elements */
.interactive-box {
  margin: 15px 0;
  padding: 10px;
  background: #f8f9fa;
  border-left: 3px solid var(--secondary);
}

button.copy-btn, button.explain-btn {
  padding: 5px 10px;
  margin-right: 8px;
  background: var(--secondary);
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.info-box {
  padding: 10px;
  background: #e8f0fe;
  border-left: 3px solid var(--secondary);
  margin: 10px 0;
}

.warning {
  color: var(--warning);
  font-weight: bold;
}
```

## JavaScript for Interactivity

```javascript
document.querySelectorAll('.copy-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const text = this.getAttribute('data-copy');
    navigator.clipboard.writeText(text);
    this.textContent = 'Copied!';
    setTimeout(() => this.textContent = 'Copy', 2000);
  });
});

document.querySelectorAll('.try-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const exampleType = this.getAttribute('data-example');
    // Load example into sandbox
  });
});

// Toggle explanation boxes
document.querySelectorAll('.explain-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const target = this.getAttribute('data-target');
    document.getElementById(target).style.display = 
      document.getElementById(target).style.display === 'none' ? 'block' : 'none';
  });
});
```
