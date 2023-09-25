
    function handle_load(){
        // r-data ead local JSON file in javascript
        json_data = fetch('https://dummyjson.com/products')
        .then(res => res.json())
        .then(json => {return json})
        return json_data
        }

        handle_load()
        .then((jsonData) => {


            console.log("json",jsonData)
            for(i of jsonData.products){
                // console.log(i.title)
                let body=document.getElementById("kunush");
                let row=document.createElement("tr");
                let col1=document.createElement("td");
                let col2=document.createElement("td")
                let col3=document.createElement("td");


                col1.innerText=i.title
                col2.innerText=i.description
                col3.innerText=i.price
                row.appendChild(col1)
                row.appendChild(col2)

                row.appendChild(col3)
                body.appendChild(row)
            }
        }
        )
    
