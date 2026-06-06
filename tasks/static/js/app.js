const open_modal = document.getElementById('open_modal_create');
const close_modal = document.getElementById('close_modal_create')
const modal_overlay = document.getElementById('modal-overlay');


open_modal.addEventListener("click", () => {
    modal_overlay.classList.add('active');
});

close_modal.addEventListener("click", () => {
    modal_overlay.classList.remove("active")
});