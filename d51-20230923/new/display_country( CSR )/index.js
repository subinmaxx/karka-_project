let data = [];

$.get('index.txt',(val)=>{
    data.push(JSON.parse(val));
    console.log(data);
})

$('.country button').click(()=>{

    let countries = data[0].countries;

   $('.country ul').html(' ');

    for(let i=0;i<countries.length;i++){

        $('.country ul').append(`<li class='dropdown-item btn' onclick='getCountry(${i})'>${countries[i].countryName}</li>`)
    }
})
function getCountry(index){

    $('.state ul').html('');

    let states = data[0].countries[index].states;

    for(let i=0;i<states.length;i++){

        $('.state ul').append(`<li class='btn dropdown-item' onclick='getState(${i},${index})'>${states[i].stateName}</li>`)
    }

    $('.country-res').html(data[0].countries[index].countryName)
}
function getState(state_id,country_id){
    
    $('#district').html('');

    let district = data[0].countries[country_id].states[state_id].districts;

    for( i of district){

        $('#district').append(`<li class='dropdown-item btn'>${i}</li>`)
    }
    $('.state-res').html(data[0].countries[country_id].states[state_id].stateName)
}
