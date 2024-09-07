function getIdeaImage(category){
    if (category === "errors"){
        return `<img src="/static/account/images/bugs/icobug_error.png" />`;
    }
    else if (category === "correction"){
        return `<img src="/static/account/images/bugs/icobug_fix.png" />`;
    }

    else if (category === "modernization"){
        return `<img src="/static/account/images/bugs/icobug_addon.png" />`;
    }
    else if (category === "new_feature"){
        return `<img src="/static/account/images/bugs/icobug_idea.png" />`;
    }
}

function renderIdeas(ideas){
    let ideasHTML = '';
    for (let idea of ideas){
        let ideaHTML = `
        <tr>
            <td style="width: 50px;" class="status">
                ${getIdeaImage(idea.category)}
            </td>

            <td style="width: 120px;">${ idea.created_at }</td>
            <td>
                <p>
                    ${ idea.title }
                </p>

                <div>
                    <p onclick="openIdeaDescription(this)" class="description hidden">
                        ${ idea.description }
                    </p>
                </div>
            </td>

            <td style="width: 120px;">${ idea.user }</td>
            <td style="width: 120px;">${ idea.status }</td>
            <td style="width: 120px;">${ idea.finishe_date }</td>

            <td style="width: 120px;">
                <div class="like">
                    <img onclick="addLike(this, {{idea.id}})" src="${idea.liked ? "/static/account/images/bugs/icobug_yes.png" : "/static/account/images/bugs/icobug_vote.png"}" />
                    <span>${ idea.likes }</span>
                </div>
            </td>
        </tr>
        `;

        ideasHTML += ideaHTML;
    }

    console.log(ideasHTML);

    document.querySelector("tbody").innerHTML = ideasHTML;
}


function loadIdeas(page=1){
    const category = $("select[name=category]").val();
    const status = $("select[name=status]").val();
    const page_size = $("select[name=page_size]").val();

    fetch(`/user/ideas?category=${category}&page_size=${page_size}&status=${status}&page=${page}`).then(response => {
        if (response.status === 200){
            response.json().then(response => {
                console.log(response);
                renderIdeas(response.ideas);
                console.log(response.total_pages);
                renderPagination(page, response.total_pages, 'loadIdeas');
                rememberIdeasFilters();
                changePaginationCount(response.count);
            })
        }
    })
}

function openIdeaForm(){
    createIdeaForm = document.querySelector(".create-idea-form");

    fetch(`/get-create-idea-form`).then(response => response.json()).then(response => {
        createIdeaForm.innerHTML = response.content;
        openForm(createIdeaForm);
        initCreateIdeaForm();
        addScreensLoadEvent();
    })
}

let createIdeaForm = document.querySelector(".create-idea-form");

function onSubmitCreateIdeaForm(element, event){
    event.preventDefault();

    const data = new FormData(element);
    let screens = [];

    for (let screen of element.querySelectorAll("input[type=file]")){
        console.log(screen)
        console.log(screen.files)
        if (screen.files[0] !== undefined){
            data.append('screens', screen.files[0])
        }
    }

    console.log(screens)

    fetch(`/user/idea`, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
        body: data
    }).then(response => {
        if (response.status === 201){
            setErrors({}, element)
            console.log("success");
            window.history.replaceState(null, '', window.location.pathname);
            location.reload();
        }
        if (response.status === 401){
            window.location.href="/user/login";
        }
        return response.json();
    }).then(response => {
        console.log(response.errors);
        console.log(element);
        setErrors({}, element)
        setErrors(response.errors, element)
    })
}

function initCreateIdeaForm(){
    createIdeaForm = document.querySelector(".create-idea-form");

    createIdeaForm.querySelector(".cross img").addEventListener('click', closeCreateProductForm);

    createIdeaForm.addEventListener('submit', event => onSubmitCreateIdeaForm(createIdeaForm, event))
}


function rememberIdeasFilters(){
    const url = new URL(window.location.href);

    const category = $("select[name=category]").val();
    url.searchParams.set('category', category);

    const page_size = $("select[name=page_size]").val();
    url.searchParams.set('page_size', page_size);

    const date = $("select[name=date]").val();
    url.searchParams.set('date', date);

    window.history.replaceState(null, '', window.location.pathname + url.search);
}

function addScreen(){
    const screensCount = document.querySelectorAll('.screens-container input[type=file]').length;

    let screen =
    `
    <div class="screen">
        <div class="screen-image">
            <img src="/static/account/images/noscreen.jpg" alt="скриншот">
            <input name="file" type="file" accept="image/*" id="file${screensCount + 1}" multiple/>
        </div>
    </div>

    <button onclick="addScreen()" class="br50">+</button>
    `;

    const screenContainer = createIdeaForm.querySelector(".screens-container");
    const button = screenContainer.querySelector("button");
    screenContainer.removeChild(button);
    screenElem = document.createElement('div');
    screenContainer.appendChild(screenElem);
    screenElem.outerHTML = screen;

    screenContainer.scrollLeft = screenContainer.scrollWidth;

    addScreensLoadEvent();
}

function addScreensLoadEvent(){
    const screens = createIdeaForm.querySelectorAll(".screen");

    screens.forEach(screen => {
        const screenLoader = screen.querySelector("input[type=file]");
        screenLoader.addEventListener("change", () => displayPhotoOnload(screen));
    })
}

function openIdeaDescription(element){
    element.classList.remove("hidden")

    element.style.cursor = 'auto';
    const a = document.createElement("a");

    element.parentElement.appendChild(a);
    a.outerHTML = `<a style="color: var(--light-ref-color); cursor: pointer;">скрыть</a>`
    element.parentElement.querySelector("a").addEventListener('click', () => hideIdeaDescription(element.parentElement))
    element.removeEventListener('click', openIdeaDescription);
}

function hideIdeaDescription(element){
    element.querySelector(".description").classList.toggle("hidden");

    element.querySelector(".description").style.cursor = "pointer";

    const a = element.querySelector("a")
    element.removeChild(a);
}

function addLike(element, ideaId){
    console.log(element.src.split("/")[element.src.split("/").length - 1]);
    if (element.src.split("/")[element.src.split("/").length - 1] === "icobug_vote.png"){
        fetch(`/user/like?idea=${ideaId}`, {method: "POST"}).then(response => {
            if (response.status === 201){
                element.src = "/static/account/images/bugs/icobug_yes.png";
                element.parentElement.querySelector("span").innerHTML = Number(element.parentElement.querySelector("span").innerHTML) + 1
            }
        })
    }
    else{
        fetch(`/user/like?idea=${ideaId}`, {method: "DELETE"}).then(response => {
            if (response.status === 204){
                element.src = "/static/account/images/bugs/icobug_vote.png";
                element.parentElement.querySelector("span").innerHTML = Number(element.parentElement.querySelector("span").innerHTML) - 1
            }
        })
    }
}

function initIdeas(){
    if (document.querySelector("select[name=category") != null){
        document.querySelector("select[name=category").addEventListener("change", () => loadIdeas());
        document.querySelector("select[name=status").addEventListener("change", () => loadIdeas());
        document.querySelector("select[name=page_size]").addEventListener("change", () => loadUser());
    }
}
