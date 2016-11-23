function change2Edit(obj){
	var tr = obj.parentNode.parentNode;
	var a = tr.getElementsByTagName('a');
	var aText = a[0].text ;

	if ('修改' == aText){

		var tds = tr.getElementsByTagName('td');

		for (var i = 0 ; i < tds.length - 3 ; i++){
			var val = tds[i].innerText;
			var input = document.createElement("input");
			input.setAttribute('type','text');
			input.setAttribute('value',val);
			tds[i].innerText = "";
			tds[i].appendChild(input);
		}

		a[0].text = '更新';
	}else if ('更新' == aText){

		var tds = tr.getElementsByTagName('td');

		for (var i = 0 ; i < tds.length - 1 ; i++){

			// var val = tds[i].innerText;
			// var input = document.createElement("input");
			// input.setAttribute('type','text');
			// input.setAttribute('value',val);
			// tds[i].innerText = "";
			// tds[i].appendChild(input);
		}

		a[0].text = '更新';
	}
	
	// alert(obj.parentNode.parentNode);
}
$(document).ready(function(){

});