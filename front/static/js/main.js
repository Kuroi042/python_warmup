
function initializeGoogle() {
    if (!window.google || !window.google.accounts) {
        console.error("Google API not loaded.");
        return;
    }


    window.google.accounts.id.initialize({
        client_id: '598064932608-hf8f5bd6aehru3fjegblkhqpge7fnubr.apps.googleusercontent.com',  // Replace with your actual client ID
        callback: handleGoogleLogin
    });

    window.google.accounts.id.renderButton(
        document.getElementById('gmail-btn'),  
         { theme: "outline", size: "Big" }            // Customize button appearance
    );

    window.google.accounts.id.prompt();   
}

 
function fetchSomeProtectedAPI(jwtToken) {
    console.log('token nnnn', jwtToken);  // Logs the token to the console for debugging
    const jwt = localStorage.getItem('jwtToken');

    fetch('http://localhost:8000/protected-api/', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${jwt}`  // Sends the token in the Authorization header
        }
    })
    .then(response => response.json())  // Parse the JSON response from the backend
    .then(data => console.log('Response from API:', data))  // Log the data from the API
    .catch(error => console.error("Error fetching protected API:", error));  // Handle errors
}



function handleGoogleLogin(response) {
    const id_token = response.credential;

    if (!id_token) {
        console.error('Google Auth error: Token not found');
        return;
    }

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
        if (data.message === "Loginn successful!") {
            console.log('fata',data); //data container the returned Json
            const user = data.user ;
            const jwtToken =  data.token;
            // console.log('hahowa token ' , jwtToken); // for token jwt
             const userName = user.name;
            const userEmail = user.email;
            const userPicture = user.picture;
            localStorage.setItem('jwtToken', jwtToken);   
            console.log('HEHEHEEH' ,user  );
            console.log('jwt token hhh', jwtToken);
            
            
            renderView(renderMainView);
            alert(`Welcome, ${userName}! Successfully logged in with Google!`);
            const profilePicElement = document.getElementById('profile-pic');
            if (profilePicElement && userPicture  ) {
                profilePicElement.src = userPicture;
            }
            const userInfoElement = document.getElementById('user-info');
            fetchSomeProtectedAPI(jwtToken);  
            userInfoElement.innerHTML = `Welcome Merhba , ${userName}`;
            
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
    initializeGoogle();  
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
                user: document.getElementById('login-user').value,
                password: document.getElementById('login-password').value,
            };
        
            try {
                const response = await fetch('http://localhost:8000/login-action/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data), // Send data directly
                });
        
                if (response.ok) {
                    const responseData = await response.json();
                    
                    console.log('Server response:', responseData.message);
                    alert('Account logged in successfully!');
                    
                    // Handle superuser redirect
                    if (responseData.redirect_url) {
                        alert('Redirecting to admin panel...');
                        window.location.href = responseData.redirect_url; // Redirect superuser to admin panel
                    } else {
                        // For regular users
                        alert(`Welcome, ${responseData.user.username}!`);
                        renderView(renderMainView);
        
                        const userInfoElement = document.getElementById('user-info');
                        if (userInfoElement) {
                            userInfoElement.innerHTML = `Welcome, ${responseData.user.username}`;
                        }
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
                // handleGoogleLogin(); no need
 


         }
    });
});