import { Api as api } from "./api/apiMain.js"



// console.log(await api.getSkills("ivashka"))
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('testButton').addEventListener('click', testApi);
});

function testApi() {
    let data = api.getSkills("ivashka")
    for (let key in data) {
        alert(key)
    }
}