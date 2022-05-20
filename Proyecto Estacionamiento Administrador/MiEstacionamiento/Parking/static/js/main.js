let mainLocation = window.pageYOffset;
window.onscroll = function(){
    let transition = window.pageYOffset;
    if(mainLocation >= transition){
        this.document.getElementById('navbarr').style.top = '0';
    }
    else{
        document.getElementById('navbarr').style.top = '-100px';
    }
    mainLocation = transition;
}