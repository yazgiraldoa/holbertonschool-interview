<h1 class="gap">0x03. Log Parsing</h1>

<p>Write a script that reads <code>stdin</code> line by line and computes metrics:</p>

<ul>
<li>Input format: <code>&lt;IP Address&gt; - [&lt;date&gt;] &quot;GET /projects/260 HTTP/1.1&quot; &lt;status code&gt; &lt;file size&gt;</code> (if the format is not this one, the line must be skipped)</li>
<li>After every 10 lines and/or a keyboard interruption (<code>CTRL + C</code>), print these statistics from the beginning:

<ul>
<li>Total file size: <code>File size: &lt;total size&gt;</code></li>
<li>where <code>&lt;total size&gt;</code> is the sum of all previous <code>&lt;file size&gt;</code> (see input format above)</li>
<li>Number of lines by status code: 

<ul>
<li>possible status code: <code>200</code>, <code>301</code>, <code>400</code>, <code>401</code>, <code>403</code>, <code>404</code>, <code>405</code> and <code>500</code></li>
<li>if a status code doesn&rsquo;t appear or is not an integer, don&rsquo;t print anything for this status code</li>
<li>format: <code>&lt;status code&gt;: &lt;number&gt;</code></li>
<li>status codes should be printed in ascending order</li>
</ul></li>
</ul></li>
</ul>
