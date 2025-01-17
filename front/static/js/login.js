function loadGoogleAPI(callback) {
  if (typeof window.google !== 'undefined' && window.google.accounts) {
      // Google API already loaded, execute the callback immediately
      callback();
      return;
  }

  // Create a script tag to load the Google API
  const script = document.createElement('script');
  script.src = "https://accounts.google.com/gsi/client";
  script.async = true;
  script.defer = true;
  script.onload = callback;  // Execute callback once the script is loaded
  script.onerror = () => {
      console.error("Google API script failed to load.");
  };

  // Append the script tag to the head of the document
  document.head.appendChild(script);
}


// Call this function after rendering the login view
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('google-signin-container')) {
    initializeGoogleSignin();
  }
});

 

function renderLoginView() {
    return `
      <h1>Login</h1>
      <form id="login-form">
        <div class="input-field">
          <i class="fa-regular fa-envelope"></i>
          <input type="email" id="login-email" placeholder="Email" required />
        </div>
        <div class="input-field">
          <i class="fa-solid fa-lock"></i>
          <input type="password" id="login-password" placeholder="Password" />
        </div>
        <p>Lost password? <a href="#">Click here!</a></p>
        <div class="btn-field">
          <button type="submit" id="login-btn">Log In</button>
        </div>
        <div class="btn-field">
          <button type="button" id="go-to-signup">Don't have an account?</button>
        </div>
        <div class="btn-field">
          <button type="button" id="intra-btn">Login with 42</button>
        </div>
        <div class="btn-field">
          <button type="button" id="gmail-btn">Login with Gmail</button>
        </div>
      </form>
    `;
  }

window.renderLoginView = renderLoginView;
