function renderSignupView() {
    return `
        <h2>Register</h2>
        <form id="signup-form">
            <div class="input-field">
                <i class="fa-regular fa-user"></i>
                <input type="text" id="signup-username" placeholder="Name" />
            </div>
            <div class="input-field">
                <i class="fa-regular fa-envelope"></i>
                <input type="email" id="signup-email" placeholder="Email" />
            </div>
                        <div class="input-field">
                        <i class="fa-solid fa-lock"></i>
                <input type="text" id="password" placeholder="password" />
            </div>
            <div class="input-field">
            <i class="fa-solid fa-lock"></i>
            <input type="text" id="confirm-password" placeholder="confirm password" />
        </div>
            <div class="btn-field">
                <button type="submit" id="register">Register</button>
            </div>
            <div class="btn-field">
                <button type="button" id="go-to-login">Already have an account?</button>
            </div>
        </form>
    `;
}

window.renderSignupView = renderSignupView;
