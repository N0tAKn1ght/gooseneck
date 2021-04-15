//Stores members info
var members = [{name:"Gabe",img:"../resources/img/OC_Shaded_Transparent_1_1.png", alt:"img of G", major: "Computer Science", year:"Sophmore", info: "Undefeated Smash Bros God from the Quad"}, 
                {name:"Kevin",img:"../resources/img/boo_1.png", alt:"img of K", major: "Computer Science", year:"Sophmore", info: "Bilingual in Spanish and English"}, 
                {name:"Tien",img:"../resources/img/Commision_Space_Boi_1.png", alt:"img of T", major: "Computer Science", year:"Sophmore", info: "Bilingual in English and Vietnamese"}, 
                {name:"Darian",img:"../resources/img/yeetus_deletus_1.jpg", alt:"img of D", major: "Computer Science", year:"Sophmore", info: "Bilingual in Spanish and English"},
                {name:"Parth",img:"../resources/img/boruto-1_1.png", alt:"img of P", major: "Computer Science", year:"Sophmore", info: "meh"}];

//loads the options in dropdown
function loadCreators(){
    for(membernum = 0; membernum < members.length; membernum++){
        var mem = document.getElementById("member_selector");
        var select = document.createElement('option');
        select.href = '#';
        select.innerHTML = members[membernum].name;
        mem.appendChild(select);
        select.setAttribute('onclick', "switchMembers(" + membernum + ")");
    }
}

//changes the data and images
function switchMembers(membernum){
    document.getElementById("m_name").innerHTML = members[membernum].name;
    document.getElementById("member_img").src = members[membernum].img;
    document.getElementById("member_img").alt = "member" + members[membernum].name;
    document.getElementById("m_year").innerHTML = members[membernum].year;
    document.getElementById("m_major").innerHTML = members[membernum].major;
    document.getElementById("m_info").innerHTML = members[membernum].info;
}