function on_load(){

$.getJSON('https://dummyjson.com/products', function (data) {
    console.log("json",data);
    document.getElementById("ids").innerText=data.products[0].id;
    document.getElementById("tittle").innerText=data.products[0].title;
    document.getElementById("dis").innerText=data.products[0].description;
    document.getElementById("price").innerText=data.products[0].price;
    document.getElementById("discount").innerText=data.products[0].discountPercentage;
    document.getElementById("rating").innerText=data.products[0].rating;
    document.getElementById("stock").innerText=data.products[0].stock;
    document.getElementById("brand").innerText=data.products[0].brand;
    document.getElementById("category").innerText=data.products[0].category;

//    for (i of data.products){
//     console.log(i)
   }
    
)}
