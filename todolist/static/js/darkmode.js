document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('darkModeToggle');
    if (btn) {
        btn.onclick = function () {
            document.body.classList.toggle('dark-mode');
            document.querySelectorAll('.card').forEach(e => e.classList.toggle('dark-mode'));
            document.querySelectorAll('.form-control').forEach(e => e.classList.toggle('dark-mode'));
            document.querySelectorAll('.btn').forEach(e => e.classList.toggle('dark-mode'));
            document.querySelectorAll('.list-group-item').forEach(e => e.classList.toggle('dark-mode'));
        };
    }
});
