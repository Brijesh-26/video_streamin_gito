const menu = document.querySelector("#menu")
const dropDown = document.querySelector("#drop-down")
const sidebar = document.querySelector(".sidebar")
const drop_down = document.querySelector(".dropdown-content-background")
console.log("start")
console.log(`this is first ${sidebar}`);
console.log(`this is asli dropdown ${dropDown}`)

menu.addEventListener("click", function(){
    sidebar.classList.toggle("show-sidebar")
})

dropDown.addEventListener("click", function(){
    console.log("pressed")
    // dropDown.classList.toggle("show-dropdown")
    dropDown.classList.replace('material-icons display-this', 'dropdown-content-background')
})



function titleValidate(){
    let errorDiv = document.getElementById("error-div")
    let title_input = document.getElementById("title")
    let count = document.getElementById("count")
    let errors = []

    let title = title_input.value
    console.log(title.length);
    
    count.innerHTML = `${title.length}/100`
    

    if (title.length > 100) {
        errors.push("You have exceeded the max length for title")
        title_input.style.color = "red"
    } else{
        title_input.style.color = "black"
    }

    if (errors.length > 0) {
        errorDiv.innerHTML = errors.join('');

        return false;
    }
    errorDiv.innerHTML = errors.join('');
    return true;
}




function desc_validate(){
  let errorDiv = document.getElementById("desc-error-div")
  let title_input = document.getElementById("description")
  let count = document.getElementById("desc-count")
  let errors = []

  let title = title_input.value
  console.log(title.length);
  
  count.innerHTML = `${title.length}/5000`
  

  if (title.length > 5000) {
      errors.push("You have exceeded the max length for title")
      title_input.style.color = "red"
  } else{
      title_input.style.color = "black"
  }

  if (errors.length > 0) {
      errorDiv.innerHTML = errors.join('');

      return false;
  }
  errorDiv.innerHTML = errors.join('');
  return true;
}







var inputs = document.querySelectorAll('#file-input')

for (var i = 0, len = inputs.length; i < len; i++) {
  customInput(inputs[i])
}

function customInput (el) {
  const fileInput = el.querySelector('[type="file"]')
  const label = el.querySelector('[data-js-label]')
  
  fileInput.onchange =
  fileInput.onmouseout = function () {
    if (!fileInput.value) return
    
    var value = fileInput.value.replace(/^.*[\\\/]/, '')
    el.className += ' -chosen'
    label.innerText = value
  }
}