<div style="font-family: 'Helvetica Neue', Arial, sans-serif; color: #333; line-height: 1.6;">

<h1 style="color: #0056b3; font-size: 2.2em; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px; margin-bottom: 20px;">3.4 TLS <span style="font-size: 0.6em; font-weight: normal; color: #555;">(Required for TLS)</span></h1>

<pre style="background-color: #f8f8f8; padding: 15px; border-left: 4px solid #0056b3; margin-bottom: 20px; font-family: 'Consolas', 'Monaco', monospace; font-size: 1.1em; color: #333; overflow-x: auto;">
<code><span style="color: #c0392b;">xrd.tls</span> <em style="color: #007bff;">cpath</em> [ <em style="color: #007bff;">kpath</em> ] [ <em style="color: #007bff;">options</em> ]</code>
</pre>

<p style="font-family: 'Georgia', serif; font-size: 1.1em; color: #555;">
<strong style="color: #0056b3;">Options:</strong> <code style="background-color: #e6e6e6; padding: 3px 6px; border-radius: 4px; font-family: 'Consolas', 'Monaco', monospace; color: #555;">[[no]detail] [hsto <em style="color: #007bff;">to</em>{h|m|s}]</code>
</p>

<h2 style="color: #0056b3; font-family: 'Helvetica Neue', Arial, sans-serif; margin-top: 30px;">Function</h2>

<p style="font-family: 'Georgia', serif; font-size: 1.1em; color: #333; margin-bottom: 20px;">
Configure transport layer security (<strong style="color: #0056b3;">TLS</strong>).
</p>

<details style="background-color: #f0f8ff; border: 1px solid #d0e8ff; border-radius: 5px; padding: 10px; margin-bottom: 20px;">
  <summary style="font-weight: bold; cursor: pointer; color: #0056b3; font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 1.2em;">Parameters</summary>
  <ul style="list-style-type: none; padding-left: 0; margin-top: 10px;">
    <li style="margin-bottom: 15px;">
      <strong style="color: #0056b3; font-family: 'Consolas', 'Monaco', monospace; font-size: 1.05em;">`cpath`</strong><br>
      <span style="font-family: 'Georgia', serif; color: #333;">Specifies the absolute path to the <strong style="color: #0056b3;">x509</strong> certificate file to use for <strong style="color: #0056b3;">TLS</strong>. The certificate must be in <strong style="color: #0056b3;">PEM</strong> format. The file may only be written by the owner.</span>
    </li>
    <li style="margin-bottom: 15px;">
      <strong style="color: #0056b3; font-family: 'Consolas', 'Monaco', monospace; font-size: 1.05em;">`kpath`</strong><br>
      <span style="font-family: 'Georgia', serif; color: #333;">Specifies the absolute path to the certificate’s <strong style="color: #0056b3;">x509</strong> private key file to use for <strong style="color: #0056b3;">TLS</strong>. The key must be in <strong style="color: #0056b3;">PEM</strong> format. The file may only be read and written by the owner of the file. If <em style="color: #007bff;">kpath</em> is not specified, then the certificate file must contain the key.</span>
    </li>
    <li style="margin-bottom: 15px;">
      <strong style="color: #0056b3; font-family: 'Consolas', 'Monaco', monospace; font-size: 1.05em;">`[no]detail`</strong><br>
      <span style="font-family: 'Georgia', serif; color: #333;">When <strong style="color: #0056b3;">detail</strong> is specified, detailed <strong style="color: #0056b3;">TLS</strong> trace back messages are printed along with explanatory messages. The <strong style="color: #0056b3;">nodetail</strong> option suppresses the <strong style="color: #0056b3;">TLS</strong> trace back messages. The default is <strong style="color: #0056b3;">nodetail</strong>. See the notes why this is so.</span>
    </li>
    <li>
      <strong style="color: #0056b3; font-family: 'Consolas', 'Monaco', monospace; font-size: 1.05em;">`to`</strong><br>
      <span style="font-family: 'Georgia', serif; color: #333;">Specifies the maximum amount of time a <strong style="color: #0056b3;">TLS</strong> handshake is allowed to take before the connection is closed. The <em style="color: #007bff;">to</em> value may be suffixed by <strong style="color: #0056b3;">h</strong> for hours, <strong style="color: #0056b3;">m</strong> for minutes, or <strong style="color: #0056b3;">s</strong> for seconds, respectively; otherwise, the <em style="color: #007bff;">to</em> value defaults to seconds. There is no default time limit for the <strong style="color: #0056b3;">TLS</strong> handshake.</span>
    </li>
  </ul>
</details>

<h2 style="color: #0056b3; font-family: 'Helvetica Neue', Arial, sans-serif; margin-top: 30px;">Defaults</h2>

<p style="font-family: 'Georgia', serif; font-size: 1.1em; color: #333; margin-bottom: 20px;">
<strong style="color: #0056b3;">TLS</strong> is not configured and cannot be used. See individual options for the defaults should you configure <strong style="color: #0056b3;">TLS</strong>.
</p>

<details style="background-color: #f0f8ff; border: 1px solid #d0e8ff; border-radius: 5px; padding: 10px; margin-bottom: 20px;">
  <summary style="font-weight: bold; cursor: pointer; color: #0056b3; font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 1.2em;">Notes</summary>
  <ol style="font-family: 'Georgia', serif; color: #333; margin-top: 10px; padding-left: 20px;">
    <li style="margin-bottom: 8px;">Normally, a host certificate should be used because the client can use it to validate that it connected to the intended host.</li>
    <li style="margin-bottom: 8px;">If you specify the <strong style="color: #0056b3;">tls</strong> directive then you must specify the <strong style="color: #0056b3;">tlsca</strong> directive as well.</li>
    <li>Most <strong style="color: #0056b3;">TLS</strong> trace back messages do not provide any more information than the companion explanatory messages and, as such, is only useful for debugging purposes. This is why <strong style="color: #0056b3;">nodetail</strong> is the default. However, if you enable <strong style="color: #0056b3;">TLS</strong> tracing using the <strong style="color: #0056b3;">xrd.trace</strong> directive, <strong style="color: #0056b3;">detail</strong> is enabled regardless of what is specified.</li>
  </ol>
</details>

<h2 style="color: #0056b3; font-family: 'Helvetica Neue', Arial, sans-serif; margin-top: 30px;">Example</h2>

<pre style="background-color: #f8f8f8; padding: 15px; border-left: 4px solid #0056b3; margin-bottom: 20px; font-family: 'Consolas', 'Monaco', monospace; font-size: 1.1em; color: #333; overflow-x: auto;">
<code><span style="color: #c0392b;">xrd.tls</span> /etc/security/xrootd/hostcert.pem</code>
</pre>

</div>