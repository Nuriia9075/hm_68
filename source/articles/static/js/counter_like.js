async function makeRequest(url, method = "GET") {
    let response = await fetch(url, { method: method })
    if (response.ok) {
        return await response.json();
    } else {
        let error = await response.json();
        // throw new Error("Возникла ошибка",error.message);
        let p = document.createElement('p');
        p.innerText = "Возникла ошибка";
        p.style.color = 'red';
        container.appendChild(p);
    }
}

async function onClick(event) {
    event.preventDefault();
    let link = event.currentTarget; // Гарантирует получение ссылки <a>
    let counterId = link.dataset.counterId;
    let counter = document.getElementById(counterId);
    let url = link.href;
    let response = await makeRequest(url);
    console.log(response);
    if (response && response.likes) {
        if (response.likes === "unlike") {
            link.innerText = "Поставить лайк";
            if (counter) counter.innerText = parseInt(counter.innerText || 0) - 1;
        } else if (response.likes === "like") {
            link.innerText = "Убрать лайк";
            if (counter) counter.innerText = parseInt(counter.innerText || 0) + 1;
        }
    }
}

function onLoad() {
    let links = document.querySelectorAll('[data-key="likes"]');
    for (let link of links){
       link.addEventListener('click', onClick);
    }
}
window.addEventListener("load", onLoad);