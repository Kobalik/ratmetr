$(document).ready(function(){

});

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);

function checkParamsOnAddmarks() {
    var inputGroups = $('#inputGroups').val();
    var inputSubjects = $('#inputSubjects').val();
    var inputTypeMarks = $('#inputTypeMarks').val();
     
    if(inputGroups.length != 0 && inputSubjects.length != 0 && inputTypeMarks.length != 0) {
        $('#loadbutton').removeAttr('disabled');
    } else {
        $('#loadbutton').attr('disabled', 'disabled');
    }
}

function checkParamsOnRegister() {
    var username = $('#username').val();
    var email = $('#email').val();
    var password = $('#password').val();
    var confirmPassword = $('#confirmPassword').val();

    if(username.length != 0 && email.length != 0 && password.length != 0 && confirmPassword.length != 0) {
        $('#submitRegister').removeAttr('disabled');
    } else {
        $('#submitRegister').attr('disabled', 'disabled');
    }
}

function checkParamsOnLogin() {
    var username = $('#username').val();
    var password = $('#password').val();

    if(username.length != 0 && password.length != 0) {
        $('#submitLogin').removeAttr('disabled');
    } else {
        $('#submitLogin').attr('disabled', 'disabled');
    }
}

function checkParamsOnVedom() {
    var group = $('#group').val();
    var typeVedom = $('#typeVedom').val();

    if (typeVedom == 'Контроль текущей успеваемости') {
        var countPoint = $('#countPoint').val()
        $('#countPoint').css({'visibility' : ''});
        $('#labelCountPoint').css({'visibility' : ''});

        if(group.length != 0 && typeVedom.length != 0 && countPoint.length != 0) {
            $('#submitVedom').removeAttr('disabled');
        } else {
            $('#submitVedom').attr('disabled', 'disabled');
        }
    } else {
        $('#countPoint').css('visibility', 'hidden');
        $('#labelCountPoint').css('visibility', 'hidden');

        if(group.length != 0 && typeVedom.length != 0) {
            $('#submitVedom').removeAttr('disabled');
        } else {
            $('#submitVedom').attr('disabled', 'disabled');
        }
    }
}

function checkParamsOnSearch() {
    var selected_group = $('#selected_group').val();

    if(selected_group.length != 0) {
        $('#submitSearch').removeAttr('disabled');
    } else {
        $('#submitSearch').attr('disabled', 'disabled');
    }
}

function checkParamsOnSearchStudent() {
    var selected_text = $('#selected_text').val();

    if(selected_text.length != 0) {
        $('#submitSearchStudent').removeAttr('disabled');
    } else {
        $('#submitSearchStudent').attr('disabled', 'disabled');
    }
}