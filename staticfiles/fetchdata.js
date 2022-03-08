/////////////////////////////////FUNCTIONS///////////////////////////////////////////
function setFunctions(name){
    $('#functions-list').append(` <li class="nav-item">
    <a class="nav-link  {% if item.id == active %} active {% endif %}" aria-current="page" href=""  style="padding-right:30px;">${name}</a>
  </li>`);
}

function getfunctions(){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/api/functions",
        "method": "GET",

    }

    $.ajax(settings).done(function (response) {
        store.dispatch({ type: 'FUNCTIONS', data:response.functions })
        var array = store.getState()['Functions']
        // console.log(array);
        array.forEach(element => {
            setFunctions(element.function_name)
        });
              
    });
}
/////////////////////////////////FUNCTIONS///////////////////////////////////////////



/////////////////////////////////SUBCATEGORY///////////////////////////////////////////
function setSubcategory(subcategory){
    $('#sybcat').empty()
        $('#main-question').empty()
        $('#sybcat').append(`<h5 class="col-12 text-center " style="color: #e85500;">${subcategory.subcategory_name}</h5>`);
        $('#main-question').append(`<p class="col-12 text-center" style="color:#e85500; font-Size:20px;">${subcategory.subcategory_details}<i class="fas fa-question-circle"></i></p>`);
}

/////////////////////////////////SUBCATEGORY///////////////////////////////////////////

/////////////////////////////////SUBCATEGORY///////////////////////////////////////////
function setQuestions(questions,question_index=0){
    $('#ajax_updated').empty()
            $('#your_level').empty()
            $('#your_level').append(`<h2 class="col-12 text-center">What is your ${questions.Options[question_index].level_name}?</h2>`);
}

/////////////////////////////////SUBCATEGORY///////////////////////////////////////////


/////////////////////////////////OPTIONS///////////////////////////////////////////
function setOptions(options,option_index=0){
//     $('#ajax_updated').append(`<div class="col-xl-3  col-md-4 row mt-2 d-flex justify-content-center">
//     <div class="col-12  d-flex justify-content-center align-items-center"><h1 style="color:#e85500">90%</h1></div>
//      <div id="${options}" class="row option d-flex justify-content-center" onclick=""  style="background:#e85500;color:white" name="opts"><span class="col-8 d-flex justify-content-center" >${options}</span> <i class="d-flex justify-content-center col-2 fas fa-info-circle info-icon "></i></div>
//  </div>`);

options[option_index].option.forEach(element => {
    $('#ajax_updated').append(`<div class="col-xl-3  col-md-4 row mt-2 d-flex justify-content-center">
   <div id="${element}" class="row option d-flex justify-content-center" onclick="selected(this)" name="opts"><span class="col-8 d-flex justify-content-center" >${element.option}</span> <i class="d-flex justify-content-center col-2 fas fa-info-circle info-icon "></i></div>
   </div>`);
});
   
}

/////////////////////////////////OPTIONS///////////////////////////////////////////



function fetchingData() {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/api/data",
        "method": "GET",
    }

    $.ajax(settings).done(function (response) {
        store.dispatch({ type: 'DATA', data:response })
        setter();
    });
}
index=0;
option_index=0;
question_index=0;
function setter(index=0){
        store.dispatch({ type: 'SETTERINDEX', data:index })
        var array = store.getState()['Data']
        setSubcategory(array.questions[index])
        setQuestions(array.questions[index],question_index)
        setOptions(array.questions[index].Options, option_index)
        $(".box").hide();
        $("#next").show()
        $("#prev").show()
}


//report
