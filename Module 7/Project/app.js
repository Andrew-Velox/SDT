

const allProd = () =>{
    fetch("https://fakestoreapi.com/products").then(res => res.json()).then(data=>{

        console.log(data);

        displayProd(data);

    }).catch((e)=> console.log(e))
    
    ;
}

allProd();

const displayProd = (product) => {


    const prod_disp=document.getElementById("product_sec");
    for(const itms of product){

        const div=document.createElement("div");
        div.classList.add("card");
        div.innerHTML=`
            <img class="itms_img" src= ${itms.image}> </img>
            <p> <b>ID: </b> ${itms.id} </p>
            <p> <b>Title: </b> ${itms.title.slice(0,10)} </p>
            <p> <b>Price: </b> ${itms.price} </p>
            <p> <b>Description: </b> ${itms.description.slice(0,20)} </p>
            <button onclick="addingToCart('${itms.image}', '${itms.id}', '${itms.title}','${itms.price}')"> Add to Cart </button>
            `;

        prod_disp.appendChild(div);
        // console.log(itms.title);
    }

}


var total_price=0;


const addingToCart = (image,id,title,price) => {
    console.log(title,price);
    const get_cart=document.getElementById("main-cart-itms");

    const div=document.createElement("div");
    div.classList.add("cart_itms");

    // <img class="itms_img" src= ${image}> </img>
    // <p> <b>ID: </b> ${id} </p>
    div.innerHTML=`
        <p> <b>Title: </b> ${title.slice(0,10)} </p>
        <p> <b>Price: </b> ${price} </p>
    `;

    let n=Math.floor(parseFloat(price));
    total_price+=n;

    console.log(typeof(price), typeof(total_price));
    console.log(total_price);

    get_cart.appendChild(div);



    const get_tot_id=document.getElementById("tot-prc");

    console.log(get_tot_id);

    get_tot_id.innerText="Total: "+ total_price;
}