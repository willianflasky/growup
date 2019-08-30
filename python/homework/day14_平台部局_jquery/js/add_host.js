/**
 * Created by willian on 2017/4/18.


function addElement() {
    // 获取用户输入的内容
    var host = document.getElementById('host_numb').value;
    var port = document.getElementById('host_port').value;

    // 创建标签(对象) *****
    var tag_tr = document.createElement('tr');
    var tag_td1 = document.createElement('td');
    var tag_td2 = document.createElement('td');
    var tag_td3 = document.createElement('td');
    var tag_input = document.createElement('input');

    tag_td2.innerHTML = host;
    tag_td3.innerHTML = port;
    tag_input.setAttribute("class","option1");
    tag_input.setAttribute("type","checkbox");

    tag_td1.appendChild(tag_input);
    tag_tr.appendChild(tag_td1);
    tag_tr.appendChild(tag_td2);
    tag_tr.appendChild(tag_td3);

    document.getElementById('tbody1').appendChild(tag_tr);

    document.getElementById('host_numb').value = "";
    document.getElementById('host_port').value = "";
}

 function delElement(){
    var list = document.getElementById("tbody1");
    list.removeChild(list.lastElementChild);

    var temp = document.getElementById('display_delete');
    temp.setAttribute('style', 'color:red;');
    temp.innerHTML="删除成功";
    console.log(temp)

    setTimeout(function () {
        document.getElementById('display_delete').innerHTML = "";
    },3000);
}
 */

function addElement() {
    var flag = true;
    $(".err").remove();
    $(".inp1").each(function(){
        var value = $(this).val();
        if(value.length == 0){
            var desc = $(this).attr('desc');
            $(this).after($("<span style='font-size:10px;color: red' class='err'>"  + desc + "必填*</span>"));
            flag = false;
            //return false;
        }
    })

    if(flag == false){
        return flag;
    }

    var host = $("#host_numb").val();
    var port = $("#host_port").val();

    var tag_tr = $("<tr></tr>");
    var tag_td1 = $("<td><input type='checkbox' class='option1'/></td>");
    var tag_td2 = $("<td></td>");
    var tag_td3 = $("<td></td>");
    tag_td2.text(host);
    tag_td3.text(port);

    tag_tr.append(tag_td1, tag_td2, tag_td3);

    $('#tbody1').append(tag_tr);

    $("#host_numb").val("");
    $("#host_port").val("");
}


function delElement(){
    $("#tbody1").children(":last").remove();

    $("#display_delete").css("color",'red').text("删除成功");

    setTimeout(function(){
        $("#display_delete").text("");
    },3000)
}