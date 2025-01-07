// Get references to elements
let title = document.getElementById("title");
let signupbtn = document.getElementById("signupbtn");
let signinbtn = document.getElementById("signinbtn");
let nameField = document.getElementById("nameField");

//  switch to sign In
signinbtn.onclick = function () {
    nameField.style.maxHeight = "0";  //hide
    title.innerHTML = "Sign In";  
    signupbtn.classList.add("disable");
    signinbtn.classList.remove("disable");
};

//   switchto sign Up
signupbtn.onclick = function () {
    nameField.style.maxHeight = "60px"; 
    title.innerHTML = "Sign Up";  
    signupbtn.classList.remove("disable");
    signinbtn.classList.add("disable");
};
