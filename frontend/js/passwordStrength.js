const passwordField = document.querySelector('input');
const indicator = document.querySelector('.indicator');

passwordField.addEventListener('keyup', ()=>{
    let uppercase = /[A-Z]/g;
    if (passwordField.value.match(uppercase)) {
        console.log("This field contain uppercase");
    }

    let lowercase = /[a-z]/g;
    if(passwordField.value.match(lowercase)) {
        console.log("This field contain lowercase");
    }

    let number = /\d/;
    if(passwordField.value.match(number)){
        console.log("This field contain number");
    }

    let specialCharacter = /[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/
    if(passwordField.value.match(specialCharacter)){
        console.log("This field contain special character");
    }
});
