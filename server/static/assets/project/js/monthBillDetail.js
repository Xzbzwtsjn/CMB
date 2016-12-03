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
         var monthParams = params['month'];
         if (monthParams){
         	$.ajax({
         	         type: 'GET',
                         url:'monthlyBill',
                         async: false,
                         data:{
                         	month:monthParams
                         },
                         error:function(){
                         	alert('connect falied!');
                         },
                         success:function(data){
                         	data = eval('('+data+')');

                         	if (data){

                         	    $('#name').text(data.Name);

                         	    if (true == data.Prepaid){
                         	        $('#prepaid').text('是');
                         	    }else{
                         	        $('#prepaid').text('否');
                         	    }

                         	    $('#Level').text(data.Level);
                         	    $('#discount_type1').text(data.Discount[0].Type1);
                         	    $('#discount_type2').text(data.Discount[0].Type2);
                         	    $('#discount_type3').text(data.Discount[0].Type3);
                         	    $('#Discount_Sum').text(data.Discount[1]['Discount_Sum']+'元');

                         	    $('#Total_Billing').text(data.Total_Billing+'元');
                         	    $('#Instance').text(data.Instance);
                         	    $('#ReservedInstance').text(data.ReservedInstance);
                         	    $('#ApplicationType').text(data.ApplicationType);

                         	    $('#Resource_Usage_CPU').text(data.Resource_Usage[0].CPU);
                         	    $('#Resource_Usage_MEM').text(data.Resource_Usage[0].MEM);
                         	    $('#Resource_Usage_NET').text(data.Resource_Usage[0].NET);
                         	    $('#Resource_Usage_IO').text(data.Resource_Usage[0].IO);

                         	    $('#Resource_Request_CPU').text(data.Resource_Request[0].CPU[0].cores+'核-'+data.Resource_Request[0].CPU[0].Frequency+"GHz");
                         	    $('#Resource_Request_MEM').text(data.Resource_Request[1].MEM[0].size+'GB');
                         	    $('#Resource_Request_NET').text(data.Resource_Request[2].NET[0].size);
                         	    $('#Resource_Request_IO').text(data.Resource_Request[3].IO[0].size);

                         	    $('#Service_Usage_Docker_Registry').text(data.Service_Usage[0].Docker_Registry);
                         	    $('#Service_Usage_Load_Average').text(data.Service_Usage[0].Load_Average);
                         	    $('#Service_Usage_Data_Backup').text(data.Service_Usage[0].Data_Backup);
                         	    $('#Service_Usage_Service_Billing').text(data.Service_Usage[0].Service_Billing);

                         	    $('#Cycle').text(data.Cycle);
                         	    $('#BillType').text(data.BillType);
                         	    $('#ID').text(data.ID);
                         	    $('#Amount').text(data.Amount);

                         	    for (var i = 1 ; i <= 31 ; i++){
                         	        var dayBiilAmount = data.Rough_dailyBill[0].days[0][''+i];
                         	        if (dayBiilAmount){
                         	        	$('#dayBillAmount'+i).text(dayBiilAmount);
                         	        	$('#dayBillHref'+i).attr('href','daliyBillDetail?date='+monthParams+'-'+i);
                         	        }else{
                         	        	$('#dayBillAmount'+i).text('None');
                         	        }
                         	    }
                         	    $('#dayBilltotal').text(data.Rough_dailyBill[1].total);
                         	}
                         }
                     });
         }else{
              alert('can\'t get month param');
         }
     }

});