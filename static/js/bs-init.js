
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
  	const id = button.getAttribute('data-bs-id')
  	// If necessary, you could initiate an AJAX request here
  	// and then do the updating in a callback.
	  const url = `http://localhost:8000/modal_content/${id}`
	  fetch(url)
	  .then(res => {
		return res.json();
	  })
	  .then(data => {
		const modalBody = staticBackdrop.querySelector('.modal-body')
		const modalFooter = staticBackdrop.querySelector('.modal-footer')

		modalBody.innerHTML = `<div class="row row-cols-md-2 align-items-center mt-2">
							<div class="col offset-3">
		  						<div class="text-center"><img class="mb-1" src="${data.image}" width="250" height="250">
			  						<p class="fs-5 fw-semibold text-primary mb-2">${data.name}</p>
		  						</div>
	  						</div>
  						</div>`
						  modalFooter.innerHTML = `<button class="btn btn-danger" type="button" data-bs-dismiss="modal">
						  <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" class="bi bi-x-square">
							  <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"></path>
							  <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"></path>
						  </svg>&nbsp;Cancel
					  </button>
					  <a href="${data.link}">
						  <button class="btn btn-success" type="link">
							  <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" class="bi bi-check-square">
								  <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"></path>
								  <path d="M10.97 4.97a.75.75 0 0 1 1.071 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.235.235 0 0 1 .02-.022z"></path>
							  </svg>&nbsp;Confirm
						  </button>
					  </a>`

	  })
})
}, false);
