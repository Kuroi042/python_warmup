



// function getCSRFToken() {
//     const cookies = document.cookie.split(';');
//     for (let cookie of cookies) {
//         const [name, value] = cookie.trim().split('=');
//         if (name === 'csrftoken') {
//             return value;
//         }
//     }
//     return null;
// }
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
        else if (target.id === 'register'){
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
                    alert('Account created successfully! Redirecting to login page...');
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
                    const userInfoElement =document.getElementById('user-info');
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
            alert('Gmail login');
        }
    });
});