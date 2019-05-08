/*  Remove mascot class from element "main" if its width is <= mascotMinWidth */
function controlMascot(mascot, mascotMinWidth) {
	$(window).resize(function(event) {
		if ( $(window).width() <= mascotMinWidth && $("main").hasClass("mascot") ) {
			removeMascot();
		} else if( $(window).width() > mascotMinWidth && ! $("main").hasClass("mascot") ) {
			setMascot(mascot);
		}
	});
}

function setMascot(mascot) {
	$('main').addClass("mascot");
	$('main').css("background-image", "url(" + mascot + ")");
	$('main').removeClass("plain");
}

function removeMascot() {
	$('main').removeClass("mascot");
	$('main').css("background-image", "");
	$('main').addClass("plain");
}

$(document).ready(function(event) {
	var mascotEnable    = true;
	var mascotPath      = "images/mascots/"
	var mascotList      = [
			'mikasaLeft.png',
			'royo.png'
			];
	var mascot         = mascotPath + mascotList[Math.floor(Math.random() * mascotList.length)];
	var mascotMinWidth = '650';

	if ( mascotEnable ) { 
		setMascot(mascot);
		controlMascot(mascot, mascotMinWidth);
	} else { removeMascot(); }

	var request = new XMLHttpRequest();
	request.onload = function() {
	    // get the file contents
	    var fileContent = this.responseText;
	    // split into lines
	    var fileContentLines = fileContent.split( '\n' );
	    // get a random index (line number)
	    var randomLineIndex = Math.floor( Math.random() * fileContentLines.length );
	    // extract the value
	    var randomLine = fileContentLines[ randomLineIndex ];
	
	    // add the random line in a div
	    document.getElementById('randQuote').innerHTML = randomLine;
	};
	request.open('GET', 'quotes.txt', true );
	request.send();
});

