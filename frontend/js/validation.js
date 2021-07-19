const inputFields = document.querySelectorAll('.inputField');
const loginPasswordField = document.querySelector('#loginPasswordField');
// -----animate the Labels --------
inputFields.forEach(element => {
    element.onfocus = function () {
        element.previousElementSibling.classList.add('activeLabel');
        element.classList.add('activeInputField');
    }
});
inputFields.forEach(element => {
    element.onblur = function () {
        element.previousElementSibling.classList.remove('activeLabel');
        element.classList.remove('activeInputField');
    }
});


// ----- Animate the labels when input fields are filled- --------

inputFields.forEach(element => {
    element.onchange = function () {

        if (element.value !== '') {
            element.previousElementSibling.classList.add('activeLabelFilled');
            element.classList.add('activeInputFieldFilled');
        }else{
            element.previousElementSibling.classList.remove('activeLabelFilled');
            element.classList.remove('activeInputFieldFilled');
            
        }
    }
});

/**** -------Show and hide functionalities---------*****/
const showPass = document.querySelector('.showPass');
const hidePass = document.querySelector('.hidePass');

// ----------- Display the show button---------
loginPasswordField.onkeyup = function(){
    if (loginPasswordField.value !== '') {
        showPass.classList.remove('hide');
    } else {
        showPass.classList.add('hide');
    }
}

// -----------Show and hide password ---------
showPass.onclick = function(){
    loginPasswordField.removeAttribute('type');
    showPass.classList.add('hide');
    hidePass.classList.remove('hide');
}
hidePass.onclick = function(){
    loginPasswordField.setAttribute('type','password');
    showPass.classList.remove('hide');
    hidePass.classList.add('hide');
}