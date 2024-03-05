document.addEventListener('DOMContentLoaded', function() {
    let mouseDown = false;

    document.body.addEventListener('mousedown', () => {
        mouseDown = true;
    });

    document.body.addEventListener('mouseup', () => {
        mouseDown = false;
    });

    document.body.addEventListener('focusin', (e) => {
        if (mouseDown) {
            e.target.classList.remove('focus-visible');
        } else {
            e.target.classList.add('focus-visible');
        }
    });

    document.body.addEventListener('focusout', (e) => {
        e.target.classList.remove('focus-visible');
    });
});