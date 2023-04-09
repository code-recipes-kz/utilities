const containers = document.querySelectorAll('div[data-title]');
let data = [];

containers.forEach(item => {
	const tags = [...item.querySelectorAll('div.keyword-tag > a')];

	const elem = {
		label: item.getAttribute('data-title'),
		tags: tags.map(item => item.innerText),
	};

	data.push(elem);
});