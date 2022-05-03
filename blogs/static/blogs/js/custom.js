let images = document.querySelectorAll('.card-mg-top')
for(let img of images) {
	img.addEventListener('clic', () =>
		document.getElementById('exempleModal').querySelector('img').src = img.src)
}