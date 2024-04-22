document.addEventListener("DOMContentLoaded", function() {
    fetch("/color-styles/backgroundcolor").
    then(response => response.json()).
    then(response => {
        document.documentElement.style.setProperty("--background-color", response)
    })

    fetch("/color-styles/maincolor").
    then(response => response.json()).
    then(response => {
        document.documentElement.style.setProperty("--main-color", response)
    })

    fetch("/color-styles/secondarycolor").
    then(response => response.json()).
    then(response => {
        document.documentElement.style.setProperty("--secondary-color", response)
    })

    fetch("/text-styles/header").
    then(response => response.json()).
    then(response => {
        //console.log(response);
        document.documentElement.style.setProperty("--header-color", response.color)
        document.documentElement.style.setProperty("--header-inverted-color", response.fontColorInverted)
        document.documentElement.style.setProperty("--header-font", response.font)
        document.documentElement.style.setProperty("--header-font-weight", response.fontWeight)
        document.documentElement.style.setProperty("--header-font-weight-mobile", response.fontWeightMobile)
        document.documentElement.style.setProperty("--header-font-size", response.fontSize)
        document.documentElement.style.setProperty("--header-font-size-mobile", response.fontSizeMobile)
    })

    fetch("/text-styles/main-text").
    then(response => response.json()).
    then(response => {
        //console.log(response);
        document.documentElement.style.setProperty("--main-text-color", response.color)
        document.documentElement.style.setProperty("--main-text-inverted-color", response.fontColorInverted)
        document.documentElement.style.setProperty("--main-text-font", response.font)
        document.documentElement.style.setProperty("--main-text-font-weight", response.fontWeight)
        document.documentElement.style.setProperty("--main-text-font-weight-mobile", response.fontWeightMobile)
        document.documentElement.style.setProperty("--main-text-font-size", response.fontSize)
        document.documentElement.style.setProperty("--main-text-font-size-mobile", response.fontSizeMobile)
    })

    fetch("/text-styles/subheader").
    then(response => response.json()).
    then(response => {
        //console.log(response);
        document.documentElement.style.setProperty("--subheader-color", response.color)
        document.documentElement.style.setProperty("--subheader-inverted-color", response.fontColorInverted)
        document.documentElement.style.setProperty("--subheader-font", response.font)
        document.documentElement.style.setProperty("--subheader-font-weight", response.fontWeight)
        document.documentElement.style.setProperty("--subheader-font-weight-mobile", response.fontWeightMobile)
        document.documentElement.style.setProperty("--subheader-font-size", response.fontSize)
        document.documentElement.style.setProperty("--subheader-font-size-mobile", response.fontSizeMobile)
    })

    fetch("/text-styles/explanation-text").
    then(response => response.json()).
    then(response => {
        //console.log(response);
        document.documentElement.style.setProperty("--explanation-text-color", response.color)
        document.documentElement.style.setProperty("--explanation-text-inverted-color", response.fontColorInverted)
        document.documentElement.style.setProperty("--explanation-text-font", response.font)
        document.documentElement.style.setProperty("--explanation-text-font-weight", response.fontWeight)
        document.documentElement.style.setProperty("--explanation-text-font-weight-mobile", response.fontWeightMobile)
        document.documentElement.style.setProperty("--explanation-text-font-size", response.fontSize)
        document.documentElement.style.setProperty("--explanation-text-font-size-mobile", response.fontSizeMobile)
    })

    fetch("/styles/margin-block").
    then(response => response.json()).
    then(response => {
        //console.log(response);
        document.documentElement.style.setProperty("--padding-block-top", response.top)
        document.documentElement.style.setProperty("--padding-block-bottom", response.bottom)
    })

    fetch("/styles/icon-size").
    then(response => response.json()).
    then(response => {
        //console.log(response);
        document.documentElement.style.setProperty("--icon-width", response.width)
        document.documentElement.style.setProperty("--icon-height", response.height)
    })
});