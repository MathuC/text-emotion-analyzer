import { useState } from 'react'
import "./App.css"

function App() {
  	const [text, setText] = useState("");
  	const [output, setOutput] = useState("");

  	return (
		<div>
			<div id="links-container">
			<div id="gh-logo-container">
				<a href="https://github.com/MathuC/text-emotion-analyzer">
				<img id="gh-logo" src='img/ghLogo.png'></img>
				</a>
			</div>
			<div id="my-link-container">
				<a id="my-link" href='https://mathusan.net'>
				<span>mathusan.net</span>
				</a>
			</div>
			</div>
				<h1 id="title">TEXT EMOTION ANALYZER</h1>
				<center>
					<textarea id="text-input" placeholder="Type something..."></textarea>
				</center>
		</div>
  	);
}

export default App
