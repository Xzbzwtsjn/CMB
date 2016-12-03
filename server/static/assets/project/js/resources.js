$(document).ready(function(){
    $.ajax({
         type: 'GET',
         url:'getResources',
         async: false,
         data:{
         },
         error:function(){
         	alert('connect falied!');
         },
         success:function(data){
         	data = eval('('+data+')');
         	var dataTable = $('#resourcesTable').DataTable();
         	if (data){
         	    for (var i = 0 ; i < data.length ; i++){
         	        var stateStr;
         	        if (true ==data[i].active){
         	        	stateStr='运行';
         	        }else{
         	        	stateStr='宕机';
         	        }

         	        var addressStr = data[i].pid.substring(data[i].pid.indexOf('@')+1);
         	       dataTable.fnAddData([
		        	data[i].id,
		        	data[i].hostname,
		        	addressStr,
		        	data[i].resources.cpus,
                                                data[i].resources.mem,
                                                data[i].resources.disk,
                                                data[i].resources.ports,
		        	stateStr
		        	],true);
         	    }
	        	
         	}
         }
     });
});