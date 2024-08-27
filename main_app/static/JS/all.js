const imgSlider = document.querySelector('.img-slider');
const items = document.querySelectorAll('.item');
const imgItems = document.querySelectorAll('.img-item');
const infoItems = document.querySelectorAll('.info-item');

const nextBtn = document.querySelector('.next-btn');
const prevBtn = document.querySelector('.prev-btn');

let colors = ['#000000', '#002200', '#3f0101', '#001f3f', '#172233', '#120018'];

let indexSlider = 0;
let index = 0;

const slider = () => {
    imgSlider.style.transform = `rotate(${indexSlider * 60}deg)`;

    items.forEach(item => {
        item.style.transform = `rotate(${indexSlider * -60}deg)`;
    });
    
    document.querySelector('.img-item.active').classList.remove('active');
    imgItems[index].classList.add('active');

    document.querySelector('.info-item.active').classList.remove('active');
    infoItems[index].classList.add('active');

    document.body.style.background = colors[index];
}

nextBtn.addEventListener('click', () => {
    indexSlider++;

    index++;
    if (index > imgItems.length -1) {
        index = 0;
    }

    slider();
});

prevBtn.addEventListener('click', () => {
    indexSlider--;

    index--;
    if (index < 0) {
        index = imgItems.length - 1;
    }

    slider();
});