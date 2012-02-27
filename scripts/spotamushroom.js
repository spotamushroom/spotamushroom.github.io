function found(message) {
	highlight();
	document.getElementById('blurb').style.display = "block";
	document.getElementById('legend').innerHTML = message;
	
	return true;
}

function highlight() {
	document.getElementById("overlay").style.display = "block";
	document.getElementById("hint").style.display = "none";
	return true;
}

setTimeout(function() {
	document.getElementById("hint").style.display = "inline";
}, 20000);