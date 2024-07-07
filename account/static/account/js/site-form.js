const range = document.querySelector("input[type=range]");

function changeLogoSize(){
    console.log(range.value);

    newLogoWidth = 260 * (range.value / 100);

    const image = document.querySelector("#logo img");
    image.style.width = newLogoWidth;
}

range.addEventListener("input", changeLogoSize)

const logo = document.querySelector("#logo")
const logoLoader = logo.querySelector("#file");

function displayLogo() {
    const file = logoLoader.files[0];
    const reader  = new FileReader();

    reader.onload = function(e)  {
        const image = logo.querySelector("img");
        image.src = e.target.result;
    }

    reader.readAsDataURL(file);
}

logoLoader.addEventListener("change", displayLogo)

function onSubmitSiteForm(element, event){
    event.preventDefault();

    const data = new FormData(element);
    data.append('logo', document.getElementById("file").files[0])

    const socialContainers = element.querySelector("#socials").querySelectorAll(".field-container");

    let socials = [];

    console.log(socialContainers)
    for (let socialContainer of socialContainers){
        console.log(socialContainer);
        let social = socialContainer.querySelector(".social").querySelector("select").value;
        let adress = socialContainer.querySelector("input[name=adress]").value;

        console.log(social, adress);

        if (social.length > 0 && adress.length > 0){
            socials.push({social: social, adress: adress});
        }
    }
    const token = getToken();

    console.log(socials);
    data.append("socials", JSON.stringify(socials));
    console.log(data);

    fetch(`http://localhost:8000/my/change-site`, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': `${token}`,
        },
        body: data
    }).then(response => {
        if (response.status === 200){
            setErrors({}, element)
            console.log("success");
            location.reload();
        }
        return response.json();
    }).then(response => {
        setErrors({}, element)
        setErrors(response.errors, element)
    })
}

const socials = document.querySelector("#socials")
const socialAdresses = socials.querySelectorAll("input[name=adress]")

function getSocialOptions(){
    let socialOptions = document.querySelector("#socials").querySelector("select").querySelectorAll("option")
    console.log(socialOptions);
    let socialValues = [""];
    let socialTexts = ["Выбрать"];

    for (let socialOption of socialOptions){
        if (socialOption.value.length > 0){
            socialValues.push(socialOption.value);
            socialTexts.push(socialOption.innerText);
        }
    }

    console.log(socialValues);
    console.log(socialTexts);

    let options = '';

    for (let i = 0; i < socialValues.length; i++){
        options += `<option value="${socialValues[i]}">${socialTexts[i]}</option>`;
    }

    return options
}

function createNewSocial(){
    const options = getSocialOptions()

    const newSocial = document.createElement("div")
    newSocial.classList.add("field-container");
    newSocial.innerHTML = `
    <div class="field social">
        <p>Соцсеть</p>
        <select name="" id="">
            ${options}
        </select>
    </div>

    <div class="field adress">
        <p>Адрес</p>
        <input name="adress" />
    </div>

    <div class="trash-container">
        <img class="trash" onclick="deleteSocial(this)" src="/static/account/images/trash.png"/>
    </div>
    `

    return newSocial;
}

function observableNewSocials(){
    const socials = document.querySelector("#socials");
    const socialAdresses = socials.querySelectorAll("input[name=adress]");

    for (let input of socialAdresses){
        input.addEventListener("change", () => {
            const socialsCount = document.querySelector("#socials").querySelectorAll("input[name=adress]").length;
            const currIndex = [...socialAdresses].indexOf(input)

            if (currIndex === socialsCount - 1 && socialsCount < 4){
                const newSocial = createNewSocial();

                socials.appendChild(newSocial);
                observableNewSocials();
            }
        });
    }
}

observableNewSocials();

function deleteSocial(element){
    const newSocial = createNewSocial();

    const socials = document.querySelector("#socials");
    const trashes = socials.querySelectorAll(".trash");

    const currentIndex = [...trashes].indexOf(element);
    console.log(currentIndex);

    const social = socials.querySelectorAll(".field-container")[currentIndex];
    social.remove();

    if (trashes.length === 1){
        socials.appendChild(newSocial);
        observableNewSocials();
    }
}
