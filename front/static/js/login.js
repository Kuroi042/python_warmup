function renderLoginView() {
    return `
      <h1>Login</h1>
      <form id="login-form">
        <div class="input-field">
          <i class="fa-regular fa-envelope"></i>
          <input type="email" id="login-email" placeholder="Email" />
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
