const show_modal = document.getElementById('test');
const modal = document.getElementById('modal')

show_modal.addEventListener("click", () => {
    modal.classList.remove('hidden')
});