
if (window.innerWidth < 768) {
	[].slice.call(document.querySelectorAll('[data-bss-disabled-mobile]')).forEach(function (elem) {
		elem.classList.remove('animated');
		elem.removeAttribute('data-bss-hover-animate');
		elem.removeAttribute('data-aos');
		elem.removeAttribute('data-bss-parallax-bg');
		elem.removeAttribute('data-bss-scroll-zoom');
	});
}

document.addEventListener('DOMContentLoaded', function() {
	const staticBackdrop = document.getElementById('staticBackdrop')
	staticBackdrop.addEventListener('show.bs.modal', event => {
  	// Button that triggered the modal
  	const button = event.relatedTarget
  	// Extract info from data-bs-* attributes
  	const recipient = button.getAttribute('data-bs-whatever')
  	// If necessary, you could initiate an AJAX request here
  	// and then do the updating in a callback.
  	//

	
  	// Update the modal's content.
  	const modalTitle = exampleModal.querySelector('.modal-title')
  	const modalBodyInput = exampleModal.querySelector('.modal-body input')

  	modalTitle.textContent = `New message to ${recipient}`
  	modalBodyInput.value = recipient
})
}, false);
