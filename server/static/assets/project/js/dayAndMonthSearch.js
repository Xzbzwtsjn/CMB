$(document).ready(function(){
     var dataTable = $('#daliyResultTable').DataTable();
    // $('#daliySearchTypeSelect').on('change',function(){
    //      var daliySearchType = $('#daliySearchTypeSelect').val();
    //      if ('keyword' == daliySearchType){
    //      	$('#daliyKwDiv').attr('class','');
    //      	$('#daliyDpDiv').attr('class','hide');
    //      	dataTable.fnClearTable();
    //      }else{
    //      	$('#daliyKwDiv').attr('class','hide')
    //      	$('#daliyDpDiv').attr('class','');
    //      	dataTable.fnClearTable();
    //      }
    // });

    $('#daliysearchBtn').on('click',function(){

        dataTable.fnClearTable();
        // var daliySearchType = $('#daliySearchTypeSelect').val();
        var startDate = $('#daliyDatepickerStart').val();
             var endDate = $('#daliyDatepickerEnd').val();
            if (startDate && endDate ){
                 $.ajax({
                     type: 'GET',
                         url:'searchDailyBill',
                         async: false,
                         data:{
                            start_date:startDate,
                         end_date:endDate,
                            type:'date'
                         },
                         error:function(){
                            alert('connect falied!');
                         },
                         success:function(data){
                            data = eval(data);
                            if (data.length && data.length > 0){
                                for (var i = 0 ; i < data.length;i++){
                                   
                                    var typeStr;
                                    if ('D' == data[i].type){
                                        typeStr="日账单";
                                    }else if ('M' == data[i].type){
                                        typeStr='月账单';
                                    }else{
                                        typeStr='未知类型';
                                    }

                dataTable.fnAddData([
                    data[i].ID,
                    data[i].Date,
                    typeStr,
                    data[i].total,
                    '<td><a href=\'daliyBillDetail?date='+data[i].Date+'\'>查看详细</a></td>'
                    ],true);
                                }
                            }
                         }
                     });
            }else{
                alert('input can\'t be empty')
            }
    });

   if ($('#daliyDatepickerStart').length > 0){
	var nowTemp = new Date();
	var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);
	 
	var checkin = $('#daliyDatepickerStart').datepicker({
	  format:'yyyy-mm-dd',
	  onRender: function(date) {
		return date.valueOf()  >= now.valueOf() ? 'disabled' : '';
	  }
	}).on('changeDate', function(ev) {
	  checkin.hide();
	  dataTable.fnClearTable();
               $('#daliyDatepickerEnd')[0].focus();
	}).data('datepicker');
    }

    if ($('#daliyDatepickerEnd').length > 0){
    var nowTemp = new Date();
    var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);
     
    var checkout = $('#daliyDatepickerEnd').datepicker({
      format:'yyyy-mm-dd',
      onRender: function(date) {
        return date.valueOf()  >= now.valueOf() ? 'disabled' : '';
      }
    }).on('changeDate', function(ev) {
      checkout.hide();
      dataTable.fnClearTable();
    }).data('datepicker');
    }


    //---------------------------------------------------monthly js----------------------------------------------------------------
     var monthlyDataTable = $('#monthlyResultTable').DataTable();
    // $('#monthlySearchTypeSelect').on('change',function(){
    //      var monthlySearchType = $('#monthlySearchTypeSelect').val();
    //      if ('keyword' == monthlySearchType){
    //      	$('#monthlyKwDiv').attr('class','');
    //      	$('#monthlyDpDiv').attr('class','hide');
    //      	monthlyDataTable.fnClearTable();
    //      }else{
    //      	$('#monthlyKwDiv').attr('class','hide')
    //      	$('#monthlyDpDiv').attr('class','');
    //      	monthlyDataTable.fnClearTable();
    //      }
    // });

    $('#monthlysearchBtn').on('click',function(){
        monthlyDataTable.fnClearTable();
        var startMon = $('#monthlyDatepickerStart').val();
             var endMon = $('#monthlyDatepickerEnd').val();
            if (startMon && endMon){
                 $.ajax({
                     type: 'GET',
                         url:'searchMonthlyBill',
                         async: false,
                         data:{
                            start_mon:startMon,
                         end_mon:endMon,
                            type:'date'
                         },
                         error:function(){
                            alert('connect falied!');
                         },
                         success:function(data){
                            data = eval(data);
                            if (data.length && data.length > 0){
                                for (var i = 0 ; i < data.length;i++){
                                   
                                    var typeStr;
                                    if ('D' == data[i].type){
                                        typeStr="日账单";
                                    }else if ('M' == data[i].type){
                                        typeStr='月账单';
                                    }else{
                                        typeStr='未知类型';
                                    }

                monthlyDataTable.fnAddData([
                    data[i].ID,
                    data[i].Month,
                    typeStr,
                    data[i].Total_Billing,
                    '<td><a href=\'monthlyBillDetail?month='+data[i].Month+'\'>查看详细</a></td>'
                    ],true);
                                }
                            }
                         }
                     });
            }else{
                alert('input can\'t be empty')
            }
    });
    // var monthlyNowTemp = new Date();
    // var year = monthlyNowTemp.getFullYear();
    // if (monthlyNowTemp.getMonth()+1> 12){
    //     year = year+1;
    // }

    // var month =  (monthlyNowTemp.getMonth()+1)%12;
    // // alert(year+'-'+month);
    //  var monthlyNow = new Date(year, month,1, 0, 0, 0, 0);
    // $('.month').datetimepicker({
    //     format:'yyyy-mm',
    //     language:  'zh-CN',
    //     endDate:'2016-12',
    //     weekStart: 1,
    //     todayBtn:  1,
    //     autoclose: 1,
    //     todayHighlight: 1,
    //     startView: 3,
    //     minView: 3,
    //     maxView: 3,
    //     forceParse: 0
    // });


   if ($('#monthlyDatepickerStart').length > 0){
	var monthlyNowTemp = new Date();
	var monthlyNow = new Date(monthlyNowTemp.getFullYear(), monthlyNowTemp.getMonth(), monthlyNowTemp.getDate(), 0, 0, 0, 0);
	 
	var monthlyCheckin = $('#monthlyDatepickerStart').datepicker({
	  format:'yyyy-mm',
	  viewMode: 'months',
                minViewMode:'months',
	  onRender: function(date) {
		return '';
	  },
	}).on('changeDate', function(ev) {

	  monthlyCheckin.hide();
	  monthlyDataTable.fnClearTable();
               $('#monthlyDatepickerEnd')[0].focus();
	}).data('datepicker');
    }
    if ($('#monthlyDatepickerEnd').length > 0){
    var monthlyNowTemp = new Date();
    var monthlyNow = new Date(monthlyNowTemp.getFullYear(), monthlyNowTemp.getMonth(), monthlyNowTemp.getDate(), 0, 0, 0, 0);
     
    var monthlyCheckout = $('#monthlyDatepickerEnd').datepicker({
      format:'yyyy-mm',
      viewMode: 'months',
                minViewMode:'months',
      onRender: function(date) {
        return '';
      },
    }).on('changeDate', function(ev) {
      monthlyCheckout.hide();
      monthlyDataTable.fnClearTable();
    }).data('datepicker');
    }
});