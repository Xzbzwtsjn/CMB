$(document).ready(function(){
    $.ajax({
         type: 'GET',
         url:'getPolicy',
         async: false,
         data:{
         },
         error:function(){
         	alert('connect falied!');
         },
         success:function(data){
         	data = eval('('+data+')');
         	for (var i = data.length-1; i >= 0 ;i--){
         	    var tr = $('<tr><td>'+data[i][''+(i+1)].monPrice+'</td><td>'+data[i][''+(i+1)].basePrice+'</td><td  colspan=\'2\'>'+data[i][''+(i+1)].cpu+'</td><td colspan=\'2\'>'+data[i][''+(i+1)].mem+'</td></tr>');
         	    $('#computeResPreNodeMon').after(tr);
         	}
            for (var i = data.length-1; i >= 0 ;i--){
                var tr = $('<tr><td>'+data[i][''+(i+1)].aftPrice+'</td><td>'+data[i][''+(i+1)].basePrice+'</td><td  colspan=\'2\'>'+data[i][''+(i+1)].cpu+'</td><td colspan=\'2\'>'+data[i][''+(i+1)].mem+'</td></tr>');
                $('#computeResPreNodeAft').after(tr);
            }
            for (var i = data.length-1; i >= 0 ;i--){
                var tr = $('<tr><td>'+data[i][''+(i+1)].nigPrice+'</td><td>'+data[i][''+(i+1)].basePrice+'</td><td  colspan=\'2\'>'+data[i][''+(i+1)].cpu+'</td><td colspan=\'2\'>'+data[i][''+(i+1)].mem+'</td></tr>');
                $('#computeResPreNodeNig').after(tr);
            }
         }
     });
});