$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

var hours=24;
var now=new Data.getTime();
var stepTime=localStorage.getItem('stepTime')

if (stepTime==null){
    localStorage.setItem('stepTime', now)
}
else {
    if(now-stepTime>hours*60*60*1000)
    {
        localStorage.clear();
        localStorage.setItem('stepTime',now)
    }
}

var orders=JSON.parse(localStorage.getItem('orders'));
var total=localStorage.getItem('total');

if (orders==null || orders==undefined)
{
    localStorage.setItem('orders'.JSON.stringify([]));
    orders=JSON.parse(localStorage.getItem('orders'));
}

if (total==null || total==undefined)
{
    localStorage.setItem('total',0);
    total=localStorage.getItem('total');
}

var cart=document.querySelector('#cart');
cart.innerHTML=orders.length;