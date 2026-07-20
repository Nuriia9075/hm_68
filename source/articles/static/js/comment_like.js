async function makeRequest(url, method = "GET") {
    let response = await fetch(url, { method: method });
    if (response.ok) {
        return await response.json();
    } else {
        return null;
    }
}
async function onClick(event) {
    event.preventDefault();
    let link = event.currentTarget;
    let counterId = link.dataset.counterId;
    let counter = document.getElementById(counterId);
    let url = link.href;
    let response = await makeRequest(url);
    console.log( response);
    if (response && response.like) {
        if (response.like === "like") {
            link.innerText = "🩶 Убрать";
        } else if (response.like === "unlike") {
            link.innerText = "❤️ Like";
        }
        if (counter && response.count !== undefined) {
            counter.innerText = response.count;
        }
    }
}
function onLoad() {
    let links = document.querySelectorAll('[data-key="comment-likes"]');
    for (let link of links){
       link.addEventListener('click', onClick);
    }
}
window.addEventListener("load", onLoad);
