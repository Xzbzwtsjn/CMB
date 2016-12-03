function GetRequest() { 
    var url = location.search; //获取url中"?"符后的字串 
    var theRequest = new Object(); 
    if (url.indexOf("?") != -1) { 
        var str = url.substr(1); 
        strs = str.split("&"); 
        for(var i = 0; i < strs.length; i ++) { 
            theRequest[strs[i].split("=")[0]]=unescape(strs[i].split("=")[1]); 
        } 
    } 
    return theRequest; 
} 

$(document).ready(function(){
     var params = GetRequest() ;
     if (params){
          var jobID = params['jobID'];
         if (jobID){
         	$.ajax({
	         type: 'GET',
	         url:'dailyTaskDetail',
	         async: false,
	         data:{
	         	jobID:jobID
	         },
	         error:function(){
	         	alert('connect falied!');
	         },
	         success:function(data){
	         	data = eval('('+data+')');
	         	var dataTable = $('#taskListTable').DataTable();
	         	if (data){
	         	    for (var i = 0 ; i < data.taskList.length ; i++){
	         	       dataTable.fnAddData([
		 	 data.taskList[i].TaskID,
		        	data.taskList[i].ResourceUsage[0].CPU,
		        	data.taskList[i].ResourceUsage[0].MEM,
		        	data.taskList[i].ResourceUsage[0].NET,
		        	data.taskList[i].ResourceUsage[0].IO
		        	],true);
	         	    }
		        	
	         	}
	         }
	     });
         }
     }
    
});