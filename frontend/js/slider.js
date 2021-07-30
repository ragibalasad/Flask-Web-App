const signupForm = document.querySelector('#signupForm')
const loginForm = document.querySelector('#loginForm')

const activeLogin = document.querySelector('#active-login')
const activeSignup = document.querySelector('#active-signup')

activeSignup.addEventListener('click', function(){
    addClass(loginForm,"d-none")
    removeClass(signupForm,'d-none')
    removeClass(activeSignup,'text-secondary')
    addClass(activeLogin,'text-secondary')
})
activeLogin.addEventListener('click', function(){
    // signupForm.classList.add('d-none')
    addClass(signupForm,'d-none')
    // loginForm.classList.remove('d-none')
    removeClass(loginForm,'d-none')
    // activeSignup.classList.remove('text-secondary')
    removeClass(activeLogin,'text-secondary')
    addClass(activeSignup, 'text-secondary')
})

function addClass(element,className) {
    element.classList.add(className);
}
function removeClass(element,className) {
    element.classList.remove(className);
}