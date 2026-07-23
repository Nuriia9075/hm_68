async function makeRequest(url, method = "POST", body=null) {
    let options = {
        method: method,
        headers: { 'Content-Type': 'application/json' }
    };
    if (body) options.body = JSON.stringify(body);
    let response = await fetch(url, options);
    return await response.json();
}
async function onClick(event) {
    event.preventDefault();
    let numA = document.getElementById('num_A')
    let numB = document.getElementById('num_B')
    let result=document.getElementById('result-output')
    let url = '/calculator' + event.target.dataset.key;
    let numbers = { "A": parseFloat(numA.value), "B": parseFloat(numB.value) };
    let response = await makeRequest(url, "POST", numbers);
    if (response && response.answer !== undefined) {
        result.innerText = response.answer;
        result.style.color = 'green';
        } else {
         result.innerText = (response && response.error) ? response.error : "Ошибка запроса";
         result.style.color = 'red';}
}
function onLoad() {
    let links = document.querySelectorAll('.calc-btn');
    for (let link of links){
       link.addEventListener('click', onClick);
    }
}
window.addEventListener("load", onLoad);