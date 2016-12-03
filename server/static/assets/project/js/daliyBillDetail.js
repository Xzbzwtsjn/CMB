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
     	var dateParams = params['date'];
     	var daliyBillTable = $('#daliyBillTable');
     	if (dateParams){
     	    $.ajax({
         	         type: 'GET',
                         url:'dailyBill',
                         async: false,
                         data:{
                         	date:dateParams
                         },
                         error:function(){
                         	alert('connect falied!');
                         },
                         success:function(data){
                         	data = eval('('+data+')');
                                var jobListTable = $('#jobListTable').DataTable();
                         	if (data){
                         	    $('#Name').text(data.Name);
                         	    $('#Level').text(data.Level);
                         	    $('#Date').text(data.Date);
                         	    $('#Total').text(data.Total);
                         	    $('#ID').text(data.ID);

                         	    for (var i = 0 ; i < data.Jobs.length;i++){
                                        jobListTable.fnAddData([
                                                    data.Jobs[i].JobID,
                                                    data.Jobs[i].JobName,
                                                    data.Jobs[i].command,
                                                    data.Jobs[i].lastSuccess,
                                                    '<td><a href=\'tasklist?jobID='+ data.Jobs[i].JobID+'\'>查看任务</a></td>'
                                                    ],true);
                         	    }
                         	}
                         }
                     });
     	}else{
     	    alert('can\'t get date params!');
     	}
     }
});