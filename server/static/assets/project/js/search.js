$(document).ready(function(){
	$('#searchBtn').on('click',function(){
		var imageName = $('#imageName').val();
		var dataTable = $('#searchResultTable').DataTable();
		if (imageName){
			$.ajax({
			         type: 'GET',
			         url:'searchByImages',
			         async: false,
			         data:{
			         	image:imageName
			         },
			         error:function(){
			         	alert('connect falied!');
			         },
			         success:function(data){
			         	// alert(data);
			         	if (data){
			         		data = eval('('+data+')');
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
		}else{
			alert('please input image name');
		}
		
	});
});