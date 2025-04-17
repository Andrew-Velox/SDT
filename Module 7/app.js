// // alert();

// const get = document.getElementsByTagName("h1");

// const gg = document.getElementById("ck");


// console.log(get[0]);


// for(x=0; x<get.length; x++){
//     get[x].style.color="red";
// }
// ck.style.color="green";


const get = document.getElementsByClassName("box");
console.log(get);

for(x=0; x<get.length; x++){
    if(x%2) get[x].style.backgroundColor="green";

    if(get[x].innerText=="box 6") get[x].style.backgroundColor="red";
}


document.getElementById("btnn").addEventListener("click",(e) =>{
    const val=document.getElementById("inpt").value;
    // console.log("hello");
    // console.log(val);

    const gg=document.getElementById("add_con");

    
    const p = document.createElement("p");
    p.className="child";


    p.innerText=val;

    // console.log(p);

    gg.appendChild(p);


    document.getElementById("inpt").value="";



    const get_child= document.getElementsByClassName("child");


    console.log(get_child);

    for(const itms of get_child){
        itms.addEventListener("click",(e) =>{
            e.target.parentNode.removeChild(itms);

        })
    }




} );


// const fnd = (e) =>{ // using onclick 
//     console.log("smashed!!!!");
// }



fetch("https://jsonplaceholder.typicode.com/users").then(res => res.json()).then( data=>{

    displayData(data);
    // console.log(data);

    // for(const itm of data){
    //     console.log(itm.name);
    // }
}).catch(err=>{
    console.log(err);
});


const displayData = (userData) => {

    console.log(userData);

    const usr_dataPrint=document.getElementById("usr_data"); 
    for(const itms of userData){

        const div=document.createElement("div");
        div.className="datas";
        div.innerHTML=`
            <p><b>Id:</b> ${itms.id}</p>
            <p><b>Name:</b> ${itms.name} </p>
            <p><b>Username:</b> ${itms.username} </p>
            <p><b>Number:</b> ${itms.phone} </p>
        `;

        usr_dataPrint.appendChild(div);
        // const p=document.createElement("p");
        // p.className="names";
        // p.innerText=itms.name;
        // div.h3.innerText(itms.name);


        // usr_dataPrint.appendChild(p);

        // const h1=document.createElement("h1");
        // h1.className="ids";
        // h1.innerText=itms.id;
        // usr_dataPrint.appendChild(h1);
    }

}

