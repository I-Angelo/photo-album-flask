const images = ["/static/images_carrousel/img1.jpeg", "/static/images_carrousel/img2.jpeg", "/static/images_carrousel/img3.jpeg", "/static/images_carrousel/img4.jpeg", "/static/images_carrousel/img5.jpeg",
 "/static/images_carrousel/img6.jpeg", "/static/images_carrousel/img7.jpeg", "/static/images_carrousel/img8.jpeg", "/static/images_carrousel/img9.jpeg", "/static/images_carrousel/img10.jpeg", "/static/images_carrousel/img11.jpeg"];
const carousel = document.querySelector(".carousel");
const interval = setInterval(function() {
    startCarousel();
}, 3000)
var index = 1;
var start = 0;

// startCarousel = () => {
//     // if(start < images.length) {
//     carousel.style.backgroundImage = `url(${images[index++]})`;
//     carousel.classList.remove("fade");
//     void carousel.offsetWidth;
//     carousel.classList.add("fade");
//     if(index > images.length -1) index - 0;
//     // }
// }

// setInterval(startCarousel,2000)
// while (start < images.length) {
//     startCarousel()
// }

// /////////////

function startCarousel(){
        if(start<images.length){
            // start=start+1;
            carousel.style.backgroundImage = `url(${images[start]})`;
            carousel.classList.remove("fade");
            void carousel.offsetWidth;
            carousel.classList.add("fade");
            start=start+1;
        }
        else{
            start=0;
        }
        // console.log(img);
        // img.innerHTML = "<img src="+slides[Start-1]+">";
       
    }
    // setInterval(startCarousel,3000);















// /////////////


// var img = document.getElementById('img');

// var slides = ["/static/images_carrousel/img1.jpeg", "/static/images_carrousel/img2.jpeg", "/static/images_carrousel/img3.jpeg", "/static/images_carrousel/img4.jpeg"];

// var Start=0;

// function slider(){
//     if(Start<slides.length){
//         Start=Start+1;
//         img.classList.add("fade");
//         void img.offsetWidth;
//         img.classList.remove("fade");
//     }
//     else{
//         Start=1;
//     }
//     console.log(img);
//     img.innerHTML = "<img src="+slides[Start-1]+">";
   
// }
// setInterval(slider,2000);
