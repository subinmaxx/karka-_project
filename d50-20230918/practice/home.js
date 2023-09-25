
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
                const row = document.createElement('tr');
                row.innerHTML = 
                    `<td>${i.id}</td>
                    <td>${i.title}</td>
                    <td><img src="${i.images[0]}" alt="Product Image" width="50"></td>
                    <td>${i.description}</td>
                    <td>${i.price}</td>
                    <td><button onclick="show_details(${i.id})" class= "btn btn-dark">click here</button></td>`
                    
                    ;
                    kunush.appendChild(row);

            }
        }
        
        )

    
