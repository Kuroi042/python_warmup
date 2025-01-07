// Select all containerslogin-container
const loginContainer = document.getElementById('login');
const signupContainer = document.getElementById('signup');
const mainContainer = document.getElementById('main');

// Form elements
const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');

// Navigation buttons
const goToSignupBtn = document.getElementById('go-to-signup');
const goToLoginBtn = document.getElementById('go-to-login');
const logoutBtn = document.getElementById('logout');

// Temporary storage for users (simulating a database)
let users = [];

// Utility functions
function showContainer(container) {
  document.querySelectorAll('.container').forEach(div => div.classList.remove('active'));
  container.classList.add('active');

}

// Navigation handlers
goToSignupBtn.addEventListener('click', () => showContainer(signupContainer),alert('signup '));
goToLoginBtn.addEventListener('click', () => showContainer(loginContainer) ,alert(' login  !'));
logoutBtn.addEventListener('click', () => {
    showContainer(loginContainer);
    alert('Logged out successfully!');
});

// Handle Signup
signupForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const username = document.getElementById('signup-username').value;
  const email = document.getElementById('signup-email').value;
  const password = document.getElementById('signup-password').value;

 

  // Add user to the "database"
  users.push({ username, email, password });
  alert('Signup successful! Please login.');
  signupForm.reset();
  showContainer(loginContainer);

    // showContainer(mainContainer);
});

// Handle Login
loginForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;

 
  const user = users.find(user => user.email === email && user.password === password);
  if (user) {
    alert(`Welcome back, ${user.username}!`);
    showContainer(mainContainer);
  } else {
    alert('Invalid email or password!');
  }
});