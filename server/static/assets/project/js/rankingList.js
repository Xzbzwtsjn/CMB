$(document).ready(function(){
    $.ajax({
         type: 'GET',
         url:'searchDailyBill?type=job',
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
         	       dataTable.fnAddData([
		        	data[i].job_name,
                              data[i].task_num,
                              data[i].job_cost
		        	],true);
         	    }
	        	
         	}
         }
     });
});