//Useful jsfuncs

function rs(q){
	// When using params be sure to use
	// double backslash due to the string
	// escaping
	if (typeof q=='undefined'){
		var s=prompt("Regex Search Term");
	} else {var s=q.toString();}
	var p=new RegExp(s,"g");
	console.log(document.body.innerText.match(p));
}
function avg(q){
	// Get average of the numbers
	// in an array
	var out=0;
	for(var i=0;i<q.length;i++){
		out+=parseInt(q[i]);}
	return out/q.length;
}
function max(q){return b-a} // Sort array max to min
function min(q){return a-b} // Sort array min to max
