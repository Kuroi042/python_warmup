function renderView(viewFunction) {
  const container = document.getElementById('view-container');
  container.innerHTML = viewFunction();
  container.classList.add('active');  
}

document.addEventListener('DOMContentLoaded', () => {
 
  renderView(renderLoginView);

 
  document.addEventListener('click', (event) => {
      if (event.target.id === 'go-to-signup') {
        renderView(renderSignupView);
      } 
      else if (event.target.id === 'go-to-login') {

          renderView(renderLoginView);
      } else if (event.target.id === 'logout') {
          renderView(renderLoginView);
      }
      else if(event.target.id === 'intra-btn')
          alert('intra login');
          else if(event.target.id === 'gmail-btn')
          alert('gmail login');
      
  });
}); 