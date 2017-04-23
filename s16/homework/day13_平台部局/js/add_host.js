/**
 * Created by willian on 2017/4/18.
 */

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

    // 将对象添加到 append
    document.getElementById('tbody1').appendChild(tag_tr);
    /*
    var tag = "<li>" + val +"</li>";
    document.getElementById('container').insertAdjacentHTML("beforeEnd",tag);
    */

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


