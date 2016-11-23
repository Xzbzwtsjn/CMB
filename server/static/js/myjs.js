$(document).ready(function() {
		$('#projectdata,#xqfx_data,#develop_data,#test_data,#online_data').daterangepicker(null,function(start, end, label) {
			console.log(start.toISOString(), end.toISOString(), label);});
						      });