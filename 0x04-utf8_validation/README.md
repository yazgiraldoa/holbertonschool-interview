<h1 class="gap">0x04. UTF-8 Validation</h1>

<p>Write a method that determines if a given data set represents a valid UTF-8 encoding.</p>

<ul>
<li>Prototype: <code>def validUTF8(data)</code></li>
<li>Return: <code>True</code> if data is a valid UTF-8 encoding, else return <code>False</code></li>
<li>A character in UTF-8 can be 1 to 4 bytes long</li>
<li>The data set can contain multiple characters</li>
<li>The data will be represented by a list of integers</li>
<li>Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer</li>
</ul>
