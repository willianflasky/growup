/**
 * Created by willian on 2017/4/18.
 */

setInterval(function(){
    var txt = document.getElementById('welcome').innerText;
    var a = txt.charAt(0)
    var b = txt.substring(1, txt.length)
    var new_txt = b + a
    document.getElementById('welcome').innerText = new_txt;
},1000)