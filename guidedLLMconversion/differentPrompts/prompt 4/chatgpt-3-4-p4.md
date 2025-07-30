## 3.4 `tls` *(required for TLS)*

<details>
<summary><strong>💡 Command Syntax</strong></summary>

```bash
xrd.tls <cpath> [<kpath>] [options]
```

**Options:**

- `[[no]detail]`
- `hsto <to>{h|m|s}`
</details>

---

### 🔧 Function

Configure **Transport Layer Security (TLS)** for encrypted communication in XRootD.

---

### ⚙️ Parameters

<details>
<summary><code>cpath</code> – Certificate File Path</summary>

Specifies the absolute path to the `x509` certificate file used for TLS.  
- Format must be **PEM**.  
- File must be **owner-writable only**.
</details>

<details>
<summary><code>kpath</code> – Private Key File Path *(optional)*</summary>

Specifies the absolute path to the `x509` private key file used for TLS.  
- Format must be **PEM**.  
- File must be **owner-readable/writable**.  
- If not provided, the key must be embedded in the certificate (`cpath`) file.
</details>

<details>
<summary><code>[no]detail</code> – Trace Output Option</summary>

- If `detail` is specified, detailed TLS trace back messages are printed.  
- `nodetail` (default) suppresses them.  
- Useful for **debugging only**.
</details>

<details>
<summary><code>to</code> – TLS Handshake Timeout</summary>

Sets how long a TLS handshake is allowed before the connection is closed.

- You may append `h`, `m`, or `s` for hours, minutes, or seconds.  
- If no suffix is given, defaults to seconds.  
- **No default timeout** is enforced.
</details>

---

### ✅ Defaults

TLS is **not enabled by default**.

- To enable it, this directive must be explicitly included.  
- Additional directives such as `tlsca` are required.

---

### 📘 Notes

1. 🔐 Use a **host certificate** to ensure clients validate the server identity.
2. ⚠️ If you use the `tls` directive, you **must also** configure the `tlsca` directive.
3. 🐞 TLS trace messages (`detail`) provide minimal extra information unless actively debugging.
   - The `xrd.trace` directive **overrides** this and always enables full detail.

---

### 📎 Example

```bash
xrd.tls /etc/security/xrootd/hostcert.pem
```

---

### 🎨 Recommended Styling (CSS)

```css
body {
  font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
  color: #333;
  line-height: 1.6;
  background-color: #fdfdfd;
}

h2, h3 {
  font-family: 'Roboto Slab', Georgia, serif;
  color: #2c3e50;
  border-bottom: 1px solid #eaecef;
  padding-bottom: 0.3em;
}

code, pre {
  font-family: 'Fira Code', 'Courier New', monospace;
  background-color: #f6f8fa;
  color: #d63200;
  padding: 0.2em 0.4em;
  border-radius: 3px;
}

pre {
  background-color: #f8f9fa;
  border-left: 4px solid #4285f4;
  padding: 1em;
  overflow-x: auto;
}

strong {
  color: #1a73e8;
}
```

---

### 🎨 Font Pairing

- **Headers**: Roboto Slab (serif)  
- **Body Text**: Inter (sans-serif)  
- **Code Blocks**: Fira Code (monospace)

---

### 🌈 Color Scheme

| Element        | Color      | Hex       |
|----------------|------------|-----------|
| Primary Text   | Dark Gray  | `#333333` |
| Headers        | Blue-Gray  | `#2c3e50` |
| Code Text      | Vivid Red  | `#d63200` |
| Accent Blue    | Blue       | `#1a73e8` |
| Background     | Light Gray | `#f8f9fa` |
