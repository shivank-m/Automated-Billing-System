// const firebaseConfig = {
//   apiKey: "AIzaSyBIZ8IDNxE67lyFgJwdlNdQF-eolSXVXNs",
//   authDomain: "automated-billing-management.firebaseapp.com",
//   databaseURL: "https://ieee-ias-website-default-rtdb.firebaseio.com",
//   projectId: "automated-billing-management",
//   storageBucket: "automated-billing-management.appspot.com",
//   messagingSenderId: "279255826434",
//   appId: "1:279255826434:web:89c1d47e058272539be71b",
//   measurementId: "G-C59XN2X92Z"
// };
// // Initialize Firebase
// firebase.initializeApp(firebaseConfig);
// firebase.getAnalytics();
// // Listen for form submit
// alert("ho");
// var messageRef = firebase.database().ref('messages');
// alert("He");
// document.getElementById("contactForm").addEventListener('submit', submitForm);
// alert(document.getElementById("contactForm").addEventListener('submit', submitForm));

// //Submit Form
// function submitForm(e) {
//   alert("Hello");
//     e.preventDefault();

//     // Get values
//     var username = getInputVal("username");
//     var phone = getInputVal("phone");
//     var problem = getInputVal("problem");
//     alert(username, phone, problem);

//     saveMessage(username, phone, problem);

//     // show alert
//     document.querySelector('.alert').style.display = 'block';

    
//     alert(username, phone, problem);
//     // Hide after 3 sec
//     setTimeout(function(){
//         document.querySelector('.alert').style.display = 'none';
//     }, 2000);

//     document.getElementById('contactForm').reset();
// }

// // Function to get Form values

// function getInputVal(id) {
//     return document.getElementById(id).value;
// }

// // Save messages

// function saveMessage(username, phone, problem){
//     var newmessageRef = messageRef.push();
//     newmessageRef.set({
//         username: username,
//         phone: phone,
//         problem: problem
//     });
// }

const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

