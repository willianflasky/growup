/**
 * Created by willian on 2017/4/18.


function showLogin(){
    document.getElementById('i1').classList.remove('hide');
    document.getElementById('i2').classList.remove('hide');
}
function hideLogin(){
    document.getElementById('i1').classList.add('hide');
    document.getElementById('i2').classList.add('hide');
}

function showRegister(){
    document.getElementById('i1').classList.remove('hide');
    document.getElementById('i3').classList.remove('hide');
}
function hideRegister(){
    document.getElementById('i1').classList.add('hide');
    document.getElementById('i3').classList.add('hide');
}
*/

function showLogin(){
    $("#i1").removeClass('hide');
    $("#i2").removeClass('hide');
}
function hideLogin(){
    $("#i1").addClass('hide');
    $("#i2").addClass('hide');
}

function showRegister(){
    $("#i1").removeClass('hide');
    $("#i3").removeClass('hide');
}
function hideRegister(){
    $("#i1").addClass('hide');
    $("#i3").addClass('hide');
}
