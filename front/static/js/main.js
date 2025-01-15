

// document.addEventListener('DOMContentLoaded', () => {
//   // Adding click event listener for the fetch button
//   document.getElementById('fetch-btn').addEventListener('click', async () => {
//       try {
//           // Making a GET request to the server
//           const response = await fetch('http://127.0.0.1:8000/button-action/', {
//               method: 'GET', // Use 'GET' method
//           });

//           // Checking if the request was successful
//           if (response.ok) {
//               const data = await response.json();  // Parsing the JSON response
//               console.log('Server Response:', data); // Logging the response data
//           } else {
//               console.error('Fetch error:', response.statusText); // If not ok, log the error
//           }
//       } catch (error) {
//           // Catching any network errors and logging them
//           console.error('Error:', error);
//       }
//   });
// });



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
      else if (target.id === 'login-btn') {
          console.log("'Login button clicked!'"); 
          
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
      
      } else if (target.id === 'go-to-login') {
          renderView(renderLoginView);
      } else if (target.id === 'logout') {
          renderView(renderLoginView); 
      } else if (target.id === 'intra-btn') {
          alert('Intra login');
      } else if (target.id === 'gmail-btn') {
          alert('Gmail login');
      }
  });
});