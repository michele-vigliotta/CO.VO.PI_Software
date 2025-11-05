<h1 align="center">CO.VO.PI Software</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/GUI-PyQt5-green.svg" alt="PyQt5">
  <img src="https://img.shields.io/badge/Architecture-MVC-orange.svg" alt="MVC">
</p>

<p>
Python desktop application developed for the <i>Consorzio Vongole del Piceno</i> to manage daily clam-fishing operations, vessel tracking, and automated crew communication.
</p>

<hr>

<p align="center">
  <img src="docs/main_view.png" width="500">
</p>

<h2>Warnings</h2>
<p>
Before starting the software, please read the <code>guide.txt</code> file inside the <code>configurazione/</code> folder.
</p>

<h2>Installation</h2>

<ol>
  <li>Clone the repository and open the project folder</li>
  <li>Create a virtual environment and activate it</li>
  <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
  <li>Read <code>guide.txt</code> inside the <code>configurazione/</code> folder</li>
  <li>Run the app: <code>python main.py</code></li>
</ol>

<h2>Features</h2>

<ul>
  <li><b>Fishing Management:</b> insert total requested sacks; automatic quota calculation; green/red fishing-permission indicator; WhatsApp Web message automation</li>
  <li><b>Vessel Management:</b> add/remove vessels; view vessel details (name, license, crew, responsible person)</li>
  <li><b>GPS Supervision:</b> real-time vessel tracking; restricted-area violation detection; early/late port exit alerts</li>
  <li><b>Weather Monitoring:</b> real-time weather for San Benedetto del Tronto and Porto San Giorgio using the Tutiempo API</li>
  <li><b>Secure Access:</b> login with username and password</li>
</ul>

<h3 align="center">Example: Weather View</h3>
<p align="center">
  <img src="docs/meteo_view.png" width="450">
</p>

<h2>Tech Stack</h2>

<ul>
  <li><b>Python 3, PyQt5 (GUI)</b></li>
  <li><b>JSON</b> (weather and GPS data)</li>
  <li><b>requests</b> (weather API)</li>
  <li><b>pywhatkit</b> + WhatsApp Web automation</li>
  <li><b>MVC architecture</b></li>
  <li><b>Unit tests</b> with <code>unittest</code></li>
</ul>

<h2>Documentation</h2>
<p>
Full technical documentation:  
<a href="docs/RelazioneProgetto.pdf"><code>RelazioneProgetto.pdf</code></a>
</p>

<h2>Authors</h2>

<ul>
  <li>Michele Vigliotta</li>
  <li>Filippo Montagnoli</li>
  <li>Erika Pignotti</li>
</ul>

<hr>

<p align="center"><i>University project developed for the Software Engineering course.</i></p>
