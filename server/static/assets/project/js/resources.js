function toPercent(point){
    var str=Number(point*100).toFixed(1);
    str+="%";
    return str;
}

Date.prototype.Format = function (fmt) { //author: meizz 
    var o = {
        "M+": this.getMonth() + 1, //月份 
        "d+": this.getDate(), //日 
        "h+": this.getHours(), //小时 
        "m+": this.getMinutes(), //分 
        "s+": this.getSeconds(), //秒 
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度 
        "S": this.getMilliseconds() //毫秒 
    };
    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
    if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}

function toOrdinaryDate(unixTs){
   var dateTmp = new Date(unixTs);
   return dateTmp.Format('yyyy-MM-dd hh:mm:ss');
}
$(document).ready(function(){
    $.ajax({
         type: 'GET',
         url:'getMachine',
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
                  // alert(data[i].job_info[0].job_name);
                  dataTable.fnAddData([
                        data[i].job_info[0].job_name,
                        data[i].job_info[0].id,
                        data[i].job_info[0].host,
                        toPercent(data[i].job_info[0].mem_used_percentage),
                        toPercent(data[i].job_info[0].cpu_used_in_user/data[i].job_info[0].cpu_total_used),
                        toOrdinaryDate(data[i].job_info[0].ts),
                        toOrdinaryDate(data[i].job_info[1].ts),
                        ],true);
         	    }
	        	
         	}
         }
     });
});