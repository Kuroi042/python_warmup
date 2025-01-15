



function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return null;
}

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
        try {
            const response = await fetch('http://localhost:8000/get-csrf-token/', {
                credentials: 'include'  // Important! This enables cookies
            });
            if (!response.ok) {
                console.error('Failed to get CSRF token');
            }
        } catch (error) {
            console.error('Error fetching CSRF token:', error);
        }

        const target = event.target;
        if (target.id === 'go-to-signup') {
            console.log("'signup button clicked!'");
            renderView(renderSignupView);
        }
        else if (target.id === 'register'){
            console.log("'register button clicked!'");
            const csrfToken = getCSRFToken();
            if (csrfToken) {
                document.getElementById('csrf-token').value = csrfToken; // Set token to hidden input
            }  
            else
                console.log('scsrffffffv not found');
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
                        'X-CSRFToken': csrfToken,  // Make sure the CSRF token is included
                    },
                    credentials: 'include',
                    body: JSON.stringify(data),  // Send data directly
                });
                if (response.status != 500) {
                    response.json().then(res=>{
                        console.log(res)
                    })
                }
                if (response.ok) {
                    const responseData = await response.json();
                    console.log('Server response', responseData.message);
                } else {
                    console.log('Fetch error:', response.statusText);
                }
            } catch (error) {
                console.log('Error:', error);
            }
        }

        else if (target.id === 'login-btn') {
            console.log("'Login button clicked!'");



        } else if (target.id === 'go-to-login') {
            renderView(renderLoginView);
        } else if (target.id === 'logout') {
            renderView(renderLoginView);
        } else if (target.id === 'intra-btn') {
            const email = document.getElementById('login-email').value;
            console.log('Email entered:', email);
            const response = await fetch('http://localhost:8000/button-action/', {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data.message);
            } else {
                console.log('Fetch error:', response.status);
            }
            alert('Intra login');
        } else if (target.id === 'gmail-btn') {
            alert('Gmail login');
        }
    });
});