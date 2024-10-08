function stopSite(element){
    const token = getToken();

    fetch(`/domain/stop`, {
        method: "get",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': `${token}`
        }
    }).then(respose => {
        if (respose.status === 200){
            console.log("success");
            element.innerHTML = "возобновить"
            $(element).attr("onclick", "activateSite(this)");
        }
    })
}

function activateSite(element){
    const token = getToken();

    fetch(`/domain/activate`, {
        method: "get",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': `${token}`
        }
    }).then(respose => {
        if (respose.status === 200){
            element.innerHTML = "остановить"
            $(element).attr("onclick", "stopSite(this)");
        }
    })
}

let siteForm = document.querySelector(".site-form");
let socialsForm = document.querySelector(".socials-form");

function openSiteForm(){
    siteForm = document.querySelector(".site-form");

    fetch(`/get-change-site-form`).then(response => response.json()).then(response => {
        siteForm.innerHTML = response.content;
        initChangeSiteForm();
        openForm(siteForm);
    })
}

const openSiteFormButton = document.querySelector("#open-site-form");
if (openSiteFormButton != null){
    openSiteFormButton.addEventListener("click", () => openSiteForm());
}
