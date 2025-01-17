function renderMainView() {
    return `
        <h2 id="user-info">Welcome</h2> 
        <p>You are logged in!</p>
        <button id="logout">Logout</button>
        <div id="user-info"></div>
        <img id="profile-pic" src="" alt="Profile Picture" />
    `;
}
window.renderMainView = renderMainView;
