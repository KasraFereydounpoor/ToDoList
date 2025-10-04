document.addEventListener("DOMContentLoaded", function () {
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
    }
    const btn = document.getElementById("darkModeToggle");
    if (btn) {
        btn.addEventListener("click", function () {
            document.body.classList.toggle("dark-mode");
            if(document.body.classList.contains("dark-mode")){
                localStorage.setItem('darkMode', 'enabled');
            } else {
                localStorage.setItem('darkMode', 'disabled');
            }
        });
    }
});
