function change2Edit(obj,type){

    var tr = $(obj).parent().parent();
    var a = tr.find("a");
    var aText = a.text();
    var tds = tr.find('td');

    if ('修改' == aText){
        for (var i = 0 ; i < tds.length-3;i++){
            var val = $(tds[i]).text();
            var input = $('<input type=\'text\' value=\''+val+'\'/>');
            $(tds[i]).html(input);
            a.text('更新');
        }
    }else if ('更新' == aText){
         var userprice = $(tds[0]).find('input').val();
         var baseprice = $(tds[1]).find('input').val();
         var cpu = $(tds[2]).text();
         var mem = $(tds[3]).text();
         var data = {};
         if ('mon' == type){
            data = {
                cpu:cpu,
                mem:mem,
                mon:userprice,
                base:baseprice
            }
         }else if ('aft' == type){
            data = {
                cpu:cpu,
                mem:mem,
                aft:userprice,
                base:baseprice
            }
         }else if ('nig' == type){
            data = {
                cpu:cpu,
                mem:mem,
                nig:userprice,
                base:baseprice
            }
         }
          $.ajax({
         type: 'GET',
         url:'updatePolicy',
         async: false,
         data:data,
         error:function(){
         	alert('connect falied!');
         },
         success:function(data){
         	if ('Operation Success' == data){
         	    $(tds[0]).text(userprice);
         	    $(tds[1]).text(baseprice);
         	    $(tds[2]).text(cpu);
         	    $(tds[3]).text(mem);

         	    alert('update success');
         	    a.text('修改');
         	}
         }
     });
         
    }
}

function changeWeight2Edit(obj){
    var tr = $(obj).parent().parent();
    var a = tr.find("a");
    var aText = a.text();
    var tds = tr.find('td');

    if ('修改' == aText){
        var val = $(tds[1]).text();
        var input = $('<input type=\'text\' value=\''+val+'\'/>');
        $(tds[1]).html(input);

        // var val1 = $(tds[3]).text();
        // var input1 = $('<input type=\'text\' value=\''+val1+'\'/>');
        // $(tds[3]).html(input1);

        a.text('更新');
    }else if ('更新' == aText){
         var value = $(tds[1]).find('input').val();

          $.ajax({
         type: 'GET',
         url:'setPair',
         async: false,
         data:{
         	key:'computeRes',
         	value:value
         },
         error:function(){
         	alert('connect falied!');
         },
         success:function(data){
         	if ('Operation Success' == data){

         	    $(tds[1]).text(value);
         	    // var another = Math.round((1-value)*100)/100;
         	    // $(tds[3]).text(another);

         	    alert('update success');
         	    a.text('修改');
         	}
         }
     });
         
    }
}
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
                var tr = $('<tr><td>'+data[i][''+(i+1)].monPrice+'</td><td>'+data[i][''+(i+1)].basePrice+'</td><td  colspan=\'2\'>'+data[i][''+(i+1)].cpu+'</td><td colspan=\'2\'>'+data[i][''+(i+1)].mem+'</td><td><a href="#" onclick="change2Edit(this,\'mon\')">修改</a></td></tr>');
                $('#computeResPreNodeMon').after(tr);
            }
            for (var i = data.length-1; i >= 0 ;i--){
                var tr = $('<tr><td>'+data[i][''+(i+1)].aftPrice+'</td><td>'+data[i][''+(i+1)].basePrice+'</td><td  colspan=\'2\'>'+data[i][''+(i+1)].cpu+'</td><td colspan=\'2\'>'+data[i][''+(i+1)].mem+'</td><td><a href="#" onclick="change2Edit(this,\'aft\')">修改</a></td></tr>');
                $('#computeResPreNodeAft').after(tr);
            }
            for (var i = data.length-1; i >= 0 ;i--){
                var tr = $('<tr><td>'+data[i][''+(i+1)].nigPrice+'</td><td>'+data[i][''+(i+1)].basePrice+'</td><td  colspan=\'2\'>'+data[i][''+(i+1)].cpu+'</td><td colspan=\'2\'>'+data[i][''+(i+1)].mem+'</td><td><a href="#" onclick="change2Edit(this,\'nig\')">修改</a></td></tr>');
                $('#computeResPreNodeNig').after(tr);
            }
         }
     });
});
