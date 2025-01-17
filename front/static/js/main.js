


 
function initializeGoogle() {
    window.google.accounts.id.initialize({
        client_id: '598064932608-4j38572h65hmj37524inmc1nhcfqiqpm.apps.googleusercontent.com',  // Replace with your actual client ID
        callback: handleGoogleLogin
    });

    window.google.accounts.id.renderButton(
        document.getElementById('gmail-btn'), // The element where you want to render the button
         { theme: "outline", size: "small" }            // Customize button appearance
    );

    window.google.accounts.id.prompt();  // Optional, can show the one-tap prompt
}
function handleGoogleLogin(response) {
    const id_token = response.credential;

    if (!id_token) {
        console.error('Google Auth error: Token not found');
        return;
    }

    // Send the token to your backend for verification and user login
    fetch('http://localhost:8000/accounts/google/login/callback/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ token: id_token }) // Send the token
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Login successful!") {
                        const userName = data.user?.name || "User";
            alert(`Welcome, ${userName}! Successfully logged in with Google!`);

            renderView(renderMainView);
            const userInfoElement = document.getElementById('user-info');
            if (userInfoElement) {
                userInfoElement.innerHTML = `Welcome Merhba , ${userName}`;
            }
            alert('Successfully logged in with Google!' );

             
        } else {
            console.error("Login failed:", data);
            alert('Login failed. Please try again.');
        }
    })
    .catch(error => {
        console.error("Error during Google login:", error);
        alert('An error occurred during login. Please try again.');
    });
}
document.addEventListener('DOMContentLoaded', () => {
    initializeGoogle();  // Initialize Google login
});

renderMainView();
renderLoginView();
renderSignupView();

const dataToSend = {


    name: "John Doe",
    email: "john.doe@example.com",
    message: "Hello from the frontend!"
};
function renderView(viewFunction) {
    const container = document.getElementById('view-container');
    container.innerHTML = viewFunction();
    container.classList.add('active');
}


document.addEventListener('DOMContentLoaded', () => {
    renderView(renderLoginView);
    document.addEventListener('click', async (event) => {


        const target = event.target;
        if (target.id === 'go-to-signup') {
            console.log("'signup button clicked!'");
            renderView(renderSignupView);
        }
        else if (target.id === 'register') {
            console.log("'register button clicked!'");
            const data = {
                username: document.getElementById('signup-username').value,
                email: document.getElementById('signup-email').value,
                password: document.getElementById('password').value,
                password2: document.getElementById('confirm-password').value,
            };

            // Send the data directly without nesting
            try {
                const response = await fetch('http://localhost:8000/register-action/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                    body: JSON.stringify(data),  // Send data directly
                });

                if (response.ok) {
                    const responseData = await response.json();
                    console.log('Server response', responseData.message);
                    
                    alert('Account created successfully! Redirecting to login page...' );

                    renderView(renderLoginView);
                } else {
                    const errorData = await response.json();
                    console.log('Fetch error:', errorData);
                    alert('Error: ' + errorData.message);
                }
            } catch (error) {
                console.log('Error:', error);
            }
        }

        else if (target.id === 'login-btn') {

            const data = {
                email: document.getElementById('login-email').value,
                password: document.getElementById('login-password').value,

            };
            try {
                const response = await fetch('http://localhost:8000/login-action/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),  // Send data directly
                });

                if (response.ok) {
                    const responseData = await response.json();
                    console.log('Server response', responseData.message);
                    alert('Account logged successfully! Redirecting to login page...');
                    alert(`Welcome ${responseData.user.username}!`);
                    renderView(renderMainView);
                    const userInfoElement = document.getElementById('user-info');
                    if (userInfoElement) {
                        userInfoElement.innerHTML = `Welcome  , ${responseData.user.username}`;
                    }
                } else {
                    const errorData = await response.json();
                    console.log('Fetch error:', errorData);
                    alert('Error: ' + errorData.message);
                }
            } catch (error) {
                console.log('Error:', error);
            }

            console.log("'Login button clicked!'");

        } else if (target.id === 'go-to-login') {
            renderView(renderLoginView);
        } else if (target.id === 'logout') {
            renderView(renderLoginView);
        } else if (target.id === 'intra-btn') {
            const email = document.getElementById('login-email').value;
            alert('Intra login');
        } else if (target.id === 'gmail-btn') {

                initializeGoogle()
                handleGoogleLogin();
 


         }
    });
});