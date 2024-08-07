function getDivId(divId) {
    const url = 'event/' + divId.replace(/ /g, '_');
    console.log(url);
    window.location.href = '/' + url;
        }
        document.addEventListener('DOMContentLoaded', function () {
            var mySwiper = new Swiper('.swiper-container', {
                slidesPerView: 3,
                spaceBetween: 30,
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev'
                },
                on: {
                    slideChange: function () {
                        if (this.isBeginning) {
                            document.querySelector('.swiper-button-prev').classList.add('hidden');
                        } else {
                            document.querySelector('.swiper-button-prev').classList.remove('hidden');
                        }
                        if (this.isEnd) {
                            document.querySelector('.swiper-button-next').classList.add('hidden');
                        } else {
                            document.querySelector('.swiper-button-next').classList.remove('hidden');
                        }
                    }
                }
            });
        });